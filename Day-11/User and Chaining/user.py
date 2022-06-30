class User:
    def __init__(self,name,balance = 0):
        self.name = name
        self.balance = balance


    def make_deposit(self,amount):
        self.balance += amount
        print(f"You have deposit {amount} successfully")
        return self
    
    def make_withdrawal(self, amount):
        if(self.balance < amount):
            print(f"Sorry {self.name}, You don't have enough money.")
        else:
            self.balance -= amount
            print(f"You have withdrawal {amount} successfully")
        return self

    def display_user_balance(self):
        print(f"Name: {self.name}\nBalance: {self.balance}\n")
        return self

    def transfer_money(self, other_user, amount):
        if(self.balance < amount):
            print(f"Sorry {self.name}, You don't have enough money.")
        else:
            self.balance -= amount
            other_user.balance += amount
            print(f"Your transfer has been made successfully\n")
            print(f"From: {self.name}\nTo: {other_user.name}\nAmount: {amount} \n")
        
        return self

    




faisal = User('Faisal',1000)
abdulrhman = User('Abdulrhman',10000)
anas = User('anas',150000)

faisal.display_user_balance()
anas.display_user_balance().transfer_money(faisal,50000).display_user_balance()
faisal.display_user_balance()