class User:
    def __init__(self, name):
        self.name = name
        self.expanse_list = []
        self.income_list = []

    def __str__(self):
        return f"Welcome {self.name}! Your total income is: {self.income_list}. Your total expanse is: {self.expanse_list}"

    def get_income_list(self):
        return self.income_list

    def get_expanse_list(self):
        return self.expanse_list

    def add_income(self, income):
        self.income_list.append(income)

    def add_expanse(self, expanse):
        self.expanse_list.append(expanse)

    def total_income(self):
        total = 0
        for income in self.income_list:
            total += income.amount
        return total

    def total_expanse(self):
        total = 0
        for expanse in self.expanse_list:
            total += expanse.amount
        return total

    def calculate_balance(self):
        return self.total_income() - self.total_expanse()

    def expanse_by_category(self):
        expanse_categories = {}
        for expanse in self.expanse_list:
            if expanse.category in expanse_categories.keys():
                expanse_categories[expanse.category] += expanse.amount
            else:
                expanse_categories[expanse.category] = expanse.amount
        return expanse_categories

class Income:
    def __init__(self, month, amount):
        self.month = month
        self.amount = amount

    def __str__(self):
        return f"{self.amount} euro in {self.month}"


class Expanse:
    def __init__(self, month, amount, category):
        self.month = month
        self.amount = amount
        self.category = category

    def __str__(self):
        return f"{self.amount} euro in {self.month}"


user1 = User("Reka")
valid_categories = ["Bills", "Food", "Transportation", "Clothing", "Hobby", "Travel", "Home"]
valid_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
while True:
    month = ""
    while month not in valid_months:
        month = input("January February March April May June July August September October November December \nChoose a month: ")
        if month not in valid_months:
            print("Invalid month. Please enter month again: ")

    transaction = input("1.Add income \n2.Add expanse \n3.Get statement \n")
    if transaction == "1":
        value = int(input("Enter the value: "))
        income1 = Income(month, value)
        user1.add_income(income1)
        print(f"Your income in {month} is {user1.total_income()} euro")

    if transaction == "2":
        value = int(input("Enter the value: "))
        category = ""
        while category not in valid_categories:
            category = input(("\nBills \nFood \nTransportation \nClothing \nHobby \nTravel \nHome \nChoose the category: "))
            if category not in valid_categories:
                print("Invalid category. Please enter the category again: ")
        expanse1 = Expanse(month, value, category)
        user1.add_expanse(expanse1)
        print(f"Your total expanse in {month} is {user1.total_expanse()} euro")

    if transaction == "3":
        print(f"In {month} you had: \nTotal income: {user1.total_income()} \nTotal expanse: {user1.total_expanse()} \nBalance: {user1.calculate_balance()}")
        expanse_by_categories1 = user1.expanse_by_category()
        print(f"Expanse by categories: ")
        for category in expanse_by_categories1:
            print(f"\n{category} : {round(expanse_by_categories1[category] * 100 / user1.total_expanse())} %")