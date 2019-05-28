# Example 1
"""
This program shows how keys are used in dictionaries.
"""
# Create an empty dictionary
my_dictionary = {}
# Set particular keys and values directly
my_dictionary["Jonathan"] = 100
my_dictionary["Karel"] = 200
my_dictionary[100] = 2
print(my_dictionary)
# Use the keys to print the associated values
print(my_dictionary["Jonathan"])
print(my_dictionary["Karel"])
# Can you guess what this line will print??
print(my_dictionary[my_dictionary["Jonathan"]])

# Example 2
"""
This programs shows how the in keyword can be used to determine whether or
not a particular key exists in a dictionary.
"""
my_dictionary = {
    "a": 1,
    "b": 2
}
# This key is in my_dictionary, so this will print True.
print("a" in my_dictionary)
# This one isn't, so this will print False.
print("z" in my_dictionary)
# 2 is not a key in my dictionary, so this will print False.
print(2 in my_dictionary)
# You can also write a for loop that iterates
# over just the keys in the dictionary.
for key in my_dictionary:
    print("key: " + str(key))
    print("value: " + str(my_dictionary[key]))

# 8.4.1
def phonebook():
    phonebook = []
    inphonebook = False
    while True:
        user_input = input("Give me a name: ")
        if(user_input == ""):
            break
        else:
            for i in range(len(phonebook)):
                if(user_input == phonebook[i][0]):
                    print(str(phonebook[i][0]) + " " + str(phonebook[i][1]))
                    inphonebook = True
            if(inphonebook == False):
                phonebook += [[user_input, input("Give me a phone number: ")]]
            inphonebook = False
    print(phonebook)

# 8.4.2
