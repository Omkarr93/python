import numpy as np
import pandas as pd

dict1 = {
    "name": ['Omkar', 'Raj', 'Neha', 'Pratik'],
    "Marks": [91, 52, 42, 32],
    "city": ['kolhapur', 'Pune', 'Pune', 'Mumbai']
}

# df = pd.DataFrame(dict1)
#
# print(df)
# df.to_csv('testcsv_file.csv')
# df.head(2)
# df.to_csv('testcsv_file_NOindex.csv',index = False)

omkar = pd.read_csv('Omkar1.csv')

print(omkar)