num1 = 42    #variable declaration    Numbers
num2 = 2.3    #variable declaration    Numbers
boolean = True    #variable declaration    Boolean
string = 'Hello World'    #variable declaration    Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']    #variable declaration    Strings    List initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}    #variable declaration    Boolean    Dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana')    #variable declaration    Tuples initialize
print(type(fruit))    #log statement    type check    access value
print(pizza_toppings[1])  #log statement    access value
pizza_toppings.append('Mushrooms')    #add value
print(person['name'])    #log statement
person['name'] = 'George'    #change value
person['eye_color'] = 'blue'    #change value
print(fruit[2])    #log statement    access value

if num1 > 45:    #conditional
    print("It's greater")    #log statement
else:    #conditional
    print("It's lower")    #log statement

if len(string) < 5:    #length check    #conditional
    print("It's a short word!")    #log statement
elif len(string) > 15:    #length check    #conditional
    print("It's a long word!")    #log statement
else:    #conditional
    print("Just right!")    #log statement

for x in range(5):
    print(x)    #log statement
for x in range(2,5):
    print(x)    #log statement
for x in range(2,10,3):
    print(x)    #log statement
x = 0
while(x < 5):
    print(x)    #log statement
    x += 1

pizza_toppings.pop()    #delete value
pizza_toppings.pop(1)    #delete value

print(person)    #log statement
person.pop('eye_color')    #delete value
print(person)    #log statement

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')    #log statement
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')    #log statement

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')    #log statement

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')    #log statement

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section    #multi-line comment
"""

# print(num3)    single-line comment
# num3 = 72
# fruit[0] = 'cranberry'    single-line comment
# print(person['favorite_team'])    single-line comment
# print(pizza_toppings[7])    single-line comment
#   print(boolean)    single-line comment
# fruit.append('raspberry')    single-line comment
# fruit.pop(1)    single-line comment