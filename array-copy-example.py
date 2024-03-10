"This is a simple example of python array copy"
import array as ar

a = ar.array('i', [1,2,3,4,5])
b = a.__copy__()

print(a)
print(b)
print(id(a))
print(id(b))

c=a
print(id(c))
print(id(a))

a[1]=100
c[2]=200

print(id(a))
print(id(c))
print(a)
print(c)