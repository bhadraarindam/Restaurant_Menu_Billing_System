class RestaurantFoodOrderBillingSystem:
    def __init__(self):

        # Calculation stuff
        self.food_price = 0
        self.username = "admin"
        self.password = "admin"
        self.cgst = 0.025
        self.sgst = 0.025

        self.items = {
            "Chicken Curry": 170,
            "Mutton Kasha": 350,
            "Butter Naan": 50,
            "Jira Rice": 140
        }
        self.list = list(self.items.keys())
        print("MENU")
        i = 1
        for x in self.list:
            print(f'{i}. {x} (₹{self.items[x]})')
            i += 1
        self.itemNo = int(input("Enter your item : "))
        self.item_types = []
        self.item_types.append(self.itemNo)

    def add_item(self):
        self.list = list(self.items.keys())
        print("MENU")
        i = 1
        for x in self.list:
            print(f'{i}. {x} (₹{self.items[x]})')
            i += 1
        self.itemNo = int(input("Enter your item : "))
        self.item_types.append(self.itemNo)

    def admin_add_product(self):
        while True:
            uname = input("Username : ")
            pswd = input("Password : ")

            if uname == self.username and pswd == self.password:
                product_name = input("Enter a product name : ")
                product_price = int(input("Enter a product price : "))
                self.items[product_name] = product_price
                break
            else:
                print("Wrong username or password")

    def calculate_price(self):

        for x in self.item_types:
            self.food_price += self.items[self.list[x-1]]

        cgst_amount = round(self.food_price*self.cgst, 2)
        sgst_amount = round(self.food_price*self.sgst, 2)
        total = self.food_price + cgst_amount + sgst_amount

        def find_quantity_of_each_element(li):
            output = {}
            sli = list(set(li))
            for x in sli:
                output[x] = li.count(x)
            return output

        print("YOUR BILL")
        print("Your Total (₹) :", self.food_price)
        print("CGST (₹) :", cgst_amount)
        print("SGST (₹) :", sgst_amount)
        print("-"*17)
        print("TOTAL (₹) :", round(total, 2))
        print()
        print()
        print("BILL DETAILS")
        print("--------------")
        output_items = find_quantity_of_each_element(self.item_types)
        item_keys = list(output_items.keys())
        for x in item_keys:
            print(
                f'{self.list[x-1]} (QTY - {output_items[x]}) : ₹{self.items[self.list[x-1]]*output_items[x]}')
