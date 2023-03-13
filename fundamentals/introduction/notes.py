# print("Hello World!")

# x= "Hello Python"
# print(x)
# y = 42
# print(y)

# name = "Alex"
# age = 29

# print("My name is", name)
# print("my age is", age)

# print("My name is " + name)
# print("my age is " + str(age))
# 
# print(f"My name is {name} and I am {age} years old.")
# f-string lets us do this

# print("My name is {} and I am {} years old.".format(name, age))


# fruits = ['apple', 'banana', 'orange', 'strawberry']
# vegetables = ['lettuce', 'cucumber', 'carrots']
# fruits_and_vegetables = fruits + vegetables
# print(fruits_and_vegetables)
# salad = 3 * vegetables
# print(salad)


# favPokemon = ["Corviknight", "Aggron", "Carkoal", "Baxcalibur"]
# print(favPokemon)
# favPokemon.append("Appleton")
# print(favPokemon)
# print(favPokemon[1:3])
# listcopy = favPokemon
# listcopy.pop(2)
# print(listcopy)

# numbers = [2,4,6,8,7,6,5,4,3]
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(sorted(numbers))
# print(numbers.index(6)) #only prints the first time 6 shows up

# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers.pop(2)
# numbers.pop(4)
# print(numbers)
# numbers.append(1)
# print(numbers)

# pokeStats = ("HP", "Atk", "Def", "Sp Atk", "Sp Def", "Spd") # tuples cannot be changed denoted by parenthesis ()

# for i in range(6):
#     print(pokeStats[i])

# nums = [1,2,3,4,5,6,7,8,9,10]

# for i in range(10): #tenth item does not get printed, always increase number by 1
#     print(i)

# for i in range(0,11,2):
#     print(i)
#     if i == 10:
#         print("done")
#     elif i > 5:
#         print("whoa big one")
#     else:
#         print("tiny boy")

# testList = [0,2,4,6,8,10,1,3,5,7,9]

# for i in range(0,len(testList)):
#     print(i, ":", testList[i])

# for j in testList:
#     print(j)
    # print(j, ":", testList[j])

# for count in range(0,5):
#     print("looping=", count)

# for i in range(0,5):
#     print("looping=", i)

# count = 0
# while count <= 5:
#     print("looping:",count)
#     count += 1
# else:
#     print("all done") # this only prints once


# for num in [0,1,2,3,4,5]:
#     if num == 2:
#         continue # skips this one
#     elif num == 4:
#         break #ends the loop
#     print(num)


# def add(a,b):	# function name: 'add', parameters: a and b
#     x = a + b	# process
#     return x	# return value: x

# # define parameters and pass arguments 
# # a and b are parameters

# # set defaults when declaring the parameters
# def be_cheerful(name='', repeat=2):
# 	print(f"good morning {name}\n" * repeat)
# be_cheerful()   # output: good morning (repeated on 2 lines)
# be_cheerful("tim")  # output: good morning tim (repeated on 2 lines)
# be_cheerful(name="john")    # output: good morning john (repeated on 2 lines)
# be_cheerful(repeat=6)   # output: good morning (repeated on 6 lines)
# be_cheerful(name="michael", repeat=5)   # output: good morning michael (repeated on 5 lines)
# # NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
# be_cheerful(repeat=3, name="kb")    # output: good morning kb (repeated on 3 lines)

# def multiply(num_list, num):
#     for x in range(len(num_list)):
#         num_list[x] *= num
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)

# #  dictionaries

# pokemon = {
#     "mon1": "bulbasaur",
#     "mon2": "ivysaur",
#     "mon3": "venusaur"
# }

# print(pokemon)
# print(pokemon["mon2"])

# pokemon["mon4"] = "charmander"

# print(pokemon)

# if "mon5" not in pokemon:
#     pokemon["mon5"] = "charmeleon"

# print(pokemon)

# if "mon5" not in pokemon:
#     pokemon["mon5"] = "misingno"
# else:
#     print("would you like to update the 5th pokemon?")

# print(pokemon["mon5"])

# poke_five = pokemon.pop("mon5")     # remove value but store it AKA return it
# print(pokemon)
# print(poke_five)

# del pokemon["mon2"]     # just straight up delete that one
# print(pokemon)

# poke_six = pokemon.get("mon6", "mon does not exist") # tells you what the value is, second thing is what comes up if the value does not exist
# print(poke_six)

# newpokemon = {"mon150": "mewtwo", "mon151": "mew", "mon1": "BULBASUAR"} 

# pokemon.update(newpokemon) # adds and updates new key value pairs

# print(pokemon, len(pokemon)) # can get how many key value pairs there are

# pokemon.clear() # completely removes the whole thing

# print(pokemon)

# capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# # another way to iterate through the keys
# for key in capitals.keys():
#     print(key)
# # output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
# #to iterate through the values
# for val in capitals.values():
#     print(val)
# # output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
# #to iterate through both keys and values
# for key, val in capitals.items():
#     print(key, " = ", val)
# # output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

# my_dict = { "name": "Noelle", "language": "Python" }
# for each_key in my_dict:
#     print(each_key)
#     print(my_dict[each_key])
# # output: Noelle, Python

# List of dictionaries
# users = [
#     {"first": "Ada", "last": "Lovelace"}, # index 0
#     {"first": "Alan", "last": "Turing"}, # index 1
#     {"first": "Eric", "last": "Idle"} # index 2
# ]
# # Dictionary of lists
# resume_data = {
#     #        	     0           1           2
#     "skills": ["front-end", "back-end", "database"],
#     #                0           1
#     "languages": ["Python", "JavaScript"],
#     #                0              1
#     "hobbies":["rock climbing", "knitting"]
# }

# print(users[0]["last"]) # prints Lovelace


#  NOTE - Classes and OOP - NOTE

# class User: # capitalize this
#     # constructor function -- creates the instance of an object
#     def __init__(self): # always use __init__
#         self.first_name = "Ada"
#         self.last_name = "Lovelace"
#         self.age = 42

# user_ada = User() #sets ada as a user
# print(user_ada.first_name)

# user_2 = User()
# print(user_2.first_name)

# class Shoe:
#     def __init__(self, brand, shoe_type, price):
#         # now assign them
#         self.brand = brand
#         self.type = shoe_type
#         self.price = price
#         # these will get applied by default
#         self.in_stock = True
    
#     def sale_percent(self, percent):
#         self.price = self.price*(1-percent)


# skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
# dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
# bball_shoe = Shoe("Nike", "Basketball", 89.99)

# # #  make skater shoe go on sale of 20%
# # skater_shoe.price = skater_shoe.price*(1-0.2)
# # # make dress shoes go on sale by 10%
# # dress_shoe.price = dress_shoe.price*(1-0.1)
# # # make skate shoe go on sale AGAIN by 10%
# # skater_shoe.price = skater_shoe.price*(1-0.1)
# # #  very very redundant
# skater_shoe.sale_percent(.2)
# print(skater_shoe.price)

# print(dress_shoe.price)
# dress_shoe.sale_percent(.5)
# print(dress_shoe.price)


# print(skater_shoe.brand)
# print(dress_shoe.type)
# print(bball_shoe.price)

# class User:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     def greeting(self):
#         print(f"Hello my name is {self.first_name} {self.last_name} and I am {self.age} years old!")

# alex = User("Alex", "Vice", 29)

# alex.greeting()

# class BankAccount:
#     # class attributes
#     bank_name = "First National Dojo"
#     # new class attribute - a list of all the accounts!
#     all_accounts = []
    
#     def __init__(self, int_rate,balance):
#         self.int_rate = int_rate
#         self.balance = balance
#         BankAccount.all_accounts.append(self)
    
#     def with_draw(self,amount):
#         # we can use the static method here to evaluate
#         # if we can with draw the funds without going negative
#         if BankAccount.can_withdraw(self.balance,amount):
#             self.balance -= amount
#         else:
#             print("Insufficient Funds")
#         return self
#     # class method to change the name of the bank
#     @classmethod
#     def change_bank_name(cls,name):
#         cls.bank_name = name
#     # class method to get balance of all accounts
#     @classmethod
#     def all_balances(cls):
#         sum = 0
#         # we use cls to refer to the class
#         for account in cls.all_accounts:
#             sum += account.balance
#         return sum
#     # static methods have no access to any attribute
#     # only to what is passed into it
#     @staticmethod
#     def can_withdraw(balance,amount):
#         if (balance - amount) < 0:
#             return False
#         else:
#             return True


# alex_account = BankAccount(3, 1000)

# print(BankAccount.all_balances())

# alex_account.with_draw(1500)

#  NOTE - Overrdiding and Polymorphism of classes

# class Parent:
#     def method_a(self):
#         print("invoking PARENT method_a!")
# class Child(Parent):
#     def method_a(self):
#         print("invoking CHILD method_a!")
# dad = Parent()
# son = Child()
# dad.method_a()
# son.method_a() #notice this overrides the Parent method!

# # We'll use the Person class to demonstrate polymorphism
# # in which multiple classes inherit from the same class but behave in different ways
# class Person:
#     def pay_bill(self):
#         raise NotImplementedError
# # Millionaire inherits from Person
# class Millionaire(Person):
#     def pay_bill(self):
#         print("Here you go! Keep the change!")
# # Grad Student also inherits from the Person class
# class GradStudent(Person):
#     def pay_bill(self):
#         print("Can I owe you ten bucks or do the dishes?")

