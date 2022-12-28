class go:

    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)

    @staticmethod
    def ram(a):
        return a


    @classmethod
    def sita(cls,name):
        cls.name=name
        print("------------")
        print(cls.name)
        return cls.name


g1=go("arha",21)
g2=go("abhi",2)
a=go.ram(30)
b=go.ram(20)
print(a)
print(b)
p=go.sita("abbhaa")
print(p)
print(g1.ram(3))