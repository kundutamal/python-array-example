"""
This is an example of singletone class.
"""

class SingletoneClass:
    _instance = None

    def __new__(cls):
        print(cls, type(cls))
        print("Creating the object.. ")
        if cls._instance is None:
            cls._instance = super(SingletoneClass, cls).__new__(cls)
    
        return cls._instance
    

obj1 = SingletoneClass()
print(obj1)

obj2 = SingletoneClass()
print(obj2)