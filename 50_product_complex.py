class Product:
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings

    def display_product_details(self):
        print(self.name, ";", self.price, ";", self.deal_price, ";", self.ratings)

    def get_deal_price(self):
        return self.deal_price


class ElectronicItem(Product):
    def set_warranty(self, warranty_in_months):
        self.warranty_in_months = warranty_in_months

    def get_warranty(self):
        return self.warranty_in_months


class GroceryItem(Product):
    pass


class Order:
    def __init__(self, delivery_speed, delivery_address):
        self.items_in_cart = []
        self.delivery_speed = delivery_speed
        self.delivery_address = delivery_address

    def add_item(self, product, quantity):
        self.items_in_cart.append((product, quantity))

    def display_order_details(self):
        for product, quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity: ", quantity)


tv = ElectronicItem("TV", 20000, 19000, 4.0)
milk = GroceryItem("MILK", 40, 25, 3.5)
mobile = ElectronicItem("MOBILE", 20000, 20000, 4.8)
ord1 = Order("Prime delivery", "Hyderabad")

ord1.add_item(tv, 3)
ord1.add_item(mobile, 5)
ord1.display_order_details()
