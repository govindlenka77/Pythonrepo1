import time
import datetime


class Product:
    def __init__(self, name, price, deal, rating):
        self.name = name
        self.price = price
        self.deal = deal
        self.rating = rating

    def displayproductdetails(self):
        print(self.name)
        print(self.price)
        print(self.deal)
        print(self.rating)

    @staticmethod
    def dec():
        print("---------------")


class Grocery(Product):
    def __init__(self, name, price, deal, rating, expire, package):
        super().__init__(name, price, deal, rating)
        self.expire = expire
        self.package = package

    def getexpiry(self):
        print(self.expire)

    def settime(self):
        self.ti = time.ctime()

    def time(self):
        return self.ti


class Electronics(Grocery):
    def __init__(self, name, price, deal, rating, expire, package, warranty):
        super().__init__(name, price, deal, rating, expire, package)
        self.warranty = warranty

    def getwarranty(self):
        print(self.warranty)

    def setdat(self):
        self.date = datetime.datetime.now()

    def disdate(self):
        print(self.date)


a1 = Grocery("govind", 9000, 50000, 100, "22-100-2025", "12-4-46")
a1.getexpiry()
a1.dec()
a1.settime()
print(a1.time())
a1.dec()
a1.displayproductdetails()
a1.dec()
a2 = Electronics("Abbas", 20, 19, 4.0, "20-5-2023", "1-10-1999", 5)
a2.settime()
print(a2.time())
a2.dec()
a2.displayproductdetails()
a2.dec()
a2.getexpiry()
a2.dec()
a2.getwarranty()
a2.dec()
a2.setdat()
a2.disdate()
a2.dec()
