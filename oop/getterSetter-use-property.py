"""
Instead of using getter and setter method we have done. Now using property which you will need to setup for the property this is a simple example that will show you how to setup. 
"""

class Employee:
    def __init__(self, name, age) -> None:
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name 
    def get_age(self):
        return self.__age
    
    def set_name(self, name):
        self.__name = name 
    
    def set_age(self, age):
        self.__age = age 
    
    name = property(get_name, set_name, "NAME")
    age = property(get_age, set_age, "AGE")


e1 = Employee("Bhavanan", 24)
print("Name : ", e1.name, "Age :", e1.age)

e1.name = "Tamal"
e1.age = 34

print("Name : ", e1.name, "Age : ", e1.age)

