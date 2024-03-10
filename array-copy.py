import array, copy

a = array.array('i', [1,2,3,4,5,6])
b = copy.deepcopy(a)
print("a : ", a)
print("b : ", b)

a[2]=100
print("a : {}".format(a))
print("b : {}".format(b))