"""
Python program that shows the method overriding process. s
"""

class Employee:
    def __init__(self, name, sal) -> None:
        self.name = name
        self.salary = sal
    
    def get_name(self):
        return self.name
    
    def get_salary(self):
        return self.salary
    
class SalaryOfficier(Employee):
    def __init__(self, name, sal, increament) -> None:
        super().__init__(name, sal)
        self.increment = increament
    
    def get_salary(self):
        return self.salary + self.increment


e1 = Employee("Rajesh", 10000)
print("Total salary for {} is rs: {}".format(e1.get_name(), e1.get_salary()))
e2 = SalaryOfficier("Kiran", 98000, 10000)
print("Total salaray of {} is rs: {}".format(e2.get_name(), e2.get_salary()))