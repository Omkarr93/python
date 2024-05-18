# import os 
import nsepy
import pandas as pd

thisinfo  = {
    "brand" : ["omkar","Dev","Digvijay"],
    "age" : [27,30,20],
    "Designation" : ["ASE","DSE","SDE"]
}

print(thisinfo)

# data = pd.Series(thisinfo)
data = pd.DataFrame(thisinfo)

# df = thisinfo



print(data)
print(data.head())