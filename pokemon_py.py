'''

import pandas as pd
import numpy as np

file1=pd.read_csv("C:\\Users\\user706\\Downloads\\pokemon_data.csv") #C:\\Users\\user706\\Downloads\\pokemon_data.csv
print(file1)        #C:\\Users\\user706\\Downloads\\pokemon_data.txt
print(file1.head(5))
print(file1.tail(5))
print(file1.columns)
print(file1["HP"])
#for index,row in file1.iterrows():
#print(index,row["Name"])

print(file1.Name)

#slicing eith dataframe
print(file1[0:3])

#select LOC and AT
print(file1.loc[:,["Name","Generation"]]) #index as input to the loc
print(file1.loc[0:4,["Name","Generation"]])
print(file1.iloc[3:5,0:2])
print(file1.iloc[[1,2,3],[0,2]])

#boolean indexing
print(file1["Speed"]>150)   #gives the indexes and true or false for each index
print(file1[file1["Speed"]>150])    #gives the data for each index


#is in
file2=file1.copy()
file2[1]='arha'         #creates a column in dataframe by name 1 and value=arha
print(file2.head(3))
print(file2[file2[1].isin([1])])    #no use.. dont know why

file2=file1.copy()
file2['arha']='abc'
print(file2)                    #i didnt understand is in usage

#drop column
file1.drop(1)

'''

import pandas as pd
import numpy as np

file1=pd.read_csv("C:\\Users\\user706\\Downloads\\pokemon_data.csv") #C:\\Users\\user706\\Downloads\\pokemon_data.csv
print(file1)

#print(file1[file1["Type 1"].isin(['Grass','Fire'])])        #isin usage

print(file1.mean())
print(file1.mean(1))
'''
dates=pd.date_range("20220101",periods=6)
s=pd.Series([1,3,5,np.NAN,6,8],index=dates).shift(2)        #i didnt understand this
file1.sub(s,axis="index")
print(s)
'''

import pandas as pd
import numpy as np
s=pd.Series(["A","B","C","aaba","baca","caba","dog","cat"])
print(s.str.lower)