# Example 1
"""
This program shows the different ways to index a tuple.
"""
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])
print(my_tuple[:2])
print(len(my_tuple))
# -- THE LINE BELOW WOULD CAUSE AN ERROR --
# my_tuple[0] = 10

# Example 2
"""
This program shows the different elements that can be found within a tuple.
"""
my_tuple = (0, 1, "hi", (2, 3))
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])
# my_tuple[3] is, itself, a tuple.
print(my_tuple[3])
# The first square bracket accesses the tuple (2, 3) within the larger tuple.
# The second square bracket accesses the integers within this smaller tuple.
print(my_tuple[3][0])

# Example 3
"""
This program shows how to create a tuple with a single element.
"""
# This just creates an integer...
x = (3)
print(x)
print(type(x))
# This creates a tuple
x = (3,)
print(x)
print(type(x))

# Example 4
"""
This program shows how to concatenate tuples.
"""
x = (1, 2)
y = (5, 6)
my_tuple = x + (3, 4) + y
print(my_tuple)
my_tuple = x + (3,) + y
# This should print (1, 2, 3, 5, 6)
print(my_tuple)

# 7.1.7
my_tuple = (0, 1, 2, "hi", 4, 5)
my_tuple = my_tuple[:3] + (3,) + my_tuple[4:]
print(my_tuple)

# 7.1.8
author_name = ("Martin", "Luther", "King, Jr.")
first_name = str(author_name[0])
middle_name = str(author_name[1])
last_name = str(author_name[2])
print(last_name + ", " + first_name + " " + middle_name)

# 7.1.9
order_1 = ("Lee", 0, 2)
order_2 = ("Tamia", 1, 0)
order_3 = ("Edward", 1, 1)
amount_hotdogs = int(order_1[1]) + int(order_2[1]) + int(order_3[1])
amount_burgers = int(order_1[2]) + int(order_2[2]) + int(order_3[2])
print("You need to buy " + str(amount_burgers) + " burgers.")
print("You need to buy " + str(amount_hotdogs) + " hotdogs.")

# 7.1.10
import math
#cord1 = (int(input("Give me the x cord of the first point: ")),(int(input("Give me the y cord of the first point: "))))
#cord2 = (int(input("Give me the x cord of the second point: ")),(int(input("Give me the y cord of the second point: "))))
def distance(point1, point2):
    return math.sqrt(pow((point1[0] - point2[0]),2) + pow((point1[1] - point2[1]),2))
print(distance((1, 1), (4, 5)))