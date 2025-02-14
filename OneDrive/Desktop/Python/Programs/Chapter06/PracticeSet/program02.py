marks1=int(input("Enter your marks : "))
marks2=int(input("Enter your marks : "))
marks3=int(input("Enter your marks : "))

toatl_per=(100*(marks1+marks2+marks3))/300

if(toatl_per>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed And you have scored : ",toatl_per)
else:
    print("Better luck next time ,You have scored : ",toatl_per)