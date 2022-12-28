import pyodbc

server = "HCL-02-85\SQLEXPRESS"
database = "Govind1"
username = "capstone"
password = "Capstone@123"

cnxn=pyodbc.connect('DRIVER={ODBC DRIVER 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
print(cnxn)
cursor = cnxn.cursor()
try:
    cursor.execute('''create table govindtable
        ( names varchar(20),
        salary int,
        project varchar(20),
        )''')
    cursor.commit()
except pyodbc.ProgrammingError:
    print("Table is already created")


#cursor.execute('''insert into govindtable
#values(52130571,'Lenka')''')
#cursor.commit()

class BonusError(Exception):
    pass

class Employee:
    Bonus=2
    projects=['python','c','java']

    def __init__(self,name,salary,project):
        self.name=name
        self.salary=salary
        self.project=project
        if self.project in self.projects:
            self.insert_employee_details()
        else:
            print("Unable insert data due to incorrect project name")

    def insert_employee_details(self):
        query='''insert into govindtable values('{0}',{1},'{2}')'''.format(self.name,self.salary,self.project)
        #print(query)
        cursor.execute(query)
        cursor.commit()

    def update_salary(self,updated_sal,emp_name2):
        self.salary=updated_sal
        x="update govindtable set salary={0} where names='{1}'"
        query=x.format(self.salary,emp_name2)
        #print(query)
        cursor.execute(query)
        cursor.commit()

    def add_bonus(self,real_bonus,emp_name5):
        self.emp_name5=emp_name5
        self.real_bonus=real_bonus
        try:
            if(self.Bonus>real_bonus):
                self.salary=(self.real_bonus)*10*self.salary+self.salary
                self.update_salary(self.salary,self.emp_name5)
            else:
                raise BonusError
        except BonusError:
            print("Very High Bonus is not applicable")

    def display_employee_datails(self,emp_name):
        x="select * from govindtable where names='{0}'"
        query=x.format(emp_name)
        #print(query)
        val=cursor.execute(query)
        for i in val:
            print(i)

    def change_project(self, emp_name1, changed_project_name):
        self.emp_name1=emp_name1
        self.changed_name=changed_project_name
        x="update govindtable set project='{0}' where names='{1}'".format(changed_project_name, emp_name1)
        print(x)
        cursor.execute(x)
        cursor.commit()

    def drop_table(self):
        query='''drop table govindtable'''
        cursor.execute(query)
        cursor.commit()


obj1=Employee('ravi',2000,'c')
obj1.display_employee_datails('ravi')
'''
obj1.update_salary(100,'ravi')
obj1.display_employee_datails('ravi')
obj1.add_bonus(1.5,'ravi')
obj1.change_project('ravi','java')
obj1.display_employee_datails('ravi')'''






#cursor.execute('''delete from govindtable where surname='Lenka' ''')
#cursor.commit()
