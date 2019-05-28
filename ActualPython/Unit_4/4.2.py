# Example 1
"""
This program prints ten numbers - 0 through 9.
"""
# Inside the for loop, we can treat i like a normal integer variable.
for i in range(10):
    print (i)

# Example 2
"""
This program prints the numbers 1 though 10.
"""
for i in range(1, 11):
    print (i)

# 5.2.5
for i in range(10, 100, 10):
    print(i)

# Example 3
"""
This program first asks the user how many numbers they want to total. It then
asks them for that many numbers and reports the total of the numbers.
"""
total = 0
number_of_numbers = int(input("How many numbers would you like to sum? "))
# Repeat the code the number of times indicated by the user
for i in range(number_of_numbers):
    next = int(input("Enter a number: "))
    total = total + next
print("Sum: " + str(total))

# 5.2.8
score = int(input("What is your score? "))
for i in range(2):
    score += int(input("What is your score? "))
print("Your average: " +str(score/3))

# 5.2.9
amount_names = int(input("How many names do you have? "))
full_name = ""
for i in range(1, amount_names + 1):
    if(i == 1):
        name = input("What is your " + str(i) + "st name? ")
    elif(i == 2):
        name = input("What is your " + str(i) + "nd name? ")
    elif(i == 3):
        name = input("What is your " + str(i) + "rd name? ")
    else:
        name = input("What is your " + str(i) + "th name? ")
    full_name += (name + " ")
print(full_name)
