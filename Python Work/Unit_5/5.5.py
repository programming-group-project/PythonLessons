# Example 1
"""
This program tries to retrieve an integer from the user. If the user enters
something other than an integer, the program handles it by printing an error.
"""
try:
    my_number = int(input("Enter an integer: "))
    print ("Your number: " + str(my_number))
except ValueError:
    print ("That wasn't an integer!")

# Example 2
"""
This program asks the user for their name and age. It handles the case where the
user fails to enter a valid integer for their age.
"""
# Ask user for name and age.
# Enter default value for age in case they do not enter an integer
name = input("Enter your name: ")
age = -1
try:
    age = int(input("Enter your age: "))
except:
    print ("That wasn't an integer.")
# Print name and age, using default age if user did not enter an integer
print ("Name: " + name)
print ("Age: " + str(age))

# 6.5.5
numerator = 2
denominator = int(input("What do you want the denominator to be? "))
while(True):
    try:
        print(numerator / denominator)
        break
    except:
        print("Enter a non zero number")
    denominator = int(input("What do you want the denominator to be? "))

# 6.5.6
# I have no idea why this doesn't work, all i know is i cant run this file because of it
def convert_to_C(x):
    return(1.8 * x) + 32
def convert_to_F(x):
    return(x - 32) / 1.8
def user_convert():
    value = input("Would you like to conert to Celsius or Fahrenheit? ")
    if(value.lower() == "celcius"):
        try:
            print(convert_to_C(float(input("What is the temperature in Fahrenheit? "))))
        except:
            print("Invalid Number")
    elif(value.lower() == "fahrenheit"):
        try:
            print(convert_to_F(float(input("What is the temperature in Celsius? "))))
        except:
            print("Invalid Number")
    else:
        print("Invalid temperature type")
user_convert()

# 6.5.7
def retrieve_pos_number():
    while(True):
        user_number = input("Give me a positive number: ")
        try:
            user_number = int(user_number)
            if(user_number == 0):
                print("Zero is not a positive number")
            elif(user_number < 0):
                print("That is not a positive number")
            elif(user_number > 0):
                return(user_number)
        except:
            print("That is not a number")

print(retrieve_pos_number())