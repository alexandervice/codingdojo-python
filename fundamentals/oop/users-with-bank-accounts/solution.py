class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}

    def open_new_account(self, int_rate=0.02, balance=0, account_name="checking"):
        # Make a bank account instance
        new_account = BankAccount(int_rate, balance)
        
        # add that instance to the accounts dictionary
        self.accounts[account_name] = new_account

        return self

    # Add a make_deposit method to the User class 
    # that calls on it's bank account's instance methods.
    def make_deposit(self, amount, account_name="checking"):
        self.accounts[account_name].deposit(amount)
        return self

    # Add a make_withdrawal method to the User class 
    # that calls on it's bank account's instance methods.
    def make_withdrawal(self, amount, account_name="checking"):
        self.accounts[account_name].withdraw(amount)
        return self


    # Add a display_user_balance method to the User class 
    # that displays user's account balance
    def display_user_balance(self):

        display_string = ""

        # show all account balances (Note: Uses key, val loop over dict)
        print(f"{self.name}'s Accounts:")
        for account_name, account in self.accounts.items():
            display_string += f"{account_name}: {account.balance} "
        print(display_string)
        print("-"*15)

        return self

    def transfer_money(self, other_person, from_account, amount, to_account):

        # NOTE: other_person should be a USER object (not BankAccount - mistake in the video)

        # Tell user you're attempting to deposit to the other person's account.
        print(f"\nTransferring ${amount} from {self.name}'s {from_account} to {other_person.name}'s {to_account}")

        # check if user has enough funds
        if self.accounts[from_account].balance < amount:
            print("Insufficient funds")
            return self
        
        # Withdraw from user's account
        self.make_withdrawal(amount, from_account)

        # Deposit into other user's account
        other_person.make_deposit(amount, to_account)

        return self


class BankAccount:
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self


# # User test
# user1 = User("Sadie", "s@s.com")
# user1.make_deposit(100).make_deposit(250).display_user_balance()

# user2 = User("William", "w@w.com")
# user2.make_deposit(1000).display_user_balance().make_withdrawal(450).display_user_balance()

# Sensei Bonus test
sadie = User("Sadie Sink", "s@s.com")
sadie.open_new_account(0.05, 0)
sadie.make_deposit(100)
sadie.open_new_account(0, 500, "savings").display_user_balance()

sami = User("Samantha Bee", "sb@sb.com")
sami.open_new_account(0.045, 300, "savings").display_user_balance()

# SENPAI BONUS TESTS
print("\n"+"*"*30) # prints a line of stars
print("Making Transfers\n")

sadie.transfer_money(sadie, "checking", 50, "savings").display_user_balance()
sadie.transfer_money(sami, "savings", 100, "savings").display_user_balance()
sami.display_user_balance()
sami.transfer_money(sadie, "savings", 1000, "checking") # should be insufficient.
