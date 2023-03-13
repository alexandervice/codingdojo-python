def countdown(num):
    arr = []
    for i in range(num, -1, -1):
        arr.append(i)
    return(arr)

# print(countdown(5))

def print_and_return(num1,num2):
    print(num1)
    return(num2)

# print(print_and_return(1,2))

def first_plus_length(arr):
    return arr[0]+arr[len(arr)-1]

# print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second(arr):
    if len(arr) < 2:
        return False
    else:
        output = []
        for i in range(len(arr)):
            if arr[i] > arr[1]:
                output.append(arr[i])
        print(len(output))
        return output

# print(values_greater_than_second([5,2,3,2,1,4]))
# print(values_greater_than_second([3]))

def this_length_that_value(num1,num2):
    output = []
    for i in range(num1):
        output.append(num2)
    return output

# print(this_length_that_value(4,7))
# print(this_length_that_value(6,2))