"""
Class creation. Object creation and class variable that is shared amon all the instances. 
"""
class Employee:
    empcount = 0
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        Employee.empcount += 1
        print("Name : {} Age: {}".format(self.name, self.age))
        print("Employee count {}".format(Employee.empcount))
    
e1 = Employee("Tamal", 32)
e2 = Employee("Thakur das", 65)
e3 = Employee("Shukla", 55)
e4 = Employee("Payal", 31)
e5 = Employee("Rinki", 23)