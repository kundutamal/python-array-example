"""
This is inheritence example. 
Multiple Inheritence
"""

class Division:
    def __init__(self, a, b) -> None:
        print("This is Division class constructor.")
        self.n = a
        self.d = b 

    def division(self):
        return self.n/self.d
    
class Modules:
    def __init__(self, a, b) -> None:
        print("This is Modules class constructor.")
        self.n = a
        self.d = b

    def mod_disvision(self):
        return self.n % self.d 
    
class mod_div(Division, Modules):
    def __init__(self, a, b) -> None:
        self.n = a
        self.d = b
        super(mod_div,self).__init__(a, b)
        super(mod_div,self).__init__(a,b)

    def mod_div_res(self):
        dival = Division.division(self)
        divmod = Modules.mod_disvision(self)
        return (dival, divmod)

c1 = mod_div(10, 5)
print(c1.division())
print(c1.mod_disvision())
print(c1.mod_div_res())