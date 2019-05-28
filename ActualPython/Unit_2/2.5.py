# Example 1
print ("hello " + ", world!")
print ("a" + "b" + "c")
print ("hi" * 3)

print ("hi" + str(3))
print ("My bike has " + str(6) + " gears.")

# 3.5.4
instrument = "kazoo"
age = 7

print ("I have played the " + instrument + " since I was " + str(age) + " years old.")

# Example 2
num_people = int(input("How many people are playing?: "))
num_teams = int(input("How many teams?: "))

people_per_team = num_people/ num_teams
left_over = num_people % num_teams

print ("If there are " + str(num_teams) + " teams, there will be " + \
str(people_per_team) + " on each team, with " + str(left_over) + " left over.")

# 3.5.6
my_name = "Sage"
my_age  = 16

print("Hi! My name is " + my_name + " and I am "+ str(my_age) + " years old")

# 3.5.7
length = 10
width = 5
print("Area = " + str(length * width))
print("Perimeter = " + str(2 * length + 2 * width))

# 3.5.8
length2 = int(input("What is the length? "))
width2 = int(input("What is the width? "))
print("Area = " + str(length2 * width2))
print("Perimeter = " + str(2 * length2 + 2 * width2))

# 3.5.9
ing1_name = input("What is the first ingredient?")
ing1_amount = float(input("How many ounces of " + ing1_name + "?"))
ing2_name = input("What is the second ingredient?")
ing2_amount = float(input("How many ounces of " + ing2_name + "?"))
ing3_name = input("What is the third ingredient?")
ing3_amount = float(input("How many ounces of " + ing3_name + "?"))
amount_of_servings = int(input("How many servings do you want?"))
print("Number of servings: " + str(amount_of_servings))
print("Total ounces of " + ing1_name + ": " + str(ing1_amount))
print("Total ounces of " + ing2_name + ": " + str(ing2_amount))
print("Total ounces of " + ing3_name + ": " + str(ing3_amount))
end_program = input("End Program: ")
