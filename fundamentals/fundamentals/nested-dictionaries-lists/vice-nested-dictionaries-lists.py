#   1) Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


x[1][0] = 15
students[0]["last_name"] = "Bryant"
sports_directory["soccer"][0] = "Andres"
z[0]["y"] = 30

print(x)
print(students)
print(sports_directory)
print(z)
print("")
#   2) Iterate Through a List of Dictionaries

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(arr):
    for i in range(len(arr)):
        if i > 0:
            print("")
        for key, val in arr[i].items():
            # print(key, "-", val, ", ", end="")
            print(f"{key} - {val}"+",", end=" ")

iterateDictionary(students)
print("")
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


#   3) Get Values From a List of Dictionaries

def iterateDictionary2(key_name, list):
    for i in range(len(list)):
        print(list[i][key_name])
print("")
iterateDictionary2("first_name", students)
print("")
iterateDictionary2("last_name", students)
print("")

#   4) Iterate Through a Dictionary with List Values

def printInfo(dict):
    for key, val in dict.items():
        print(len(val), key)
        for i in range(len(val)):
            print(val[i])
        print("")

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)