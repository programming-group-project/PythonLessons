# Example 1
# This function returns the number 10. Wherever it is used, Python
# effectively replaces it with the number 10, similar to how Python
# replaces 3 + 4 with the number 7.
def return_ten():
    return 10
print (return_ten())
x = return_ten()
print (x + 1)

# 6.4.4
def return_plus_one(num):
    return num + 1
print(return_plus_one(41))

# Example 2
# Here's a function that has a parameter and a return value. It takes the
# parameter and returns the negative of it.
def negate(x):
    return -x
print (negate(5))
x = negate(-4)
print (x)

# Example 3
# A function can call another function!
def add_two(x):
    return x + 2
def multiply_by_three(x):
    return x * 3
def my_function(x):
    return add_two(x) + multiply_by_three(x)
print (my_function(12))

# Example 4
# The return value of one function can be used as the parameter of another. This
# is called function composition.
def add_two2(x):
    return x + 2
def multiply_by_three2(x):
    return x * 3
def my_function2(x):
    return add_two2(multiply_by_three2(x))
print (my_function2(5))

# 6.4.8
def sum(x,y):
    return x + y
print(sum(2,2))

# 6.4.9
def convert_to_C(x):
    return(1.8 * x) + 32
def convert_to_F(x):
    return(x - 32) / 1.8
def user_convert():
    value = input("Would you like to conert to Celcius or Fahrenheit? ")
    if(value.lower() == "celcius"):
        convert_to_C(int(input("What is the temperature in Fahrenheit? ")))
    elif(value.lower() == "fahrenheit"):
        convert_to_F(int(input("What is the temperature in Celcius? ")))
    else:
        print("Invalid temperature type")
user_convert()