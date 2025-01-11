class Database(Enum):
    Management = 1
    SDProduction = 2
    Measure = 3
    Janus_Ops = 4
 
 
class Measure:
    def __init__(self, computationType: str, measureId: str, measureStartDate: str = None, measureEndDate: str = None, childMeasures: str = '') -> None:
        self.ComputationType = computationType
        self.MeasureId = measureId
        self.MeasureStartDate = measureStartDate
        self.MeasureEndDate = measureEndDate
        self.ChildMeasures = childMeasures
 
 
@dataclass
class Input:
    Unit: str
    IsPatientSpecific: int
    MeasureId: List[str]
    EntityId: int
    ParentEntityId: List[int]
    MeasureDetails: list = field(default_factory=list)
    EntityName: str = "practice"
    ParentEntityName: str = "practice"
    DurationFrom: str = "2024-01-01 00:00:00"
    DurationTo: str = "2024-12-31 23:59:59"
    IsDataIncompleteRequired: bool = True
    IsSIPractice: int = 1
    Flag: str = "MNR"
 
 
@dataclass
class Config:
    Registry: str
    MicroserviceHost: str
    MicroservicePort: str
    From: str
    To: str
    PostgresHost: str
    PostgresPort: str
    PostgresUser: str
    PostgresPassword: str
    JiraProject: str
    Management: str
    Measure: str
    JanusHost: str
    SplitBy: str = None
 
 
def getConfigurationDetails() -> List[Config]:
    configPath = f"{SCRIPT_FOLDER}/verification.json"
    codec = codecs.open(configPath, "r", "utf-8-sig")
    return json.load(codec, object_hook=lambda a: Config(**a))
 
 
def getConnectionString(appInfo: Config, database: Database, year: str = None) -> str:
    escapedPassword = quote(appInfo.PostgresPassword)
    return {
        Database.Management: f"postgresql+psycopg2://{appInfo.PostgresUser}:{escapedPassword}@{appInfo.PostgresHost}:{appInfo.PostgresPort}/{appInfo.Management}",
        Database.SDProduction: f"postgresql+psycopg2://{appInfo.PostgresUser}:{escapedPassword}@{appInfo.PostgresHost}:{appInfo.PostgresPort}/sdproduction",
        Database.Measure: f"postgresql+psycopg2://{appInfo.PostgresUser}:{escapedPassword}@{appInfo.PostgresHost}:{appInfo.PostgresPort}/{appInfo.Measure}",
        Database.Janus_Ops: f"postgresql+psycopg2://{appInfo.PostgresUser}:{escapedPassword}@{appInfo.JanusHost}:{appInfo.PostgresPort}/janus_ops_{year}",
    }.get(database)
 
 
def getData(connStr: str, query: str, params: dict = None) -> pandas.DataFrame:
    engine = create_engine(connStr)
    df = pandas.read_sql_query(text(query), engine, params=params)
    engine.dispose()
    return df
 
 
def transformToMeasure(x) -> Measure:
    computationType = str(x['computationtype'])
 
    if computationType is None:
        childMeasure: str = ''
    else:
        match = re.search('Derived_WeightedAvg_\{(.*)\}', computationType)
        childMeasure = '' if match is None else match.group(1)
 
    measure = Measure(
        computationType, str(x['measureno']), str(x['measurestartdate']), str(x['measureenddate']), childMeasure)
    return measure
 
 
def transformToPayload(x) -> Input:
    measureDetails = json.dumps(x[8].__dict__)
    item = Input(x[9], int(x[6]), [x[2]], int(x[1]), [int(x[1])])
    item.MeasureDetails.append(measureDetails)
    return item
 
 
def makeRequest(input: Input, appInfo: Config) -> Response:
    url = f'http://{appInfo.MicroserviceHost}:{appInfo.MicroservicePort}/Performance/GetAllMeasureOutput'
    headers = {"Content-Type": "application/json"}
    item = json.dumps(input.__dict__)
    item = item.replace('["{', '[{').replace('}"]', '}]').replace('\\"', '"')
    payload = '{"FilterMeasureInfo": ' + item + '}'
 
    return request("POST", url, data=payload, headers=headers)
 
 
year = sys.argv[1]
registryList = sys.argv[2]
 
argsLength = len(sys.argv)
 
