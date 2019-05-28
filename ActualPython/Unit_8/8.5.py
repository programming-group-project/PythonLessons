# Example 1
"""
This program shows the difference between equivalence and identity with mutables.
"""
print("---- list_two = list_one ----")
list_one = [1, 2, 3]
list_two = list_one
# Both variables now refer to the same list
if list_one == list_two:
    print("Equivalent!")
else:
    print("Not equivalent.")
if list_one is list_two:
    print("Identical!")
else:
    print("Not identical.")
# Altering listOne also alters listTwo
list_one[0] = 10
print("list_one: " + str(list_one))
print("list_two: " + str(list_two))
# However, replacing the contents of listOne does not affect listTwo
print("---- list_one = [1, 2, 3] ----")
list_one = [1, 2, 3]
print("list_one: " + str(list_one))
print("list_two: " + str(list_two))
if list_one == list_two:
    print("Equivalent!")
else:
    print("Not equivalent.")
if list_one is list_two:
    print("Identical!")
else:
    print("Not identical.")

# Example 2
"""
This program displays equivalence and identity with immutables.
"""
string_one = "hi there"
string_two = string_one
if string_one == string_two:
    print("Equivalent!")
else:
    print("Not equivalent.")
if string_one is string_two:
    print("Identical!")
else:
    print("Not identical.")

# Example 3
# This function takes a single argument and returns nothing. It assumes the
# argument is a list. It appends the number 6 to the list.
def change_my_list(my_list):
    my_list.append(6)
numbers = [1, 2, 3]
print(numbers)
# This will affect numbers!
change_my_list(numbers)
print(numbers)

# 8.5.1
# swap_lists
# -----
# This function takes two lists of equal length 
# as arguments and swaps their values.
global list_one1
list_one1 = [1, 2, 3]
global list_two1
list_two1 = [4, 5, 6]
def swap_lists(first, second):
    if len(first) != len(second):
        print("Lengths must be equal!")
        return
    temp = first
    first = second
    second = temp
print("Before swap")
print("list_one: " + str(list_one1))
print("list_two: " + str(list_two1))
swap_lists(list_one1, list_two1)
print("After swap")
print("list_one: " + str(list_one1))
print("list_two: " + str(list_two1))
# This wont work and i have no clue why, i want to die

# 9.5.2