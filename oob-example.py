"""
This is the first program of OOP
"""
class Employee:
    def __init__(self, name="Tamal", age=35) -> None:
        self.name = name 
        self.age = age 
    def display(self):
        print("name : {} age {}".format(self.name, self.age))

print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__dict__)
print(Employee.__bases__)