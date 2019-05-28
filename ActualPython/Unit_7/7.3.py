# Example 1
"""
This program will use for loops to go through elements in a list in
multiple ways.
"""
my_list = ["hi", 5, 4.7]
# Print each element in the list
for thing in my_list:
    print("The next thing is: " + str(thing))
# Use the len function to control the range value in your for loop
for index in range(len(my_list)):
    print("The thing at index " + str(index) + \
          " is " + str(my_list[index])) 
# Keep track of the index value as well as the element stored there
for index, value in enumerate(my_list):
    print("The thing at index " + str(index) + \
          " is " + str(value))

# Example 2
"""
This program uses for loops to iterate through a list and uses the range
values in the for loop as the index values to print each list element.
"""
first_list = [1, 10, 3]
second_list = [2, 5, 6]
# This for loop uses the length of the list to determine the index values
for index in range(len(first_list)):
    print("Looking at index: " + str(index))
    thing_in_first_list = first_list[index]
    thing_in_second_list = second_list[index]
    
    print("   1st list has: " + str(thing_in_first_list))
    print("   2nd list has: " + str(thing_in_second_list))
    if (thing_in_first_list > thing_in_second_list):
        print("      thing in 1st list was bigger")
    elif (thing_in_second_list > thing_in_first_list):
        print("      thing in 2nd list was bigger")

# 7.3.5
my_list = [5, 2, -5, 10, 23, -21]
def max_int_in_list(lis):
    large = lis[0]
    for i in range(len(lis)):
        if lis[i] >= large:
            large = lis[i]
    print(large)
max_int_in_list(my_list)

# 7.3.6
def find_word(string, word):
    string = string.lower()
    string = string.split()
    word_count = 0
    for i in range(len(string)):
        temp = string[i]
        correct_count = 0
        for i in range(len(word)):
            if(temp[i] == word[i]):
                correct_count += 1
            else:
                break
            if(correct_count == len(word)):
                word_count += 1
    return word_count
print(find_word("I really like owls. Did you know that an owl's eyes are more than twice as big as the eyes of other birds of comparable weight? And that when an owl partially closes its eyes during the day, it is just blocking out light? Sometimes I wish I could be an owl." , "owl"))

# 7.3.7
def replace_i(string):
    for i in range(len(string)):
        if(string[i] == "i"):
            string = string[:i] + "!" + string[i+1:]
    return string
print(replace_i("hello i like to eat pie"))

# 7.3.8
def word_ladder():
    word = input("Give me a word: ")
    word_list = [word,]
    for i in range(4):
        index = int(input("Give me an index number: "))
        if(index < len(word) and index >= 0):
            replace = input("Give me a letter: ")
            word = word[:i] + replace + word[i+1:]
            word_list += [word,]
    print(word_list)
word_ladder()