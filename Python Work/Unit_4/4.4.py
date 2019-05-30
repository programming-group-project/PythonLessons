# Example 1
"""
This program visualizes nested for loops but printing number 0 through 3
and then 0 through 3 for the nested loop.
"""
for i in range(4):
    print ("Outer for loop: " + str(i))
    for j in range(4):
        print ("    Inner for loop: " + str(j))

# Example 2
"""
This program asks for the test scores for multiple people, and reports the average
test score for each person.
"""
# Try changing these, and see what happens!
num_people = 3
tests_per_person = 3
# For each person, get name and test scores
for i in range(num_people):
    name = input("Enter name: ")
    sum = 0 
    # Add up the test scores
    for j in range(tests_per_person):
        score = int(input("Enter a score: "))
        sum = sum + score   
    # Calculate and print average score
    average = float(sum) / tests_per_person
    print ("Average for " + name + ": " + str(average))


# Example 3
# You can also nest for loops with
# while loops. Check it out!
for i in range(4):
    print ("For loop: " + str(i))
    x = i
    while x >= 0:
        print ("    While loop: " + str(x))
        x = x - 1

# 5.4.6
for i in range(1, 7):
    for x in range(1, 7):
        print(str(i) + ", " + str(x))

# 5.4.7
    for i in range(3):
        category = input("Enter a category: ")
        category_list = ""
        for x in range(3):
            category_list += " " + input("Enter something in that category: ")
        print(category + ": " + category_list)