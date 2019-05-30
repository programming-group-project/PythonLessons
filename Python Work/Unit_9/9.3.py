import random
# Rectangle Class
class rect:
    def __init__(self, length = 2, width = 2):
        self.length = length
        self.width = width
    def __repr__(self):
        return("Rectangle with length " + str(self.length) + " and width " + str(self.width))
    def __eq__(self, other):
        if((self.length == other.length) and (self.width == other.width)):
            return("Rectangles have the same dimensions!")
        else:
            return("Rectangles have different dimensions!")
# 9.3.1
rectangle = rect(3, 5)
print(rectangle)

# 9.3.2
r1 = rect(3, 4)
r2 = rect(3, 4)
r3 = rect(6, 4)
print(r1 == r2)
print(r1 == r3)

# 9.3.3
class NameHat:
    def __init__(self):
        self.list = []
    def __repr__(self):
        return(str(self.list))
    def insert_name(self, name):
        in_list = False
        for i in range(len(self.list)):
            if(name == self.list[i]):
                in_list = True
        if(in_list == False):
            self.list += [name]
        else:
            print("That name is already in the hat")
    def draw_name(self):
        if(len(self.list) == 0):
            choice = "There are no names in the hat"
        else:
            choice = random.choice(self.list)
            location = self.list.index(choice)
            self.list = self.list[:location] + self.list[location + 1:]
        return choice
names_in_hat = NameHat()
user_choice = input("Do you wish to run NameHat program? Y/N: ")
if(user_choice == "Y"):
    while True:
        user_input = input("Which command do you wish to use; print, insert, or draw: ")
        if(user_input == "print"):
            print(names_in_hat)
        elif(user_input == "insert"):
            names_in_hat.insert_name(input("Enter name you wish to input: "))
        elif(user_input == "draw"):
            print(names_in_hat.draw_name())
        elif(user_input == "end"):
            break
        else:
            print("I coundn't undestand what you said")
