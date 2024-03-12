"This example shows classmethod"

class Employee:
    empCount = 0
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        Employee.empCount += 1
    
    def showcount(self):
        print("Total employee", self.empCount)
    
    counter = classmethod(showcount)

e1 = Employee("Wipro", 3.4)
e2 = Employee("TCS", 4.11)
e3 = Employee("Xoriant", 5)

Employee.counter()
e1.counter()