import sys

from user_function import UserFunction
from login_function import LoginFunction
from food_function import FoodFunction

class LoginMain:

    def __init__(self, loginfunction_obj, userfunction_obj, foodfunction_obj):
        self.loginfunction_obj = loginfunction_obj
        self.userfunction_obj = userfunction_obj
        self.foodfunction_obj = foodfunction_obj

    def execute(self, choice):
        if choice == 1:
            print("==============Login===========")
            user_id = int(input("Enter the user id: "))
            user_password = input("Enter the password: ")
            result = loginfunction_obj.userValidation(user_id, user_password)
            if result == True:
                print("Login Success !!!")
                loginfunction_obj.mainMenu()
            else:
                print("Login failed check the username or password, contact tech support")
        elif choice == 2:
            print("==============Register=========")
            userfunction_obj.add_user_item()
        elif choice == 3:
            print("==============Exit============")
            sys.exit()
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    loginfunction_obj = LoginFunction()
    userfunction_obj = UserFunction()
    foodfunction_obj = FoodFunction()
    loginmain = LoginMain(loginfunction_obj, userfunction_obj, foodfunction_obj)

    while True:
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Welcome to the Edyoda Restaurant Project Online Food Management System")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("1.Login \n2.Sign Up \n3.Exit")
        choice = int(input("Enter your choice : "))
        loginmain.execute(choice)
