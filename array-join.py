"""
In this exercise we are going to implement the array functionality of join. 

There is 3 different ways it can be implemented. 

we will be covering one by one. 
"""
import array as ar

a = ar.array('i', [1,2,3,4,5,6,7])
b = ar.array('i', [7,8,9,10])

print("before a: {} b: {}".format(a,b))
for i in range(len(b)):
    a.append(b[i])

print("After b elements are appending {}".format(a))

print("now using the array tolist and then fromlist")
a = ar.array('i', [1,2,3,4,5])
b = ar.array('i', [5,6,7,8,9])
x = a.tolist()
y = b.tolist()
x.extend(b)
c = ar.array('i')
c.fromlist(x)
print("after join of a: {} b: {} c: {}".format(a,b,c))

print("Now in array have extend methond which can be used to join 2 array")
a = ar.array('i', [1,2,3,4,5])

b = ar.array('i', [6,7,8,9,10])
print("before a: {} b {}".format(a,b ))
a.extend(b)

print("After a: {} b: {}".format(a, b))