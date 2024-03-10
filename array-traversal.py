"For loop to traverse array"
import array as ar

a = ar.array('i', [1,2,3,4,5,6])
"using for loop"
for i in a:
    print(i)
c=0
l=len(a)
"using while loop"
while(c<=l):
    print(a[c])
    c+=1

