#Write a python program to take 2 inputs A and B, and print True if a is greater than or equal to B, If not print False.
#1. My approach
Num1 = int(input("Enter A :"))
Num2 = int(input("Enter B :"))

if(Num1>=Num2):
    print("Statement :", (Num1>=Num2) and (Num2<=Num1))
else:
    print("Statement :", (Num1<=Num2) and (Num2<=Num1))

#2. Best Approach
print(Num1>=Num2)
