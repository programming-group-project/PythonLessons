import math
# Rectangle Class
class rect:
    num_rectangles = 0
    def __init__(self, length = 2, width = 2, color = "black"):
        self.length = length
        self.width = width
        self.color = color
        rect.num_rectangles += 1
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

# 9.5.1
r1 = rect()
print(r1)
print(r1.num_rectangles)
r2 = rect()
print(r2)
print(r2.num_rectangles)
r2 = rect()
print(r2)
print(r2.num_rectangles)

# 9.5.2
class Car:
    num_cars_made = 0
    num_doors = 4
    def __init__(self, doors = 4):
        self.num_doors = doors
        self.num_wheels = 4
        self.color = "boring gray"
        Car.num_cars_made += 1

car1 = Car()
print(car1.color)
c2 = Car(6)
c2.color ="red"
print(c2.color)
print("#####")
print(car1.num_doors)
car1.num_doors = 10
print(car1.num_doors)
print(c2.num_doors)
print(Car.num_doors)