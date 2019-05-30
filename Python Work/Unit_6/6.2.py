# Example 1
"""
This program shows how index values are assigned and utilized to isolate
multiple characters in a string.
"""
# indexes:             0   1   2   3   4   5
#                      h   e   l   l   o   !
# negative indices:    -6  -5  -4  -3  -2  -1
my_string = "hello!"
print ("my_string[1:3] is " + my_string[1:3])
print ("my_string[1:] is " + my_string[1:])
print ("my_string[:3] is " + my_string[:3])

# Example 2
"""
This program gives several examples of creating strings out of two other
strings, or out of pieces of those strings.
"""
string_one = "abcde"
string_two = "fghij"
print ("string1: " + string_one)
print ("string2: " + string_two)
string_three = string_one + string_two
print ("string3: " + string_three)
string_four = string_two + string_one
print ("string4: " + string_four)
string_five = string_one + " " + string_two
print ("string5: " + string_five)
string_six = string_one[0] + " " + string_two[1:]
print ("string6: " + string_six)

# 6.2.6
def first_character(str):
    return str[0]
def all_but_first(str):
    return str[1:]
print(first_character("hello"))
print(all_but_first("hello"))

# 6.2.7
def replace_at_index(str,ind):
    str = str[:ind] + "-" + str[ind + 1:]
    return str
s = replace_at_index("eggplant",3)
print(s)

# 7.2.8
user_string = input("Enter a word or phrase: ")
user_index = int(input("Enter the index number of what word you want to replace: "))
user_replace = input("Enter what you want to replace it with: ")
def user_replace_cha(str,int,cha):
    str = str[:int] + cha + str[int+1:]
    return str
print(user_replace_cha(user_string,user_index,user_replace))