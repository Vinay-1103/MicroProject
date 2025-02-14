for i in range(1,6):
    print(i)

# While loop

i=1
while(i<=50):
    print(i)
    i+=1
# usin list in loop
l=[10,"Vinay",False,78.5,"Kumar"]

i=0
while(i<len(l)):
    print(l[i])
    i+=1

# range
for i in range (0,100,5):
    print(i)

# for loop in list

l=[10,52,98,785.45]

for i in l:
    print(i)

# for in tuple

t=(45,87,94,64)

for i in t:
    print(i) 


# loop usin strinf

n="Vinay Kumar"
for i in n:
    print(i)

for i in range(1,10):
    print(i)
    if(i==5):
        break

for i in range(1,10):
    if(i==5):
        continue
    print(i)