class Hcl:
    def __init__(self, sap_id, name, mail):
        self.sap_id = sap_id
        self.name = name
        self.mail = mail

    def get_sap_id(self):
        return self.sap_id

    def get_name(self):
        return self.name

    def display_details(self):
        print(self.sap_id, self.name, self.mail)


class Cisco:
    def __init__(self, cisco_id, location):
        self.cisco_id = cisco_id
        self.location = location
        self.dict1 = {}

    def add_item(self, a, b):
        self.dict1[a]=b

    def delete_item(self, a):
        del self.dict1[a]

    def display_cis(self):
        for i, j in self.dict1:
            print(i,j)

    def displ_upper(self):
        for i,j in self.dict1.items():
           #print(i.type(i))
            i.display_details()
            print(j)

    def update(self,a,name):
        a.name = name
        #for i in self.dict1.keys():
           # if(i==a):
                #i.name=name

    def pri(self):
        print(self.dict1)


a = Hcl(570, "Govi", "govi@")
b = Hcl(520, "adi", "adi@")
c1 = Cisco(112, "Hyde")
c1.add_item(a, 20)
c1.add_item(b,19)
c1.displ_upper()
#c1.display_cis()
#c1.display_cis()
c1.pri()
#c1.delete_item(a)
c1.update(a,"Govind")
c1.displ_upper()
