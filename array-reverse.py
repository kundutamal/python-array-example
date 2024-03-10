"Array reverse"
import array

a = array.array('i', [1,2,3,4,5,6])
b = array.array('i')
l = len(a)
for i in range(l-1, -1, -1):
    b.append(a[i])
print("a : ", a)
print("b : ", b)    

print("Now another way of doing reverse array.")
a = array.array('i', [10, 20, 30, 40, 50])
b = a.tolist()
a = array.array('i')
a.fromlist(b)
print("a : ", a)
print("This is an example of array and array reverse using list")