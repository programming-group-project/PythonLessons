# Example 1
"""
This program shows how to use the len function to determine the length of
a string.
"""
print(len("hello"))
print(len(""))
print(len("a b c d e"))
my_string = "hello"
bad_index = len(my_string)
# This line causes an error.
#print(my_string[bad_index])

# 6.4.4
user_name = input("What is your name? ")
print(len(user_name))

# Example 2
"""
This program uses a for loop to print out each letter in the string on its
own line using indicies.
"""
my_string = "hello"
for i in range(len(my_string)):
    print(my_string[i])

# Example 3
"""
This program uses a for loop to print out each letter in the string on its
own line.
"""
my_string = "hello"
for letter in my_string:
    print(letter)

# 6.4.7
bee_string = "bepis"
for i in range(len(bee_string)):
    print(bee_string[i] + "!")

# 6.4.8
string_one = "Hello"
sring_check = "l"
def count_occurances(str1, str2):
    count = 0
    for i in range(len(str1)):
        if(str1[i] == str2):
            count += 1
    return count
print(count_occurances("hello", "l"))