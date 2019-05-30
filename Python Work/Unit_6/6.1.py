# Example 1
"""
This program shows how index values are assigned and utilized to isolate
specific characters in a string.
"""
# indices:             0   1   2   3   4   5
#                      h   e   l   l   o   !
# negative indices:    -6  -5  -4  -3  -2  -1
my_string = "hello!"
print ("my_string[0] is " + my_string[0])
print ("my_string[1] is " + my_string[1])
print ("my_string[2] is " + my_string[2])
print ("my_string[-1] is " + my_string[-1])
print ("my_string[-2] is " + my_string[-2])
print ("my_string[-3] is " + my_string[-3])

# 6.1.4
name_first = input("What is your first name? ")
name_last = input("What is your last name? ")
print("Initals: " + name_first[0] + "." + name_last[0] + ".")

# 6.1.5
my_string2 = "doghouse"
# print "h" here
print(my_string2[3])
# print "e" here
print(my_string2[7])
# print "e" using a second index value
print(my_string2[-1])
