import time
class product:
    def __init__(self,name,price,deal,rating):
        self.name = name
        self.price = price
        self.deal = deal
        self.rating = rating

    def displayproductdetails(self):
        print(self.name)
        print(self.price)
        print(self.deal)
        print(self.rating)

    def erase(self):
        self.r1="r1"
        print(self.r1)

class electronics:
    def __init__(self,warranty):
        self.warranty=warranty

    def getwarranty(self):
        print(self.warranty)

    def erase(self):
        self.e1="Harsha"
        print(self.e1)

class grocery(product):
    def __init__(self,name,price,deal,rating,expire,package):
        super().__init__(name,price,deal,rating)
        self.expire=expire
        self.package=package
    def getexpiry(self):
        print(self.expire)

    def settime(self):
        self.ti=time.ctime()

    def time(self):
        return self.ti

    def erase1(self):
        super().erase()
        self.e1="Govind"
        print(self.e1)
        return "Nothing"


a1=product("harsha",2000,1500,4.5)
a1.displayproductdetails()
b1=electronics(2)
b1.getwarranty()
c1=grocery("harsha",2000,1500,4.5,"22-10-2023","10-5-2022")
c1.getexpiry()
c1.displayproductdetails()
c1.settime()
print(c1.time())
print(c1.erase1())
