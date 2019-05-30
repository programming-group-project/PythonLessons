'''
# 9.1.1
class rect:
    def __init__(self):
        self.length = 0
        self.width = 0
    def print_size(self):
        print("Length: " + str(self.length))
        print("Width: " + str(self.width))


rectangle = rect()
rectangle.length = 5
rectangle.width = 6
rectangle.print_size()
'''
# 9.1.2
class rect2:
    def __init__(self, length = 0, width = 0):
        self.length = length
        self.width = width
    def print_size(self):
        print("Length: " + str(self.length))
        print("Width: " + str(self.width))
rectangle2 = rect2()
rectangle2.print_size()
rectangle3 = rect2(6,7)
rectangle3.print_size()