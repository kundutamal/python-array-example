"""
This is simple program that will show the public, protected and private variable.
"""

class Employee:
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.__age = age
        self._salary = salary
    
    def get_age(self):
        return self.__age

e1 = Employee("Tamal", 32, 98000)
print(e1.name)
#print(e1.__age)
print(e1._salary)

print(e1.get_age())