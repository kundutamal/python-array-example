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

