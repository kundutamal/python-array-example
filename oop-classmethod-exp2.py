"""
Now using the @classmethod
"""

class Employee:
    empCount = 0

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        Employee.empCount += 1

    @classmethod
    def showcount(cls):
        print("Total employee : ",cls.empCount)
        return
    
    @classmethod
    def newEmployee(cls, name, age):
        cls(name, age)
    
e1 = Employee("Tamal", 32)
e2 = Employee("Surajit", 34)
e3 = Employee("Suranjan", 31)

e4 = Employee.newEmployee("Jyoti", 23)

Employee.showcount()