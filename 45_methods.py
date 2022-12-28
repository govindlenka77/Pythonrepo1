"""class a:
    p=1
    def l(self):
        print("DDDDDDDD",self.p)

print(a.p)
x=a()
x.l()
"""
class aclass:
    r=4000
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def leela(cls,name,age):
        cls.name=name
        cls.age=age
        print(cls.name)
        print(cls.age)
        #print(self.name)
        #print(r)

x=aclass("Bobby",20)
x.leela("arha",10)
y=aclass("keerthi",20)
y.leela("keerthi",19)
print(x.name)
print(y.name)
print(x.age)
print(y.age)
