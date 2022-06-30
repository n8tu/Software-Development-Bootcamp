from bankAccount import BankAccount

class User:
    def __init__(self,name):
        self.name = name
        self.account = {"Funding Account":BankAccount(0.01,0)}

    def make_deposit(self,amount,bank_account_name = "Funding Account"):
        self.account[bank_account_name].deposit(amount)
        return self
    
    def make_withdrawal(self,amount, bank_account_name = "Funding Account"):
        self.account[bank_account_name].withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"Name: {self.name}\nBalance:")
        for key in self.account:
            print(key, "=>" ,self.account[key].balance)

        return self
    
    def open_bank_account(self,account_name,int_rate,balance = 0):
        self.account[account_name] = BankAccount(int_rate,balance)
        print(f"congratulations you just opend an account with '{account_name}' name.")
        return self




user1 = User("Faisal")
user1.display_user_balance()
user1.open_bank_account("Saving Account",0.05,5000).make_deposit(400,"Saving Account").display_user_balance()
user1.open_bank_account("Funding2 Account",0.01).make_deposit(200,"Funding2 Account").display_user_balance()