class a:
    r=10
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @staticmethod
    def sat(a,b):
        print(a)
        print(b)
        #print(self.name)       ERROR
        #print(self.age)        ERROR   because STATIC METHOD
        #print(r)               ERROR

x=a("arha",10)
x.sat(20,10)
