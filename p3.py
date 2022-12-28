import pandas as pd
import numpy as np
import re
df_xlsx=pd.read_excel("C:\\Users\\user706\\Desktop\\pokemon_data.xlsx")
#print(df_xlsx)

'''
print(df_xlsx.columns)
x=df_xlsx[["Attack","Defense","Speed"]]
print(x.sum())
x=x.iloc[1::2]
print(x.sum())
print(x)





print(df_xlsx)
y=df_xlsx["Type 1"]
print(y)
df_xlsx["Type 1"]=df_xlsx["Type 2"]
print(df_xlsx[["Type 1","Type 2"]])
df_xlsx["Type 2"]=y
print(df_xlsx[["Type 1","Type 2"]])




#regex='A.*'
#new_df=df_xlsx[df_xlsx["Name"].str.match(regex)]
new_df2=df_xlsx.loc[df_xlsx["Name"].str.contains('^A[a-z]*',flags=re.I,regex=True)]
new_df2.reset_index(drop=True,inplace=True)

print(new_df2)





print(df_xlsx.index.size)
date=pd.date_range("20220101",periods=df_xlsx.index.size)
print(date)
df_xlsx.set_index(date,inplace=True)
print(df_xlsx)






'''



