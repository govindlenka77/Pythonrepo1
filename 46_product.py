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

class electronics:
    def __init__(self,warranty):
        self.warranty=warranty

    def getwarranty(self):
        print(self.warranty)

class grocery:
    def __init__(self,expire,package):
        self.expire=expire
        self.package=package
    def getexpiry(self):
        print(self.expire)

a1=product("harsha",2000,1500,4.5)
a1.displayproductdetails()
b1=electronics(2)
b1.getwarranty()
c1=grocery("22-10-2023","10-5-2022")
c1.getexpiry()
