import numpy as np
import pandas as pd
import random

#df=pd.read_csv('data1')
#print(df)
#print()
#print(df.loc[[0,2,1]]) #prints the values in the indices in the given order
#print(pd.__version__)
'''
a=[3,3,4,5]
series=pd.Series(a)
print(series)
arha=pd.Series(a,index=[3,6,10,9])
print(arha)


print(df.head(3))
print(df.tail(2))
print(df.info)
data=pd.DataFrame(df)
print(data)

#print(df.to_string())

dict1={'names':['arha','allu','neha'],'ages':[20,39,20]}
print(dict1)
frame1=pd.DataFrame(dict1)
print(frame1)
print(frame1.names[2]) #accesssing values in the dataframe is possible using this technique
print(pd.options.display.max_rows) #number of rows
pd.options.display.max_rows=3
df=pd.read_csv('data1')
print(df)
print(pd.options.display.max_rows)


dates=pd.date_range("20220201",periods=5)
s1=pd.Series(dates)
print(dates)
print(s1)


x=pd.Series([1,2,3,np.NaN,7])
y=pd.Series([1,2,3,4])
print(y)
print(x)
print(x[3])

'''

date=pd.date_range("20220101",periods=5)
df=pd.DataFrame(np.random.rand(5,4),index=date,columns=list("ABCD"))
print(df)


'''
df2=pd.DataFrame(
    {
        "A":1,
        "B":pd.Timestamp("20220112"),
        "C":pd.Series(1,index=list(range(5)),dtype="float32"),
        "D":np.array([3]*5,dtype="int32"),
        "E":pd.Categorical(["test","traim","tat","tat","test"]),
        "F":"foo",
    }
)
print(df2)
print(df2.dtypes)
print(df2.head(2))
print(df2.columns)
print(df2.index)
print(df2.to_numpy())
print(df2.describe())
print(df2.T)
'''

print(df.sort_index(axis=0,ascending=True))
print()