"""
This is a simple example to show the example of constructors.
"""

class Employee:
    def __init__(self, name="Default", age=20) -> None:
        self.name = name
        self.age = age

    def display(self):
        print("Name : ", self.name)
        print("Age : ", self.age)

e1 = Employee("Tamal", 34)
e2 = Employee()
e1.display()
e2.display()