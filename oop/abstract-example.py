"""
This is a simple example of doing abstract method.
"""
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def draw(self):
        print("Abstract method")
        return 


class Circle(Shape):
    def draw(self):
        super().draw()
        print("Draw a circle..")
        return 

class Rectangle(Shape):

    def draw(self):
        super().draw()
        print("Draw a rectangle")
        return 
    
shapes = [Circle(), Rectangle()]
for i in shapes:
    print(i.draw())