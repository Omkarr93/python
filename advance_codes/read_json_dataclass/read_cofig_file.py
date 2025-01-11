import json
from dataclasses import dataclass
from typing import List
import sys

# Define the Config class
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

# Function to read and parse JSON, converting it to a list of Config objects
def get_configuration_details(file_path: str) -> List[Config]:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)  # Read JSON file as Python dictionaries
    print(data)
    # Convert each dictionary to a Config object
    config_objects = [Config(**item) for item in data]
    return config_objects

config_file = "D:/python/advance_codes/read_json_dataclass/config.json"  # Path to the sample JSON file
configs = get_configuration_details(config_file)


print(configs)
# Print the Config objects to verify
sys.exit(0)
for config in configs:
    print(config)
