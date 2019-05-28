# Example 1
"""
This program turns a string into all capital or all lowercase letters.
"""
first_string = "hello"
second_string = first_string.upper()
third_string = second_string.lower()
print(first_string)
print(second_string)
print(third_string)

# 6.6.4
def add_enthusiasm(str):
    return str.upper() + "!"
print(add_enthusiasm("sage"))

# Example 2
"""
This program uses the swapcase method which returns a new string equal to the
old string, but with uppercase letters turned into lowercase letters
and vise versa.
"""
s = "PyThOn"
print(s)
print(s.swapcase())

# Example 3
"""
This program uses the strip method which returns a new string equal to the
old string with leading and trailing whitespace characters (spaces, tabs, etc.)
removed.
"""
s = "    hi there    "
print(s)
print(s.strip())

# Example 4
"""
This program uses the find method which returns the first index at which
a particular string is found within a string, or -1 if it is not found.
"""
s = "abra kadabra alakazam"
print(s)
print(s.find("a"))
print(s.find("kadabra"))
print(s.find("q"))

# 6.6.8
def firstNameVowel():
    user_name = input("What is your first name? ")
    user_name = user_name.lower()
    for i in range(len(user_name)):
        if((user_name[i] == "a") or (user_name[i] == "e") or (user_name[i] == "i") or (user_name[i] == "o") or (user_name[i] == "u")):
            vowel = user_name[i]
            vowel_location = i
            print("There is an " + vowel + " in your name, first found at index: " + str(vowel_location))

# 6.6.9
def remove_all_from_string(str1, str2):
    string = str1.lower()
    while(True):
        if(string.find(str2) != -1):
            string = string[:(string.find(str2))] + string[(string.find(str2))+1:]
        else:
            break
    return string
print(remove_all_from_string("hello","l"))

# 6.6.10
def remove_all_from_string2(str1, str2):
    string = str1.lower()
    while(True):
        if(string.find(str2) != -1):
            string = string[:(string.find(str2))] + string[(string.find(str2))+len(str2):]
        else:
            break
    return string
print(remove_all_from_string2("bananas","na"))