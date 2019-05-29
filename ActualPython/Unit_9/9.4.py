import math
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
    def __add__(self, other):
        return([self.length + other.length, self.width + other.width])
    def __sub__(self, other):
        return([abs(self.length - other.length), abs(self.width - other.width)])

r1 = rect(3, 4)
r2 = rect(3, 8)
r3 = rect(6, 5)

# 9.4.1
r4 = r1 + r2
print(r4)

# 9.4.2
r5 = r3 - r2
print(r5)

# 9.4.3
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

class ContactBook:
    def __init__(self):
        self.book = {}
    def __repr__(self):
        return(str(self.book))
    def __add__(self, other):
        for key in other.book:
            if((key in self.book) == True):
                if(self.book[key] != other.book[key]):
                    self.book[key] = (str(self.book[key]) + " or " + str(other.book[key]))
            else:
                self.book[key] = other.book[key]
        return self.book
    def add_person(self):
        person = input("Who do you wish to add to this contact book? ")
        if((person in self.book)==False):
            self.book[person] = input("Give me " + person + "'s number: ")
        else:
            print("This person is already in the contact book")
c1 = ContactBook()
c2 = ContactBook()
user_choice = input("Do you wish to run ContactBook program? Y/N: ")
if(user_choice == "Y"):
    while True:
        user_input = input("Which command do you wish to use; print, insert, add, or end: ")
        if(user_input == "end"):
            break
        elif(user_input == "add"):
            c1 = c1 + c2
            c2 = ContactBook()
            print("Contact Book 1 and 2 have been combined, Contact Book 2 has been wiped")
        elif(user_input == "print" or user_input == "insert"):
            user_effecting = input("Which book do you wish to change; c1/c2: ")
            if(user_input == "print"):
                if(user_effecting == "c1"):
                    print(c1)
                elif(user_effecting == "c2"):
                    print(c2)
            elif(user_input == "insert"):
                if(user_effecting == "c1"):
                    c1.add_person()
                elif(user_effecting == "c2"):
                    c2.add_person()
            elif(user_input == "end"):
                break
            else:
                print("I coundn't undestand what you said")
        else:
            print("I coundn't undestand what you said")
    print("The program has been terminated")