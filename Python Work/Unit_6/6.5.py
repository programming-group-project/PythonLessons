# Example 1
"""
This program usees the keyword 'in' to determine if a certain character or
group of characters exists in a given string.
"""
word = "eggplant"
# Check if the letter 'e' is found in the given word
if "e" in word:
    print("Found an e in " + word)
else:
    print("Didn't find an e in " + word)
# Check if the letter 'a' is found in the given word
letter = "a"
if letter in word:
    print("Found " + letter + " in " + word)
else:
    print("Didn't find " + letter + " in " + word)
# Check if the phrase 'egg' is found in the given word
phrase = "egg"
if phrase in word:
    print("Found " + phrase + " in " + word)
else:
    print("Didn't find " + phrase + " in " + word)

# Example 2
"""
Ask the user for a string and something to look for within the string. Output whether
the second string is, in fact, in the first string.
"""
big_string = input("Enter a string: ")
string_to_find = input("Enter what to look for: ")
if string_to_find in big_string:
    print("Found it!")
else:
    print("Didn't find it.")

# 6.5.5
user_str = input("Enter a string of lowercase letters: ")
if(("a" in user_str) or ("e" in user_str) or ("i" in user_str) or ("o" in user_str) or ("u" in user_str)):
    print("Contains a lowercase vowel")
else:
    print("Doesnt contain a lowercase vowel")