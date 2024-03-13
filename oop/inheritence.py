"""

inheritence concept
"""

class Parent:
    def __init__(self) -> None:
        self.attr = 1000
        print(" calling parrent constructor.")

    def parentMethod(self):
        print("Calling parent method")
    
    def set_attr(self, attr):
        self.attr = attr

    def get_attr(self):
        print("Parent attributes : ", self.attr)

class Child(Parent):
    def __init__(self) -> None:
        print("calling child constructor ")
        super(Child, self).__init__()

    def childMethod(self):
        print("calling child method.. ")

e1 = Child()
e1.childMethod()
e1.get_attr()
e1.parentMethod()
e1.set_attr(2000)
e1.get_attr()
