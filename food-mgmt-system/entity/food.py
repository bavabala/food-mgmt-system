class Food:
    def __init__(self,food_id,food_item,food_quantity,food_price,food_discount,food_stock_left):
        self.food_id = food_id
        self.food_item = food_item
        self.food_quantity = food_quantity
        self.food_price = food_price
        self.food_discount = food_discount
        self.food_stock_left = food_stock_left

    def __str__(self):
        return f"Food ID : {self.food_id} \nFood Item : {self.food_item} \nFood Quantity : {self.food_quantity} \nFood Price : {self.food_price} \nFood discount : {self.food_discount} \nFood stock left : {self.food_stock_left}"

    def set_food_id(self,food_id):
        self.food_id = food_id
    
    def get_food_id(self,food_id):
        self.food_id = food_id

    def set_food_item (self,food_item):
        self.food_item = food_item
    
    def get_food_item(self,food_item):
        self.food_item = food_item

    def set_food_quantity(self,food_quantity):
        self.food_quantity =food_quantity

    def get_food_quantity(self,food_quantity):
        self.food_quantity = food_quantity

    def set_food_price(self,food_price):
        self.food_price = food_price

    def get_food_price(self,food_price):
        self.food_price = food_price

    def set_food_discount(self,food_discount):
        self.food_discount = food_discount

    def get_food_discount(self,food_discount):
        self.food_discount = food_discount

    def set_food_stock_left(self,food_stock_left):
        self.food_stock_left =food_stock_left

    def get_food_stock_left(self,food_stock_left):
        self.food_stock_left = food_stock_left
    



    