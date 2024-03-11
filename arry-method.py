"""
In this example we are going to see different type of method used by array.
"""

import array as ar

a = ar.array('i', [1, 2,3, 4, 5, 2])

print("Before a : {}".format(a))
a.reverse()

print("After a : {}".format(a))

c = a.count(2)
print(c)

print(a.index(5))

a = ar.array("u", ["Wipro", "TCS", "Xoriant"])
with open("file.txt", mode="w+") as file:
    a.tofile(file)


