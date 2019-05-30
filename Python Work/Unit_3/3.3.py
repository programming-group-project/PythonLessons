# Example 1
x = 10
y = 5

print ("x is " + str(x))
print ("y is " + str(y))

print ("Is x equal to y?")
print (x == y)

print ("Is x not equal to y?")
print (x != y)

print ("Is x less than y?")
print (x < y)

print ("Is x greater than y?")
print (x > y)

print ("Is x less than or equal to y?")
print (x <= y)

print ("Is x greater than or equal to y?")
print (x >= y)



# Example 2
"""
This program determines if Yelena can clear the bar in the high jump event
"""
# Set the bar
height_of_bar = 1.9
print ("The bar is " + str(height_of_bar) + " meters off the ground.")
# Yelena jumps!
yelena_jump = 2.0
print ("Yelena's jump: " + str(yelena_jump) + " meters.")
if yelena_jump > height_of_bar:
    print ("Yelena cleared the bar!")
else:
    print ("Yelena didn't clear the bar.")



# Example 3
"""
This program determines if a rider reaches the height requirement for the
roller coaster.
"""
height = 5.5
height_requirement = 5.0
# You must be at least 5.0 feet tall to ride the roller coaster.
can_ride_roller_coaster = height >= height_requirement
if can_ride_roller_coaster:
    print ("You are tall enough to ride this roller coaster!")
else:
    print ("Sorry, you aren't tall enough.")



# 4.3.6
age = int(input("What is your age?: "))

if age >= 19:
    print("You can vote")
else:
    print("You are not old enough to vote")


# 4.3.7
num = int(input("Give me a number: "))
if num == 0:
    print("That number is zero")
elif num > 0:
    print("That number is positive")
elif num < 0:
    print("That number is negative")


# Example 4
"""
This program determines which age group a certain number falls into.
"""
age = 33
# Each branch below only gets reached if every prior branch had
# a condition that evaluated to False.
if age < 18:
    print ("0 - 17")
elif age < 26:
    print ("18 - 25")
elif age < 36:
    print ("26 - 35")
elif age < 46:
    print ("36 - 45")
elif age < 56:
    print ("46 - 55")
elif age < 66:
    print ("56 - 65")
else:
    print ("66+")


# 4.3.9
reservation_name1 = "Sage"
reservation_name2 = "sage"
name = input("What is your name? ")
print("Name: " + name)
if reservation_name1 == name or reservation_name2 == name:
    print("Right this way")
else:
    print("I'm sorry we don't have a reservation under that name")


# 4.3.10
user_balance = 1000
user_temp_balance = user_balance
user_decision = input("Do you want to make a deposit or a withdrawl?: ")
if user_decision == "deposit":
    user_change_balance = int(input("How much money do you wish to " + user_decision + "?: "))
elif user_decision == "withdrawl":
    user_change_balance = -int(input("How much money do you wish to " + user_decision + "?: "))
else:
    user_change_balance = 0
    print("Invalid transaction")

user_temp_balance += user_change_balance

if(user_temp_balance < 0):
    print("You cannot have a negative balance")
else:
    user_balance = user_temp_balance
    print("Your final balance is: " + str(user_balance))