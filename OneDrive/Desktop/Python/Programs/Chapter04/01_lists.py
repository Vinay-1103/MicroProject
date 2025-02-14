l1=[45,24,"vinay",78.45]
print(l1)

print(l1[0])
print(l1[3])
print(l1[2])

# methods of lists

l1 = [1,8,7,2,21,15]
l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.append(122)
l1.sort()
print(l1)

l1.insert(1,"vinay")
print(l1)

l1.pop(1)
print(l1)

l1.extend([15,464])
print(l1)

l1.remove(122)
print(l1)

c=l1.count(2)
print(c)

l1.clear()
print(l1)