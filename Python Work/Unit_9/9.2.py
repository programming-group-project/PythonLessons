# 9.2.1 + 9.2.2
class rect:
    def __init__(self, length = 2, width = 2):
        self.length = length
        self.width = width
    def get_dimensions(self):
        print("Length: " + str(self.length))
        print("Width: " + str(self.width))
    def get_area(self):
        print("Area: " + str(self.length * self.width))
    def get_perimeter(self):
        print("Perimeter: " + str(self.length*2 + self.width*2))