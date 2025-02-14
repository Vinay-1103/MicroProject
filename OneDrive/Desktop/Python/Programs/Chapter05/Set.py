s=set()

print(s)

s.add(100)
print(s)

s.add(45)

print(s)

print(len(s))
# print(s.remove(45))
# print(s.remove(100))
# print(s)

a={12,45,87,96,5,45}

print(a)

print(a.union(s))
print(a|s)

s.update([45,64,94])
print(s)

print(a|s)

print(a&s)

print(45 in a)

print(0 in a)