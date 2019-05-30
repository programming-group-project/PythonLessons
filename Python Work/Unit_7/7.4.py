# Example 1
"""
This program demonstrates how append and extend can be used to add to a list.
"""
# Start with an empty list
my_list = []
print(my_list)
# Append things to the end of the list.
# Each call to append changes the list.
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
print(my_list)
# Extend adds a list to a list!
my_list.extend([5, 6, 7])
print(my_list)
# This line will not actually change the value of the variable 'my_list'
print(my_list + [10, 12, 14])
print(my_list)

# 7.4.4
def user_name_list():
    user_names = int(input("How many names do you have? "))
    user_name = []
    for i in range(user_names):
        user_name += [input("Name: ")]
    user_first_name = str(user_name[0])
    print("First Name: " + user_first_name)
    if(user_names > 2):
        user_middle_names = user_name[1:user_names - 1]
        print("Middle Name(s): " + str(user_middle_names))
    user_last_name = str(user_name[-1])
    print("Last Name: " + user_last_name)

# 7.4.5
def number_list():
    list = []
    sum = 0
    for i in range(5):
        list += [int(input("Give me a number: "))]
        sum += list[i]
        print(list)
    print(sum)

# Example 2
"""
This program uses the sort method on a list to change the list such that the
elements are placed in order from least to greatest.
"""
my_list = [1, 4, 2, -4, 10, 0]
print(my_list)
my_list.sort()
print(my_list)

# 7.4.7
def ssh_is_library():
    library = []
    for i in range(5):
        library += [input("Last Name of Author: ")]
    library.sort()
    print(library)

# Example 3
"""
This program uses the reverse method to change a list such that it is in the
reverse order that it was in. Note that it does NOT put it in reverse sorted
order (unless the list was ALREADY in sorted order).
"""
my_list = [1, 4, 2, -4, 10, 0]
print(my_list)
my_list.reverse()
print(my_list)

# Example 4
"""
This program uses the count method which does not change the list. It returns
an integer that represents how many instances of a particular thing were
found in the list.
"""
# List of numbers
my_list = [1, 4, 2, -4, 10, 0, 4, 2, 1, 4]
print(my_list)
# Find how many of each number are in the list
print("There are " + str(my_list.count(4)) + " 4's in this list.")
print("There are " + str(my_list.count(1)) + " 1's in this list.")
print("There are " + str(my_list.count(-4)) + " -4's in this list.")
print("There are " + str(my_list.count(700)) + " 700's in this list.")
print("-----------------")
# List of strings
list_of_strings = ["hi", "hello", "hi", "hi", "hello"]
print(list_of_strings)
# Find how many of each word are in the list
print("There are " + str(list_of_strings.count("hi")) + " hi's in this list.")
print("There are " + str(list_of_strings.count("hello")) + " hello's in this list.")

# Example 5
"""
This program uses the remove method to remove a particular thing from a list.
"""
my_list = ["apple", "banana", "orange", "grapefruit"]
print(my_list)
my_list.remove("apple")
print(my_list)
# Note that it ONLY removes the first occurrence of something.
my_list = ["apple", "banana", "orange", "grapefruit", "apple"]
print(my_list)
my_list.remove("apple")
print(my_list)

# 7.4.11
my_list = ["broccoli", "apple", "zucchini", "rambutan", "grapefruit"]
# Your code here...
my_list.remove("grapefruit")
my_list.sort()
my_list.reverse()
print(my_list)

# 7.4.12
def ssh_is_library2():
    library = []
    for i in range(5):
        temp = input("Authors Full Name: ")
        temp.split()
        library += temp[-1]
    library.sort()
    print(library)
ssh_is_library2()
# 7.4.13
def owl():
    word = "owl"
    #string = input("Enter some text here: ")
    string = "Owls are so cool! I think snowy owls might be my favorite. Or maybe spotted owls."
    string = string.lower()
    string = string.split()
    word_count = 0
    word_index = []
    for i in range(len(string)):
        temp = string[i]
        correct_count = 0
        for x in range(len(word)):
            if(temp[x] == word[x]):
                correct_count += 1
            else:
                break
            if(correct_count == len(word)):
                word_count += 1
                word_index += [i]
    print("There were " + str(word_count) + " words that contained \"owl\".")
    print("They occurred at indices: " + str(word_index))
owl()
