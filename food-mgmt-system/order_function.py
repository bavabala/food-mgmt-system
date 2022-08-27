from entity.order import Order
from food_function import FoodFunction

class OrderFunction:
    orderlist = []

    def add_Order(self):
        order_item = input("Enter the Order Item:  ")
        order_quantity = int(input("Enter the Order quantity: "))
        order_price = int(input("Enter the Order price: "))
        order_obj = Order(order_item,order_quantity,order_price)
        self.orderlist.append(order_obj)
        print("Food successfully ordered!")

    def view_Order(self):
        for i in self.orderlist:
            print()
            print(i)

    def remove_Order(self):
        order_item = int(input("Enter order item of the Order you want to delete: "))
        for Order in self.orderlist:
            if Order.order_id == order_item:
                self.orderlist.remove(Order)
                print("Successfully Deleted Order")
                break
            else:
                print("No Order Found!")

    def execute(self, choice):
        if choice == 1:
            print("==============add_Order===========")
            foodFunctionObj = FoodFunction()
            foodFunctionObj.view_food_item()
            self.add_Order()
        elif choice == 2:
            print("==============view Order=========")
            self.view_Order()
        self.orderRootFunction()

    def orderRootFunction(self):
        print("=======================================")
        print("Choose option Order Management: \n1.add_Order \n2.view_Order \n3.Back to menu \n4.Main Menu")
        choice = int(input("Enter your choice : "))
        if choice == 3:
            return 1
        elif choice == 4:
            return 0
        else:
            self.execute(choice)
