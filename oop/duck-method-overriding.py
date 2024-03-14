"""
In this example we are going to see the duck method of overriding. 
"""
class Shape:
    def draw(self):
        print("Draw method")
class Circle:
    def draw(self):
        print("Draw a circle")

class Rectangle:
    def draw(self):
        print("Draw a rectangle.")

class Area:
    def area(self):
        print("This is just area")

def duck_funstion(obj):
    obj.draw()
objs = [Shape(), Circle(), Rectangle()]

for i in objs:
    duck_funstion(i)

