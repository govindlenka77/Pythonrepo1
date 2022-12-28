import pyodbc

server = "HCL-02-85\SQLEXPRESS"
database = "Govind1"
username = "capstone"
password = "Capstone@123"

cnxn = pyodbc.connect(
    'DRIVER={ODBC DRIVER 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
# print(cnxn)
cursor = cnxn.cursor()


# cursor.execute('''insert into govindtable
# values(52130571,'Lenka')''')
# cursor.commit()

class BonusError(Exception):
    pass


class Employee:
    Bonus = 2
    projects = ['python', 'c', 'java']

    def __init__(self, id, name, salary, project):
        self.id = id
        self.name = name
        self.salary = salary
        self.project = project
        try:
            cursor.execute('''create table govindtable
            ( id int not null,
            primary key(id),
            names varchar(20),
            salary int,
            project varchar(20),
            )''')
            cursor.commit()
            if self.project in self.projects:
                self.insert_employee_details(self.id, self.name, self.salary, self.project)
            else:
                print("Unable insert data due to incorrect project name")
        except pyodbc.ProgrammingError:
            print("Table is already created")
            if self.project in self.projects:
                self.insert_employee_details(self.id, self.name, self.salary, self.project)
            else:
                print("Unable insert data due to incorrect project name")

    def insert_employee_details(self, id1, name1, salary1, project1):
        if project1 in self.projects:
            try:
                query = '''insert into govindtable values({0},'{1}',{2},'{3}')'''.format(id1, name1, salary1, project1)
                cursor.execute(query)
                cursor.commit()
            except pyodbc.IntegrityError:
                print("Data with this same id exists in the database\nintentionally stopping the execution ")
                exit()
        else:
            print("Unable to insert because project is not in the available list")

    def update_salary(self, updated_sal, id):
        self.salary = updated_sal
        x = "update govindtable set salary={0} where id='{1}'"
        query = x.format(self.salary, id)
        # print(query)
        cursor.execute(query)
        cursor.commit()

    def add_bonus(self, real_bonus, id):
        self.real_bonus = real_bonus
        try:
            if (self.Bonus > real_bonus and real_bonus>=0):
                self.salary = ((self.real_bonus)  * self.salary)//10 + self.salary
                self.update_salary(self.salary, id)
            else:
                raise BonusError
        except BonusError:
            print("Very High Bonus is not applicable")

    def display_employee_datails(self, id):
        self.id = id
        x = "select * from govindtable where id={0}"
        query = x.format(self.id)
        # print(query)
        val = cursor.execute(query)
        for i in val:
            print(i)
        print("=====")

    def change_project(self, id, changed_project_name):
        self.changed_name = changed_project_name
        if self.changed_name in self.projects:
            x = "update govindtable set project='{0}' where id='{1}'".format(changed_project_name, id)
            # print(x)
            cursor.execute(x)
            cursor.commit()
        else:
            print("Can not change the project name to the unknown project name")

    def drop_table(self):
        query = '''drop table govindtable'''
        cursor.execute(query)
        cursor.commit()
        print("Table is deleted ")

    def display_table(self):
        x = "select * from govindtable"
        # print(query)
        val = cursor.execute(x)
        for i in val:
            print(i)
        print("------")

    def delete_details(self, id):
        x = "delete from govindtable where id={}".format(id)
        cursor.execute(x)
        cursor.commit()
        print("row is deleted")


obj1 = Employee(9, 'ravi', 2000, 'c')
obj1.display_table()
#obj1.insert_employee_details(7, 'arha', 300, 'python')
# obj1.display_employee_datails(1)
obj1.display_table()
obj1.update_salary(10000,1)
obj1.display_employee_datails(1)
obj1.add_bonus(1.5,1)
# print("----")
obj1.display_table()
obj1.change_project(1, 'c#')
obj1.display_table()
# obj1.display_employee_datails(5)
# obj1.projects.append('c++')
# print(obj1.projects)
# obj1.drop_table()
#obj1.delete_details(1)
obj1.display_table()
