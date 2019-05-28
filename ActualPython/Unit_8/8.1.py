# Example 1
"""
This program shows how it is possible to index a list inside a list.
"""
my_list = []
my_list.append([1, 2, 3])
my_list.append([4, 5, 6])
print(my_list)
# Indexing into myList gives you a list of numbers
print(my_list[0])
# Indexing into THAT gives you a number
print(my_list[0][1])

# Example 2
"""
This program shows how it is possible to index a list inside a list.
"""
my_list = []
my_list.append([1, 2, 3])
my_list.append([4, 5, 6])
print(my_list)
# Indexing into myList gives you a list of numbers
print(my_list[0])
# Indexing into THAT gives you a number
print(my_list[0][1])

# Example 3
"""
This program shows how slicing and the append method can be used in a 2d list.
"""
my_list = []
# Append 3 lists to my_list.
for i in range(3):
    my_list.append([i * 1, i * 2, i * 4])
print(my_list)
# Take a slice of the outer list.
print(my_list[0:2])
# Take a slice of an inner list.
print(my_list[0][0:2])

# 8.1.1
def print_board(board):
    for i in range(len(board)):
        print(board[i])
def reset_row(reversed):
    row = [0,1,0,1,0,1,0,1]
    if(reversed == True):
        return row.reverse()
    else:
        return row
checkerboard = [[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]]
def start_board(board):
    temp = []
    for i in range(len(board)):
        if(i != 3 and i != 4):
            if (i % 2 == 0):
                temp += [reset_row(False)]
            elif (i % 2 == 1):
                temp += [reset_row(True)]
        else:
            temp += [0,0,0,0,0,0,0,0]
    return temp
checkerboard = start_board(checkerboard)
print_board(checkerboard)
# 8.1.2
# I cannot figure this out im sorry
# 8.1.3
# 8.1.4
