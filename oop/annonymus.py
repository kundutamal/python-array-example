"""
In this example we are going to learn about anonymus function. 
"""
def getA(self):
    return "Value of A is : ", self.a

obj = type('', (object,), {'a':5, 'b': 6, 'c':7, 'getA': getA, 'getB': lambda self: self.b})()
print(obj.getA(), obj.getB())