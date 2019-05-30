# Example 1
x = True
y = False
print ("x: " + str(x))
print ("y: " + str(y))
print ("x and y")
print (x and y)
print ("x or y")
print (x or y)
print ("x and not y")
print (x and not y)
# This means "It is not the case
# that x is true, and it is the
# case that y is true."
print ("not x and y")
print (not x and y)
# Notice that you can use parentheses
# to force (x and y) to be evaluated
# before the "not" keyword is applied.
#
# This means "It is not the case that
# both x and y are true."
print ("not (x and y)")
print (not (x and y))


# 4.4.4
user_role = input("Are you a teacher, administrator, or student?: ")
if(user_role == "administrator" or user_role == "teacher"):
    print("You can have a key")
elif(user_role == "student"):
    print("Students cannot have keys")
else:
    print("You must be one of the three choices")


# 4.4.5
user_age = int(input("What is your age?: "))
user_citizen = input("Were you born in the US?: ")
if(user_citizen == "yes" or user_citizen == "Yes"):
    user_citizen = True
else:
    user_citizen = False
user_resident = int(input("How long have you been a US resident?: "))
if(user_age >= 35 and user_citizen == True and user_resident >= 14):
    print("You are eligible to be a US President")
else:
    if(user_age < 35):
        print("You are too young, must be at least 35 years of age")
    elif(user_citizen == False):
        print("You must be born in the US")
    elif(user_resident < 14):
        print("You haven't been a resident for long enough, you must be a resident for 14 years")