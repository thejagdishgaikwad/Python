#write a PYTHON program to find the greatest among 3 numbers!
Num1 = int(input("Enter A:"))
Num2 = int(input("Enter B:"))
Num3 = int(input("Enter C:"))

if(Num1>Num2 and Num1>Num3):
    print(Num1,"is the greatest!\n")
elif(Num2>Num3):
    print(Num2,"is the greatest!\n")
else:
    print(Num3,"is the greatest!\n")