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
    
obj = [Employee("Tamal", 32), Employee("Thakur das", 65), Employee("Shukla", 55),Employee("Payal", 31), Employee("Rinki", 23)]

for i in obj:
    print(i.name, i.age, i.empcount, Employee.empcount)