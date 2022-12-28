import pyodbc
import mysql.connector

dataBase = mysql.connector.connect(
    host="HCL-02-85\SQLEXPRESS",
    user="capstone",
    passwd="Capstone@123"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

# creating database
cursorObject.execute("CREATE DATABASE geeks4geeks")


================
'''
    def append_project(self,new_project):
        self.new_project=new_project
        self.projects.append(self.new_project)
'''