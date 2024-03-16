"""
This example will show the inner and outter class example.
"""

class Student:
    def __init__(self) -> None:
        self.name = "Tamal Kundu"
        self.obj = self.Subjects()
    
    def display(self):
        print("Name: ", self.name)
        print("Display subject : ", self.obj.display_sub())
    class Subjects:
        def __init__(self) -> None:
            self.sub1 = "Physics"
            self.sub2 = "Maths"

        def display_sub(self):
            return "Subject 1 :", self.sub1, "Subject 2 : ", self.sub2

s1 = Student()
s1.display()