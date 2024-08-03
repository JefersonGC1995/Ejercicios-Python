mi_set = set([1, 2, 3, 4, 5, 6])
#mi_set = set({1, 2, 3})
#mi_set = set((1, 2, 3))

mi_set = {1, 2, 3}
print(len(mi_set))

conjunto = {1,2,3,4,5,6,7,8,9,1,1}
print(conjunto)

print(2 in conjunto)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)
s1.add(4)
print(s1)
s1.remove(3)
print(s1)
s1.clear()
print(s1)