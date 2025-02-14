f=open("twinkle.txt")

content=f.read()

if("twinkle" in content):
    print("Twinkle present in the poem")
else:
    print("Its not present")
f.close()