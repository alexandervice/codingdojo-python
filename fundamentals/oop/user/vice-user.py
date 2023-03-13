class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        # defaults
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(f"First name is : {self.first_name}")
        print(f"Last name is: {self.last_name}")
        print(f"{self.first_name}'s email is {self.email}")
        print(f"{self.first_name} is {self.age} years old")
        print(f"Rewards member status = {self.is_rewards_member}")
        print(f"{self.first_name} has {self.gold_card_points} gold card points")
        print("")
    
    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print(f"Error - {self.first_name} is already a rewards member")

    def spend_points(self, ammount):
        if self.gold_card_points >= ammount:
            self.gold_card_points = self.gold_card_points - ammount
            print(f"{self.first_name}'s remaining Gold Card Points = {self.gold_card_points}")
        else:
            print(f"Error - {self.first_name} has insufficient Gold Card Points for this purchase. Ballance = {self.gold_card_points}")


superman = User("Clark", "Kent", "ckent@dailyplanet.com", 39)
batman = User("Bruce", "Wayne", "bwayne@wayneenterprises.com", 38)
alex = User("Alexander", "Vice", "alexdvice@gmail.com", 29)
# alex.display_info()
# print("")
# alex.enroll()
# alex.display_info()

superman.spend_points(50)
batman.enroll()
batman.spend_points(80)

superman.display_info()
batman.display_info()
alex.display_info()

batman.enroll()