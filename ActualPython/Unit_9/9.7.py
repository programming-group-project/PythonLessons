import math
# 9.7.1
class rect:
    __num_rectangles = 0
    def __init__(self, length = 2, width = 2, color = "black"):
        self.length = length
        self.width = width
        self.color = color
        self.area = self.length * self.width
        if(self.area % 2 == 0):
            rect.__num_rectangles += 1
    def __repr__(self):
        return("Rectangle with length: " + str(self.length) + ", width: " + str(self.width) + ", and color: " + self.color)
    def __eq__(self, other):
        if((self.length == other.length) and (self.width == other.width)):
            return("Rectangles have the same dimensions!")
        else:
            return("Rectangles have different dimensions!")
    def __add__(self, other):
        return([self.length + other.length, self.width + other.width])
    def __sub__(self, other):
        return([abs(self.length - other.length), abs(self.width - other.width)])
    def get_area(self):
        if(self.area % 2 == 0):
            return("Area: " + self.area)
        else:
            return("Area is not an even value")
    def get_num_rectangles(self):
        return (rect.__num_rectangles)

# 9.7.2
class TripleAndHalve:
    def __init__(self):
        self.number = 1
    def triple(self):
        self.number *= 3
    def halve(self):
        self.number /= 2
    def __repr__(self):
        return(str(self.number))
num = TripleAndHalve()
user_choice = input("Do you wish to run TripleAndHalve program? Y/N: ")
if(user_choice == "Y"):
    while True:
        user_input = input("Which command do you wish to use; triple, halve, print, or end: ")
        if(user_input == "end"):
            break
        elif(user_input == "print"):
            print(num)
        elif(user_input == "triple"):
            num.triple()
        elif(user_input == "halve"):
            num.halve()
        else:
            print("I coundn't undestand what you said")
    print("The program has been terminated")