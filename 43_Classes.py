"""
class car:
    a = "dummy"

    def samp(self, a):
        print(a)
        print(self.a)


car1 = car()
car2=car()
car1.samp("Hii")
car2.samp(2)

#ERROR
class car():
    a="haha"
    b="hehe"
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def display(self):
        print(self.name)
        print(self.model)

car1=car("audi","A5")
car1.display()


class stat():
    @staticmethod
    def samp(x,y):
        return x+y

    @staticmethod
    def samp2(x,y):
        return x*y

stat1=stat()
out1=stat1.samp(2,3)
print(out1)
out2=stat1.samp2(5,10)
print(out2)

"""
class dog():
    att1="arha"

    def __init__(self,name):
        self.name=name

    def chan(self,name):
        self.name=name

a1=dog("ara")
print(a1.name)
a1.chan("a")
print(a1.name)