# Food ordering App Python Project Edyoda
# Restaurant name ShrisKitchen

# 0. Creating class on Restaurant name
class ShrisKitchen:
    def __init__(self, name):
        self.admin_password = None
        self.admin_name = None
        self.shris_kitchen_name = name
        self.food_menu = {}
        self.food_menu_ID = len(self.food_menu) + 1
        self.admin_details = {}
        self.user_details = {}
        self.ordered_food_item = []

                                     # Admin Functionalities

    # 1. Admin register function
    def admin_register(self):
        try:
            self.admin_name = input("Enter your User Name : ")
            self.admin_password = input("Enter your Password: ")
            self.admin_details = {"User Name": self.admin_name, "Password": self.admin_password}
            print("\n!! ADMIN ACCOUNT REGISTERED SUCCESSFULLY !!\n")
            print("ADMIN REGISTERED DETAILS: ")
            for i in self.admin_details:
                print(i, ":", self.admin_details[i])
        except Exception as e:
            print(e)
            print("\n!! ADMIN REGISTER CREDENTIALS FAILED")

    # 2. Admin login function
    def admin_login(self):
        try:
            print(f"WELCOME TO {self.shris_kitchen_name} VEG RESTAURANT\n\n")
            name = input("Enter Your Registered Name : ")
            password = input("Enter Your Password : ")
            if len(self.admin_details.values()) != 0:
                if name == self.admin_name and password == self.admin_password:
                    print("\n!! LOGIN SUCCESSFUL !!!WELCOME!!! !!\n")
                # 3. Admin Functionalities calling via while loop
                while True:
                    print("\nEnter the Below Options\n")
                    print("\t1. ADD FOOD ITEM \n\t2. EDIT FOOD ITEM\n\t3. VIEW FOOD ITEM\n\t4. REMOVE FOOD ITEM\n\t5. "
                          "GO BACK")
                    z = input()
                    if z == "1":
                        self.add_food_item()
                    elif z == "2":
                        self.edit_food_item()
                    elif z == "3":
                        self.view_food_item()
                    elif z == "4":
                        self.remove_food_item()
                    elif z == "5":
                        break
                    else:
                        print("NOT A VALID OPTION ")
                else:
                    print("\n!! INCORRECT ADMIN DETAILS !!\n")
            else:
                print("\n!! ADMIN ACCOUNT DOES NOT EXIST !!\n")
        except Exception as e:
            print(e)
            print("\n!! ADMIN LOGIN CREDENTIALS FAILED !!")

    # 4. Add Food Items function only admin can add food items function call
    def add_food_item(self):
        try:
            name = input("Enter the food name : ")
            quantity = float(input("Enter the quantity in values only, for pieces,gram and ml  : "))
            price = float(input("Enter the price in 'INR' only : "))
            discount = float(input("Enter the discount in 'INR' only : "))
            stock = float(input("Enter the available stock in values, 'Count' only : "))
            food_item = {"Name": name, "Quantity": quantity, "Price": price, "Discount": discount, "Stock": stock}
            self.food_menu_ID = len(self.food_menu) + 1
            self.food_menu[self.food_menu_ID] = food_item
            print("\n!! FOOD ITEM ADDED SUCCESSFULLY !!\n")
            print("UPDATED FOOD ITEMS :", self.food_menu, "\n")
        except Exception as e:
            print(e)
            print("\n!! ADDING NEW FOOD ITEM FAILED !!\n")

    # 5. Edit food items function call
    def edit_food_item(self):
        try:
            x = int(input("Enter the Food ID you want to update : \n"))
            if x in self.food_menu.keys():
                print(
                    "\t1. UPDATE FOOD NAME\n\t2. UPDATE QUANTITY\n\t3. UPDATE PRICE\n\t4. UPDATE DISCOUNT\n\t5. "
                    "UPDATE STOCK\n")
                y = input("Enter the Number Only : ")
                if y == "1":
                    self.food_menu[x]["Name"] = input("Updated Food name : ")
                    print("\n!! Food Name Successfully Updated !!\n")
                elif y == "2":
                    self.food_menu[x]["Quantity"] = float(input("Updated Quantity in values only : "))
                    print("\n!! Quantity Successfully Updated !!\n")
                elif y == "3":
                    self.food_menu[x]["Price"] = float(input("Updated Price in 'INR' only : "))
                    print("\n!! Price Successfully Updated !!\n")
                elif y == "4":
                    self.food_menu[x]["Discount"] = float(input("Updated Discount in 'INR' only : "))
                    print("\n!! Discount Successfully Updated !!\n")
                elif y == "5":
                    self.food_menu[x]["Stock"] = float(input("Updated Stock in values only : "))
                    print("\n!! Stock Successfully Updated !!\n")
                else:
                    print("!! NOT A VALID OPTION !!\n")
            else:
                print("\n!! INCORRECT FOOD ID !!\n")
        except Exception as e:
            print(e)
            print("\n!! ERROR IN EDITING THE FOOD ITEMS NOT ACCESSING !!\n")

    # 6. View the list of all food added function call
    def view_food_item(self):
        print("LIST OF FOOD ITEMS IN ShrisKitchen: \n")
        if len(self.food_menu) != 0:
            for i in self.food_menu:
                print(f"Food Id : {i}")
                for j in self.food_menu[i]:
                    print(j, ":", self.food_menu[i][j])
                print()
        else:
            print("!! FOOD ITEMS ARE NOT AVAILABLE RIGHT NOW !!\n")

    # 7. remove the food item based on food ID function call
    def remove_food_item(self):
        try:
            print("!! WARNING !!\nFOOD ITEM WILL DELETE PERMANENTLY\n")
            print("Enter the Food ID ")
            x = int(input())
            if x in self.food_menu.keys():
                del self.food_menu[x]
                print("\n!! FOOD ITEM DELETED SUCCESSFULLY !!\n")
                print("UPDATED FOOD ITEM LIST :\n", self.food_menu)
            else:
                print("!! INCORRECT FOOD ID!!\n")
        except Exception as e:
            print(e)
            print("\n!! ERROR IN REMOVING FOOD ITEMS KINDLY PROVIDE VALID CREDENTIALS !!\n")

                                            # User Functionalities

    # 1. User register or Create account function call
    def user_register(self):
        try:
            user_name = input("Enter your FUll Name : ")
            phone_no = int(input("Enter your 10 digit Phone number : "))
            email = input("Enter your Email id : ")
            password = input("Enter your Password : ")
            address = input("Enter your Address with area PIN code ")
            self.user_details = {"User Name": user_name, "Phone No.": phone_no, "Email_ID": email, "Password": password,
                                 "Address": address}
            print("\n!! ACCOUNT CREATED SUCCESSFULLY !!\n")
            print("USER DETAILS : ")
            for i in self.user_details:
                print(i, ":", self.user_details[i])
        except Exception as e:
            print(e)
            print("\n!! USER REGISTER CREDENTIALS FAILED  !!\n ")

    # 2. User login credential function call
    def user_login(self):
        try:
            print(f"WELCOME TO {self.shris_kitchen_name} VEG RESTAURANT\n\n")
            user_name = input("Enter Your User Name : ")
            password = input("Enter Your Password : ")
            if len(self.user_details.values()) != 0:
                if user_name == self.user_details["User Name"] and password == self.user_details["Password"]:
                    print("\n!! LOGIN  CREDENTIALS SUCCESSFUL !!")
                    while True:
                        print("\nEnter the Below Options\n")
                        print("\t1. PLACE NEW ORDER\n\t2. ORDER HISTORY\n\t3. UPDATE PROFILE\n\t4. GO BACK")
                        z = input()
                        if z == "1":
                            self.place_new_order()
                        elif z == "2":
                            self.ordered_history()
                        elif z == "3":
                            self.update_profile()
                        elif z == "4":
                            break
                        else:
                            print("NOT A VALID OPTION")
                else:
                    print("\n!! INCORRECT USER DETAILS!!\n")
            else:
                print("\n! USER ACCOUNT NOT EXIST\n")
        except Exception as e:
            print(e)
            print("\n!! USER LOGIN CREDENTIALS FAILED !!")

    # 3. placing new order from user function call
    def place_new_order(self):
        try:
            if len(self.food_menu) != 0:
                print("LIST OF AVAILABLE FOOD ITEMS :\n")
                menu = []
                for items in self.food_menu:
                    menu.append([self.food_menu[items]["Name"], self.food_menu[items]["Quantity"],
                                 self.food_menu[items]["Price"]])
                for i in range(len(menu)):
                    print(i + 1, ".", menu[i])
                while True:
                    print("\n\t1. CONTINUE ORDER\n\t2. GO BACK\n")
                    x = input()
                    if x == "1":
                        print("Enter the Food number You want to ordered separated by comma")
                        y = input().split(",")
                        for i in y:
                            z = int(i)
                            if z <= len(menu):
                                self.ordered_food_item.append(menu[z - 1])
                            else:
                                print("\nFOOD ITEM NOT AVAILABLE  : ", z)
                        print("\nLIST OF FOOD ITEMS SELECTED : \n")
                        for j in self.ordered_food_item:
                            print(j)
                    elif x == "2":
                        break
                    else:
                        print("!! NOT A VALID OPTION !!\n")
            else:
                print("\n!! FOOD ITEMS ARE NOT AVAILABLE !!\n")
        except Exception as e:
            print(e)
            print("\n!! PLACING NEW ORDER FAILED !!")

    # 4. Order history function call
    def ordered_history(self):
        if len(self.ordered_food_item) != 0:
            print("\nLIST OF PREVIOUS ORDERED FOOD ITEMS : \n")
            for i in self.ordered_food_item:
                print(i)
        else:
            print("\n!! ORDER HISTORY NOT AVAILABLE !!")

    # 5. Update user registered credential function call
    def update_profile(self):
        try:
            for i in self.user_details:
                print(i, ":", self.user_details[i])
            while True:
                print("Select Below Options to Update Your Profile Details\n")
                print(
                    "\t1. UPDATE NAME\n\t2. UPDATE PHONE NO\n\t3. UPDATE EMAIL ID\n\t4. UPDATE PASSWORD\n\t5. UPDATE "
                    "ADDRESS\n\t6. GO BACK\n")
                x = input()
                if x == "1":
                    self.user_details["User Name"] = input("Enter your updated full name : ")
                    print("\n!! Name Successfully Updated !!\n")
                elif x == "2":
                    self.user_details["Phone No."] = int(input("Enter your updated 10 digit phone number : "))
                    print("\n!! Phone No Successfully Updated !!\n")
                elif x == "3":
                    self.user_details["Email_ID"] = input("Enter your updated email id : ")
                    print("\n!! Email ID Successfully Updated!!")

                elif x == "4":
                    self.user_details["Password"] = input("Enter your updated password : ")
                    print("\n!! Password Successfully Updated !!\n")

                elif x == "5":
                    self.user_details["Address"] = input("Enter your updated address with area PIN code ")
                    print("\n!! Address Updated Successfully Updated!!\n")

                elif x == "6":
                    break
                else:
                    print("\n!! NOT A VALID OPTION !!\n")

                if x in ["1", "2", "3", '4', "5"]:
                    for i in self.user_details:
                        print(i, ":", self.user_details[i])
                else:
                    pass
        except Exception as e:
            print(e)
            print("\n!! UPDATE PROFILE INPUT CREDENTIAL ERROR !!\n ")
