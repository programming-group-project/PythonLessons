# Example 1
"""
This program shows how range can be used in a list comprehension to make a
list out of a range.
"""
numbers = [x for x in range(5)]
print(numbers)

# Example 2
"""
This example prints a list of the first five square numbers, staring at 1.
"""
numbers = [x * x for x in range(1, 6)]
print(numbers)

# 8.2.1
def divide_by_three():
    numbers = [x % 3 == 0 for x in range(1, 11)]
    print(numbers)
divide_by_three()

# Example 3
"""
This program uses the math module and the round function to print pi
approximated to different numbers of decimal places.
"""
import math
print([round(math.pi, i) for i in range(1, 6)])

# Example 4
"""
This program creates a list of booleans from the original list, where True
is given if the number is even and False otherwise.
"""
original_list = [10, 6, -43, 4, 3, 4, 0, 50]
print([x % 2 == 0 for x in original_list])

# 8.2.2
names = [
    "Maya Angelou",
    "Chimamanda Ngozi Adichie",
    "Tobias Wolff",
    "Sherman Alexie",
    "Aziz Ansari"
]
# Your code here...

# 8.2.3
list_of_strings = ["a", "2", "7", "zebra"]
def safe_arg(list):
    return_list =[]
    for i in range(len(list)):
        try:
            return_list += [int(list[i])]
        except:
            return_list += [0]
    print(return_list)
safe_arg(list_of_strings)
