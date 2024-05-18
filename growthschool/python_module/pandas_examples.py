import pandas as pd


data = {'name': ['omkar','vikram','kunal','sushant'],
        'age' : [25,26,27,28],
        'city': ['Kolhapur','pandharpur','satara','pune']}

data1 = {'name': ['rahul'],
        'age' : [28],
        'city': ['sangli']}

df = pd.concat([data,data1],axis=0)

print(df)
# df = pd.DataFrame(data)
#
# s = pd.Series(['a','b','c','d'])
#
# print(s)
# print(df)






