# 9.6.1
class Food:
    def __init__(self):
        self.calories = 0
        self.category = ""
    def __repr__(self):
        return("Category: " + self.category + ", Calories: " + str(self.calories))
class Vegetable(Food):
    def __init__(self):
        Food.__init__(self)
        self.category = "Veggie"
class Broccoli(Vegetable):
    def __init__(self):
        Vegetable.__init__(self)
        self.calories = 100
thing = Broccoli()
print(thing)

# 9.6.2
foodList = [Food(), Vegetable(), Broccoli(), 5]
for thing in foodList:
    if isinstance(thing, Food):
        print(thing)
    else:
        print(str(thing) + " is not food.")