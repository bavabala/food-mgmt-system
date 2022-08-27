from entity.user import user

class UserFunction:
    UserList = []
    def add_user_item(self):
        user_id = int(input("Enter the user ID: "))
        user_name = input("Enter the user name: ")
        user_mobile = int(input("Enter the user mobile: "))
        user_email = input("Enter the user_email: ")
        user_adddress = input("Enter the user address:" )
        user_password = input("Enter the user password: ")
        user_profile = input("Enter the user profile: ")
        user_obj = user(user_id,user_name,user_mobile,user_email,user_adddress,user_password,user_profile)
        self.UserList.append(user_obj)
        print("User Successfully Added")

    def view_user_item(self):
        for i in self.UserList:
            print()
            print(i)

    def edit_user_name(self):
        edit_user_name = input("Enter the edit user name: ")
        for User in self.UserList:
             if User.user_name == edit_user_name:
                 user_name = input("Enter the User name:  ")
                 user_mobile = int(input("Enter the user_mobile: "))
                 user_email = input("Enter the user_email: ")
                 user_address = (input("Enter the user address: "))
                 user_password = (input("Enter the user password: "))

                 User.set_user_name(user_name)
                 User.set_user_mobile(user_mobile)
                 User.set_user_email(user_email)
                 User.set_user_address(user_address)
                 User.set_user_password(user_password)
                 print("succesfully edited user")
                 break
             else:
                print("user item not found!")

    def remove_user_name(self):
        user_id = int(input("Enter USer Id of the food you want to delete: "))
        for Users in self.UserList:
            if Users.user_id == user_id:
                self.UserList.remove(Users)
                print("Successfully Deleted User")
                break
        else:
            print("No user Found!")

    def execute(self, choice):
        if choice == 1:
            print("==============add_user_item===========")
            self.add_user_item()
        elif choice == 2:
            print("==============view user item=========")
            self.view_user_item()
        elif choice == 3:
            print("==============edit food item============")
            self.edit_user_name()
        elif choice == 4:
            print("==============remove food item=========")
            self.remove_user_name()
        else:
            print("Invalid Choice")
        self.userRootFunction()

    def userRootFunction(self):
           while True:
            print("Enter \n1.add_user_item \n2.view_user_item \n3.edit_user_item \n4.remove_user_item \n5.Back to the Menu \n6.Back to the Main Menu")
            choice = int(input("Enter your choice : "))
            if choice == 5:
                return 1
            elif choice == 6:
                return 0
            else:
                self.execute(choice)