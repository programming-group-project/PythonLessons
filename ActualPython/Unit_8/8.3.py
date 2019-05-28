# Example 1
"""
This program shows how packing can use variables as elements in a list.
"""
x = 1
y = 2
z = 3
my_list = [x, y, z]
print(my_list)

# Example 2
"""
This program shows how unpacking can be used to separate out elements in 
a list or tuple.
"""
# Assign multiple variables at a time, like this:
x, y, z = 1, 2, 3
print("x: " + str(x))
print("y: " + str(y))
print("z: " + str(z))
# Assign multiple variables to a list (only if the number of variables
# is the SAME as the number of elements in the list.)
my_list = [10, 20, 30]
x, y, z = my_list
print("x: " + str(x))
print("y: " + str(y))
print("z: " + str(z))
# A tuple can also be used
my_tuple = (1.0, 2.0, 3.0)
x, y, z = my_tuple
print("x: " + str(x))
print("y: " + str(y))
print("z: " + str(z))

# Exmaple 3
"""
This program shows how unpacking can be used to assign parameters to a function.
"""
def sum_three_numbers(x, y, z):
    return x + y + z
my_list = [1, 2, 3]
# Split list into respective pieces using asterisk
sum = sum_three_numbers(*my_list)
print(sum)

# 8.3.1
def cords():
    user_x = int(input("Give me the x value: "))
    user_y = int(input("Give me the y value: "))
    user_cord = [user_x, user_y]
    print(user_cord)

# 8.3.2
def slope():
    cords = []
    while True:
        try:
            user_cords = [int(input("Give me cord " + str(len(cords)+1) + "'s x value: ")),int(input("Give me cord " + str(len(cords)+1) + "'s y value: "))]
            cords += [user_cords]
            if(len(cords) == 5):
                break
        except:
            print("Enter a number value")
    slope = 0
    for i in range(4):
        slope = (cords[i+1][1] - cords[i][1]) / (cords[i+1][0] - cords[i][0])
        print("Slope between "+ str(cords[i]) +" and "+ str(cords[i+1])+": " + str(slope))

# Example 4
"""
This program shows how to can swap variables using unpacking.
"""
first = 10
second = 20
print("Before swap: first is " + str(first) + ",  second is " + str(second))
# Swap using unpacking
first, second = second, first
print("After swap: first is " + str(first) + ",  second is " + str(second))

# 8.3.3
def name():
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    list_name = [first_name, last_name]
    print("Full name: " + str(list_name[0]) + " " + str(list_name[1]))
    print("Citation: " + str(list_name[1]) + ", " + str(list_name[0]))
slope()