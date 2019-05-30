# Exmaple 1
"""
This program shows how indexing and slicing can be used with lists.
"""
# Creating an empty list:
my_list = []
print(my_list)
# Creating a list with things in it:
list_of_things = ["hi", 3, 4.8]
thing_zero = list_of_things[0]
thing_one = list_of_things[1]
thing_two = list_of_things[2]
print(thing_zero)
print(thing_one)
print(thing_two)
print(list_of_things)
print(len(list_of_things))
# Unlike with a tuple, you can change a particular element in a list!
list_of_things[0] = 2
print(list_of_things)
# Get everything starting at thing 0 and going up to BUT NOT INCLUDING thing 2
print(list_of_things[0:2])
# This gets things 1 and 2
print(list_of_things[1:3])
# This gets everything from thing 1
# to the end.
print(list_of_things[1:])
# This gets everything from the beginning up to but not including
# thing 2
print(list_of_things[:2])
# This gets the last thing.
print(list_of_things[-1])
# This gets the last two things.
print(list_of_things[-2:])
# This gets everything but the last thing.
print(list_of_things[:-1])

# Exampe 2
"""
This program shows how strings can be turned into lists and lsits into strings.
"""
my_string = "abcde"
print(my_string)
# Turn string into a list
my_list = list(my_string)
print(my_list)
# Turn list into a string
my_other_string = "".join(my_list)
print(my_other_string)

# 7.2.5
user_name = list(input("What is your name? "))
print(user_name)

# Example 3
"""
This program will turn a phrase into a list by separating elements at
the whitespace (or spaces) entered.
"""
my_string = "try to be a rainbow in someone's cloud"
print(my_string)
my_list = my_string.split()
print(my_list)

# 7.2.7
user_info = input("What is your name, age, and favorite sport? ")
user_info = user_info.split()
print("Hello, " + user_info[0] + "! I also enjoy " + user_info[2])

# Example 4
"""
This program displays the rules of modifying lists and tuples.
"""
# Here we have a list with a tuple embedded
my_list = ["a", "b", "c", (1, 2, 3)]
print(my_list)
# You can alter the list this way because you are allowed to replace a tuple
# and you are allowed to change a list.
my_list[3] = (10, 2, 3)
print(my_list)
# Here we have a tuple with a list embedded
my_tuple = ("a", "b", "c", [1, 2, 3])
print(my_tuple)
# You can alter the tuple by changing the element inside the list because
# you are allowed to change a list.
my_tuple[3][0] = 10
print(my_tuple)
