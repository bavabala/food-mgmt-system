from user_function import UserFunction
from food_function import FoodFunction
from order_function import OrderFunction

class LoginFunction:

    def userValidation(self, userId, password):
        userfunction_obj = UserFunction()
        for user in userfunction_obj.UserList:
            if user.user_id == userId and password.__eq__(user.user_password):
                return True
            else:
                return False

    def mainMenu(self):
        print("Menu \n1.Food \n2.User \n3.Order Management \n4.Exit")
        option = int(input("Enter the option to navigate : "))
        foodfunction_obj = FoodFunction()
        userfunction_obj = UserFunction()
        Orderfunction_obj = OrderFunction()
        if option == 1:
            if foodfunction_obj.foodRootFunction() == 1:
                self.mainMenu()
            else:
                return
        elif option == 2:
            if userfunction_obj.userRootFunction() ==1:
                self.mainMenu()
            else:
                return
        elif option == 3:
            if Orderfunction_obj.orderRootFunction() == 1:
                self.mainMenu()
            else:
                return
        elif option == 4:
            return 0
