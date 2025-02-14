p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

ms=input("Enter a message : ")

if((p1 in ms) or (p2 in ms )or (p3 in ms) or (p4 in ms )):
    print("This is spam message")
else:
    print ("Not a spam")