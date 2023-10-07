import pandas as pd
df = pd.read_csv('data.csv')
print(df)
print(df.to_string()) 
print(pd.options.display.max_rows) 
pd.options.display.max_rows = 10
print(pd.options.display.max_rows) 
print(df.head(1))
print(df.head())
print('-----------------------------------')
print (df.info())
