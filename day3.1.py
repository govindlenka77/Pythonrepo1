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

    def create_table(self):
        try:
            cursor.execute('''create table govindtable
            ( id int not null,
            primary key(id),
            names varchar(20),
            salary int,
            project varchar(20),
            )''')
            cnxn.commit()
            print("Table is created..")
        except pyodbc.ProgrammingError:
            print("Table is already created")

    def insert_employee_details(self, id1, name1, salary1, project1):
        try:
            if project1 in self.projects:
                try:
                    query = '''insert into govindtable values({0},'{1}',{2},'{3}')'''.format(id1, name1, salary1,
                                                                                             project1)
                    cursor.execute(query)
                    cursor.commit()
                except pyodbc.IntegrityError:
                    print("Data with this same id exists in the database\nintentionally stopping the execution ")
                    exit()
            else:
                print("Unable to insert because project is not in the available list")
        except:
            print("table is not existed in the database")

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
            if (self.Bonus > real_bonus):
                self.salary = (self.real_bonus) * 10 * self.salary + self.salary
                self.update_salary(self.salary, id)
            else:
                raise BonusError
        except BonusError:
            print("Very High Bonus is not applicable")

    def display_employee_datails(self, id):
        try:
            self.id = id
            x = "select * from govindtable where id={0}"
            query = x.format(self.id)
            # print(query)
            val = cursor.execute(query)
            for i in val:
                print(i)
        except:
            print("There are employee details and no table ")

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
        try:
            query = '''drop table govindtable'''
            cursor.execute(query)
            cursor.commit()
            print("Table is deleted ")
        except:
            print("Table is already deleted..")


    def display_table(self):
        try:
            x = "select * from govindtable"
            # print(query)
            val = cursor.execute(x)
            for i in val:
                print(i)
            print("------")
        except:
            print("Table is empty")

    def delete_details(self, id):
        try:
            x = "delete from govindtable where id={}".format(id)
            cursor.execute(x)
            cursor.commit()
            print("row is deleted")
        except:
            print("There is no table to delete the details")


obj1 = Employee()
obj1.create_table()
#obj1.drop_table()
#obj1.drop_table()
obj1.display_table()
obj1.insert_employee_details(1, 'arha', 300, 'c')
obj1.display_employee_datails(1)
#obj1.display_table()
obj1.update_salary(10000,1)
obj1.display_employee_datails(1)
obj1.add_bonus(1.5,1)
# print("----")
# obj1.display_table()
obj1.change_project(1, 'c#')
obj1.display_table()
#obj1.display_employee_datails(5)
obj1.projects.append('c++')
print(obj1.projects)
obj1.insert_employee_details(3,'sam',9876,'c++')
# obj1.drop_table()
#obj1.delete_details(1)
obj1.display_table()
