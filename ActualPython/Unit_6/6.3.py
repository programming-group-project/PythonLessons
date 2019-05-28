# Example 1
"""
This program shows the immutability of strings.
"""
'''my_string = "hello!"
my_string = "hi!"
my_other_string = my_string[:2]
# This line will cause an error because it tries to change a string.
my_string[0] = "H"'''

# 6.3.4
my_string = "hello!"
# One of the two lines below will cause an error.
# Each line is an attempt to replace the first
# letter of myString with H. Comment out the
# line you think is incorrect.
#my_string[0] = "H"
my_string = "H" + my_string[1:]
print(my_string)
