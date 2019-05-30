# Example 1
x = 0.0037 / 100
y = 0.000037
# These numbers look equal!
print (x)
print (y)
# ... But they aren't exactly equal!
if x == y:
    print ("Equal!")
else:
    print ("Unequal!")
# ... But they are approximately equal (to five decimal places)!
if round(x, 5) == round(y, 5):
    print ("Approximately equal!")
else:
    print ("Not approximately equal!")


# 4.5.4
# Amount of food and number of people
tons_of_food = 0.07
num_people = 25
# Determine how much food each person gets
tons_of_food_per_person = tons_of_food / num_people
print (tons_of_food_per_person)
# Ask the user how much food they took
tons_taken = float(input("How many tons of food did you take? "))
if tons_taken == round(tons_of_food_per_person,5):
    print ("Good job, you took the right amount of food!")
else:
    print ("You took the wrong amount of food!")
