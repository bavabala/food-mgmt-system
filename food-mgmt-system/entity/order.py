class Order:
    def __init__(self, order_item, order_quantity, order_price):
        self.order_item = order_item
        self.order_quantity = order_quantity
        self.order_price = order_price

    def __str__(self):
        return f"Order Item : {self.order_item} \nOrder Quantity : {self.order_quantity} \nOrder Price : {self.order_price} "

    def set_order_item(self, order_item):
        self.order_item = order_item

    def get_order_item(self, order_item):
        self.order_item = order_item

    def set_order_quantity(self, order_quantity):
        self.order_quantity = order_quantity

    def get_order_quantity(self, order_quantity):
        self.order_quantity = order_quantity

    def set_order_price(self, order_price):
        self.order_price = order_price

    def get_order_price(self, order_price):
        self.order_price = order_price



