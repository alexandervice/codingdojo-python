class BankAccount:
    default_int_rate = 0.02
    default_balance = 0
    all_accounts = []
    def __init__(self, int_rate=None, balance=None): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        if int_rate == None:
            self.int_rate = BankAccount.default_int_rate
        else:
            if int_rate > 0 and int_rate< 1:
                self.int_rate = int_rate
            else:
                print("Error: Interest Rate Invalid. Setting default interest rate of 2%")
                self.int_rate = BankAccount.default_int_rate
        if balance == None:
            self.balance = BankAccount.default_balance
        else:
            if balance > 0:
                self.balance = balance
            else:
                print("Error: Invalid Balance. Setting default balance as $500")
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        print(f"New Balance: {self.balance}")
        return self
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"New Balance: {self.balance}")
        else:
            print(f"Warning {amount} is larger than total balance of {self.balance}. You will be fined a $5 fee for your mistake.")
            self.balance -= 5
            print(f"New Balance: {self.balance}")
        return self
    def display_account_info(self):
        print(f"Your account balance is: {self.balance}")
        print(f"Your interest rate is {self.int_rate}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.int_rate
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

batman = BankAccount(0.08,10000)

batman.deposit(5000).deposit(2550).deposit(7550).withdraw(20000).yield_interest().display_account_info()


superman = BankAccount()
superman.deposit(350).deposit(700).withdraw(400).withdraw(35).withdraw(150).withdraw(300).yield_interest().display_account_info()

BankAccount.all_balances()

# print(batman.int_rate)