match argsLength:
    case 3:
        pass
    case 4:
        days = float(sys.argv[3])
        now = datetime.datetime.now()
        startDate = (now - datetime.timedelta(days=days)).strftime("%Y-%m-%d")
        endDate = now.strftime("%Y-%m-%d")
    case 5:
        startDate = sys.argv[3]
        endDate = sys.argv[4]
    case _:
        print("Invalid number of inputs. Exiting...")
        exit(0)
 
config = getConfigurationDetails()
 
for registry in registryList.split(','):
    try:
        registryInfo = next(x for x in config if registry == x.Registry)
 
        # get measure details
        params = {
            'year': year
        }
        connStr = getConnectionString(registryInfo, Database.Measure)
        measureDF = getData(connStr, MEASURE_QUERY, params)
 
        measureDF['measureObj'] = measureDF.apply(transformToMeasure, axis=1)
        measureDF.set_index('measure_id', inplace=True)
 
        match argsLength:
            case 3:
                # get active measure-practice list
                params['jiraProject'] = registryInfo.JiraProject
                connStr = getConnectionString(
                    registryInfo, Database.SDProduction)
                activeDF = getData(connStr, SDPRODUCTION_PRACTICE_QUERY, params) \
                    .set_index('practice_id')
 
                # get big-ids and join with the above dfs
                connStr = getConnectionString(
                    registryInfo, Database.Management)
                df = getData(connStr, PRACTICE_QUERY) \
                    .set_index('practice_id') \
                    .join(activeDF, how='inner') \
                    .reset_index() \
                    .set_index('measure_id') \
                    .join(measureDF, how='inner') \
                    .reset_index()
 
            case 4 | 5:
                params = {
                    'registry': registry,
                    'sDate': startDate,
                    'eDate': endDate
                }
 
                connStr = getConnectionString(
                    registryInfo, Database.Janus_Ops, year)
                df = getData(connStr, DURATION_LOG_QUERY, params) \
                    .set_index('measure_id') \
                    .join(measureDF, how='inner') \
                    .reset_index()
 
        df['Unit'] = registry
 
        outputList = []
        threadList: List[threading.Thread] = []
 
        def unitIteration(a):
            payload = transformToPayload(a)
            response = makeRequest(payload, registryInfo)
 
            output = json.loads(response.text)
            items = output["ResultInfo"]["Data"]["MeasureDetailInfo"]
 
            if type(items) is list:
                outputList.extend(items)
                print(items)
            else:
                print(f'Measure = {str(row[3])} | Error = {response.text}')
 
        maxThreadCount = 5
 
        for index, row in df.iterrows():
            thread = threading.Thread(target=unitIteration, kwargs={'a': row})
            thread.start()
            threadList.append(thread)
 
            while len(threadList) == maxThreadCount:
                for thr in threadList:
                    if not thr in threading.enumerate():
                        threadList.remove(thr)
 
        for thread in threadList:
            thread.join()
 
        measureDF.reset_index().set_index('measureno', inplace=True)
 
        outputDF = pandas.DataFrame(outputList) \
            .rename({'MeasureId': 'measureno'}, axis=1)  \
            .set_index('measureno') \
            .join(measureDF[['ispatientspecific', 'isinverse', 'measureno']], how='inner', rsuffix='_right') \
            .rename({'ispatientspecific_right': 'ispatientspecific', 'isinverse_right': 'isinverse'}, axis=1)
 
        def transformPatientSpecific(x) -> str:
            return 'Yes' if int(x['ispatientspecific']) == 1 else 'No'
 
        def transformInverse(x) -> str:
            return 'Yes' if int(x['isinverse']) == 1 else 'No'
 
        outputDF['Patient Specific'] = outputDF.apply(
            transformPatientSpecific, axis=1)
        outputDF['Inverse'] = outputDF.apply(transformInverse, axis=1)
 
        REPORT_PATH = f'{SCRIPT_FOLDER}/{registry}_{datetime.datetime.now().strftime("%Y%m%d")}.csv'
 
        outputDF.reset_index(drop=True) \
            .rename(PAYLOAD_OUTPUT_MAPPER, axis=1)[OUTPUT_COLUMNS] \
            .to_csv(REPORT_PATH, sep='|', index=False)
    except StopIteration:
        print('Registry does not match with expected values.')