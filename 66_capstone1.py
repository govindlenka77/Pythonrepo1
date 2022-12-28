import pyodbc
server='HCL-02-85\SQLEXPRESS'
database='FileSearchResults'
username='capstone'
password='Capstone@123'
cnxn=pyodbc.connect('DRIVER={ODBC DRIVER 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
print(cnxn)
cursor=cnxn.cursor()
print(cursor)
cursor.execute('''INSERT INTO FileSearchResults_table(NameOfFile,File_Location,SearchCount)
values('bike','E:\arha1\arha2\arha3\arha4\arha5.txt',1)''')
cnxn.commit()
values=cursor.execute('''select * from FileSearchResults_table''')
for i in values:
    print(i)