"""
This is an emaple of Dynamic Overriding.  
""" 

class Shape:
    def draw(self):
        print("Draw method")
        return 

class Circle(Shape):
    def draw(self):
        print("Draw a circle")
        return 

class Rectangle(Shape):
    def draw(self):
        print("Draw rectangle.")
        return 

shapes = [Circle(), Rectangle()]
for obj in shapes:
    print(obj.draw())


