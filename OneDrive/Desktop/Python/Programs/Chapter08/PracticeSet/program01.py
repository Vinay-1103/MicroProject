def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
a=int(input("Enter number : "))
b=int(input("Enter number : "))
c=int(input("Enter number : "))

print(f"Greatest among the numbers is :{greatest(a,b,c)}")