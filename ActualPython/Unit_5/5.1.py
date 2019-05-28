# Example 1
# This function prints a greeting
def greeting():
    print ("Hi there!")
    print ("Nice to meet you!")
# Call the function to run
greeting()

# Example 2
"""
This code will print out a greeting based on the time of day.
"""
# This function will print a greeting for the morning
def morning_greeting():
    print ("Good morning! It will be a lovely day!") 
# This function will print a greeting for the afternoon
def afternoon_greeting():
    print ("Good afternoon! I hope you are having a lovely day!") 
# This function will print a greeting for the evening
def evening_greeting():
    print ("Good evening! I hope you had a lovely day!")
# Get input from the user and print matching greeting
# If other option, print that it is invalid
time_of_day = input("What time of day is it? (morning, afternoon, evening): ")
if time_of_day == "morning":
    morning_greeting()
elif time_of_day == "afternoon":
    afternoon_greeting()
elif time_of_day == "evening":
    evening_greeting()
else:
    print ("Invalid option.")

# 6.1.5
weather = input("What is the weather like today? Sunny, rainy, or snowy? ")
def greating(int):
    if(int == 1):
        shoe = "sandals"
        weather = "sunny"
    elif(int == 2):
        shoe = "galoshes"
        weather = "rainy"
    elif(int == 3):
        shoe = "boots"
        weather = "snowy"
    print("On a "+weather+" day, "+shoe+" are appropriate footwear.")
if(weather == "Sunny" or weather == "sunny"):
    greating(1)
elif(weather == "Rainy" or weather == "rainy"):
    greating(2)
elif(weather == "Snowy" or weather == "snowy"):
    greating(3)