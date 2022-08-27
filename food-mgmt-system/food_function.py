from entity.food import Food

class FoodFunction:

    foodlist = []

    def add_food_item(self):
        food_id = int(input("Enter Food Id : "))
        food_item = input("Enter the Food Item:  ")
        food_quantity = int(input("Enter the food_quantity: "))
        food_price = int(input("Enter the food_price: "))
        food_discount = int(input("Enter the food_discunt: "))
        food_stock_left = int(input("Enter the food stock left: "))
        food_obj = Food(food_id,food_item,food_quantity,food_price,food_discount,food_stock_left)
        self.foodlist.append(food_obj)
        print("Food successfully ordered!")

    def view_food_item(self):
        for i in self.foodlist:
            print()
            print(i)

    def search_food_id(self):
        food_id = int(input("Enter the food id: "))
        for foods in self.foodlist:
            if foods.food_id == food_id:
                print(foods)
                break
        else:
            print("Food not found")

    def search_food_item(self):
        food_item = input("Enter item of the food : ")
        for foods in self.foodlist:
            if foods.food_item == food_item:
                print(foods)
                break
        else:
            print("food not found!")

    def edit_food_item(self):
        edit_food_item = input("Enter the edit food item: ")
        for food in self.foodlist:
             if food.food_item == edit_food_item:
                 food_item = input("Enter the Food Item:  ")
                 food_quantity = int(input("Enter the food_quantity: "))
                 food_price = int(input("Enter the food_price: "))
                 food_discount = int(input("Enter the food_discunt: "))
                 food_stock_left = int(input("Enter the food stock left: "))

                 food.set_food_item(food_item)
                 food.set_food_quantity(food_quantity)
                 food.set_food_price(food_price)
                 food.set_food_quantity(food_quantity)
                 food.set_food_discount(food_discount)
                 food.set_food_stock_left(food_stock_left)
                 print("succesfully edited food")
                 break
        print("food item not found!")


    def remove_food_item(self):
        food_id = int(input("Enter Food Id of the food you want to delete: "))
        for foods in self.foodlist:
            if foods.food_id == food_id:
                self.foodlist.remove(foods)
                print("Successfully Deleted Food")
                break
        else:
            print("No food Found!")

    def execute(self, choice):
        if choice == 1:
            print("==============add_food_item===========")
            self.add_food_item()
        elif choice == 2:
            print("==============view food item=========")
            self.view_food_item()
        elif choice == 3:
            print("===============search_food_id==============")
            self.search_food_id()
        elif choice == 4:
            print("==============search_food_item============")
            self.search_food_item()
        elif choice == 5:
            print("==============edit food item============")
            self.edit_food_item()
        elif choice == 6:
            print("==============remove food item=========")
            self.remove_food_item()
        else:
            print("Invalid Choice")
        self.foodRootFunction()

    def foodRootFunction(self):
        print("=======================================")
        print("Choose option food main menu: \n1.add_food_item \n2.view_food_item \n3.search_food_id \n4.search_food_item \n5.edit_food_item \n6.remove food item \n7.Back to menu \n8.Main menu \n")
        choice = int(input("Enter your choice : "))
        if choice == 7:
            return 1
        elif choice == 8:
            return 0
        else:
            self.execute(choice)

   

   
