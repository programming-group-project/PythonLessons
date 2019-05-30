# Example 1
# This function takes a single parameter and prints it.
def print_number(x):
    print (x)
print_number(12)
print_number("dog")

# Example 2
"""
This function takes two arguments. It expects the first to be a string and
the second to be a number.
"""
def print_name_and_age(name, age):
    print ("Hi, my name is " + name + " and I am " + str(age) + " years old.")
print_name_and_age("Sierra", 34)
print_name_and_age("Marcus", 19)

# 6.3.5
def multiply(x,y):
    print(x * y)
multiply(5,10)

# 6.3.6
def printmultiple(str, length):
    for i in range(length):
        print(str)

# Example 3
# This function prints the numbers given as parameters and uses a
# default value for y if none is given.
def print_two_numbers(x, y = 10):
    print ("First number: " + str(x))
    print ("Second number: " + str(y))
print_two_numbers(5)
print_two_numbers(7, 8)

# 6.3.8
def calculate_area(length = 10):
    if(length <= 0):
        print("Cannot have side length of " + str(length))
        length = 10
        calculate_area(int(input("What is the side length of the square? ")))
    else:
        print("The length of a square with the side length of " + str(length) + " is: " + str(length * 2))
calculate_area(int(input("What is the side length of the square? ")))