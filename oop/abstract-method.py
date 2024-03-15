"""
This is an axample of abstract method.
"""
from abc import ABC, abstractmethod
class Democlass(ABC):
    @abstractmethod
    def method1(self):
        print("Abstract method is defined here..")
    
    def method(self):
        print("Another method but this is no abstract method")

class Example(Democlass):
    def method1(self):
        return super().method1()
    

list_Example = [Example(), Example(), Example()]
for i in list_Example:
    print(id(i), type(i))
    print(i.method1())
    print(i.method())