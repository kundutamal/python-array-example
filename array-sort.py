"Array sort alogorithm. sort alogorithm"

import array as ar

a = ar.array('i', [12, 5, -1, 2, 100, -2])
print(a)

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print(a)