# Example 1
"""
This program repeatedly asks a user to guess a number. The program ends
when they're geussed correctly.
"""
# Secret number
my_number = 10
# Ask the user to guess
guess = int(input("Enter a guess: "))
# Keep asking until the guess becomes equal to the secret number
while guess != my_number:
    print ("Guess again!")
    guess = int(input("Enter a guess: "))
print ("Good job, you got it!")

# Example 2
# See if you can guess what this program prints!
x = 10
while x > 5:
    print (x)
    x = x - 2

# Example 3
# Can you guess what this program prints?
x = 5
y = 5
while x > 5 or y < 10:
    print (x)
    print (y)
    x = 15 - x
    y = y + 2

# 5.1.6
num = 2
while num <= 20:
    print(num)
    num += 2

# 5.1.7
numerator = int(input("Enter a numerator: "))
denominator = int(input("Enter denominator: "))
# Use a while loop here to repeatedly ask the user for
# a denominator for as long as the denominator is 0
# (or, put another way, until the denominator is not
# equal to 0).
while denominator == 0:
    print("You cannot divide by zero")
    denominator = int(input("Enter denominator: "))
if numerator / denominator * denominator == numerator:
    print ("Divides evenly!")
else:
    print ("Doesn't divide evenly.")

