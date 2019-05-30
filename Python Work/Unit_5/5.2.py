# Example 1
"""
This program prints a variable saved in a function.
"""
def print_something():
    x = 10
    print (x)
print_something()

# Example 2
"""
This program shows how changing an outside variable from within a function
makes another variable!

In this program, printSomething has its own variable called z. It can no longer
access the outer variable called z.
"""
z = 6.5
def print_something2():
    z = "hi"
    print (z * 3)
print_something2()
print (z * 3)

# 6.2.5
"""
This program takes two values and prints their sum.
"""
def add_nums():
    global sum
    num1 = 5
    num2 = 6
    sum = num1 + num2
add_nums()
print (sum)

# 6.2.6
def add_user_nums():
    global sum2
    num1 = 5
    num2 = int(input("Give me a number: "))
    sum2 = num1+ num2
add_user_nums()
print(sum2)

#  6.2.7
def decision(mode, num1, num2):
    global sum3
    if(mode == "add"):
        sum3 = num1 + num2
    elif(mode == "subtract"):
        sum3 = num1 - num2
    elif(mode == "multiply"):
        sum3 = num1 * num2
    else:
        sum3 = "Invalid operation"

user_num1 = int(input("What is the first number? "))
user_num2 = int(input("What is the second number? "))
user_mode = input("Chose an operation(add, subtract, multiply): ")
decision(user_mode, user_num1, user_num2)
print(sum3)