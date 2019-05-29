# 9.8.1
class Food:
    edible = True
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
thing1 = Food()
thing2 = Vegetable()
thing3 = Broccoli()