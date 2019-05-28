# Example 1
# This for loop only prints 0 through 4.
for i in range(10):
    if i == 5:
        break
    print (i)

# Example 2
# This for loop only prints 0 through 4 and 6 through 9.
for i in range(10):
    if i == 5:
        continue
    print (i)

# Example 3
"""
This program asks a user for the size of their bike frame and determines
if the size fits into the available constraints.
"""
# Continue asking user for a bike frame size until the size fits into constraints
while True:
    bike_frame_size = int(input("Enter bike frame size, in cm: "))
    if bike_frame_size > 60:
        print ("That bike is too big!")
    elif bike_frame_size < 55:
        print ("That bike is too small!")
    else:
        print ("That bike is the right size!")
        break
print ("Hooray, I found a bike.")

# Example 4
"""
This program continually asks a user to guess a number until they have guessed
the magic number.
"""
magic_number = 10
# Ask use to enter a number until they guess correctly
# When they guess the right answer, break out of loop
while True:
    guess = int(input("Guess my number: "))
    if guess == magic_number:
        print ("You got it!")
        break
    print ("Try again!")

# Print this sentence once number has been guessed
print ("Great job guessing my number!")

# 5.3.7
magic_number = 3
while True:
    guess = int(input("Guess a number 1-100: "))
    if(guess > magic_number):
        print("That was too low of a guess")
    elif(guess < magic_number):
        print("That was too high of a guess")
    else:
        break
    print("Try again")
print("You got it!")

# 5.3.8
my_float = 3.3312
while True:
    guess = float(input("Guess a decimal 1-100: "))
    if(guess > round(my_float,2)):
        print("That was too low of a guess")
    elif(guess < round(my_float,2)):
        print("That was too high of a guess")
    else:
        break
    print("Try again")
print("You got it!")
