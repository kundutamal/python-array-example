"""
This example will show you the static method. 
"""

class Employee:
    empCount = 0
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age 
        Employee.empCount += 1
    
    @staticmethod
    def showcount():
        print(Employee.empCount)

e1 = Employee("Tamal", 31)
e2 = Employee("Surajit", 32)
e3 = Employee("Ajit", 35)

e1.showcount()
Employee.showcount()