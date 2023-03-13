# NOTE This code is not DRY... the extra challenges were tough for me to add while also keeping things nice and DRY

class BankAccount:
    all_accounts = []
    def __init__(self, int_rate=0.02, balance=0): 
        if int_rate > 0 and int_rate< 1:
            self.int_rate = int_rate
        else:
            print("Error: Interest Rate Invalid. Setting default interest rate of 2%")
            self.int_rate = 0.02
        if balance >= 0:
            self.balance = balance
        else:
            print("Error: Invalid Balance. Setting default balance as $0")
            self.balance = 0
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        print("Deposit Successful")
        return self
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
            print("Withdraw successful")
        else:
            print(f"Warning {amount} is larger than total balance of {self.balance}. You will be fined a $5 fee for your mistake.")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Your account balance is: {self.balance}")
        print(f"Your interest rate is {self.int_rate}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.int_rate
            print("Interest applied")
        else:
            print("Error: Unable to recieve interest payment")
        return self
    
    @classmethod
    def all_balances(cls):
        sum = 0
        userNum = 0
        for i in cls.all_accounts:
            sum += i.balance
            userNum += 1
            print(f"User {userNum} has a balance of {i.balance} and interest rate of {i.int_rate}")
        print(f"The Bank has a total balance for all users of ${sum}")
        
        return sum
    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

class User:
    bank_accounts = {} # I realize now I could have added the account name within the BankAccount class... oh well, it probably would have been easier, but this works for now.

    def __init__(self, name, email, int_rate=0.02, balance=0, account_name="Main"):
        self.name = name
        self.email = email
        self.int_rate = int_rate
        self.balance = balance
        User.bank_accounts[(name,account_name)] = (BankAccount(int_rate, balance))
        # User.find_account_balance(name)
        print(f"{name} has successfully created an account called {account_name} with a balance of ${balance}")
        
    # other methods
    
    def make_deposit(self, amount, account_name="Main"):
        # self.account.deposit(amount)
        User.bank_accounts[(self.name,account_name)].deposit(amount)
        # print(f"{self.name}'s New Balance: {self.account.balance}")
        return self
    def make_withdraw(self,amount, account_name="Main"):
        User.bank_accounts[(self.name,account_name)].withdraw(amount)
        # print(f"{self.name}'s New Balance: {self.account.balance}")
        return self
    def display_user_balance(self):
        for accounts, money in User.bank_accounts.items():
            if accounts[0] == self.name:
                print(f"{accounts[0]} has ${money.balance} in Account: {accounts[1]}")
        return self
    def user_yield_interest(self, account_name="Main"):
        User.bank_accounts[(self.name,account_name)].yield_interest()
        return self
    def create_new_account(self, account_name, int_rate=None, balance=None):
        for account in User.bank_accounts.keys():
            if account[1] == account_name:
                print(f"Error Account Name: {account_name} already exists")
            else:
                print(f"New Account: {account_name} opened for {self.name}")
        User.bank_accounts[(self.name,account_name)] = (BankAccount(int_rate, balance))
        return self
    def transfer_money(self, amount, other_user, account_name="Main"):
        for accounts, money in User.bank_accounts.items():
            if accounts[0] == other_user:
                for accounts2, money2 in User.bank_accounts.items():
                    if accounts2[0] == self.name and accounts2[1] == account_name:
                        if amount <= money2.balance:
                            money2.balance -= amount
                            money.balance += amount
                            print(f"Transfer successful")
                            return self
                        else:
                            print(f"Warning {amount} is larger than total balance of {money2.balance} in {accounts2[1]}. You will be fined a $5 fee for your mistake.")
                            money2.balance -= 5
                            return self
                print(f"Error: Account Name: {account_name} not found in your accounts")
                return
        print(f"Error User: {other_user} not found")
        return
    @staticmethod
    def find_account_balance(user,account_name="Main"):
            for accounts, money in User.bank_accounts.items():
                if accounts[0] == user and accounts[1] == account_name:
                    return money.balance
            print("Error: Account not found")
            return


bruce = User("Bruce Wayne", "bwayne@wayneenterprise.com",0.08,10000)

bruce.make_deposit(4000).make_withdraw(11000).display_user_balance().user_yield_interest().display_user_balance()

bruce.create_new_account("Batman Funds", 0.04, 50000).make_deposit(100000,"Batman Funds").display_user_balance()

clark = User("Clark Kent", "ckent@dailyplanet.com")

bruce.transfer_money(50000,"Clark Kent","Batman Funds").display_user_balance()
clark.display_user_balance()

# clark.transfer_money(1000000, "Lois")
# clark.transfer_money(1000000, "Bruce Wayne")