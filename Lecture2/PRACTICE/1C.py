#write a python program to check if the entered number is divisible by 7 or not!
Number = int(input("Enter any number of your choice :"))
if(Number%7==0):
    print(Number,"is divisible by 7!\n")
elif(Number%7 != 0):
    print(Number,"is not divisible by 7!\n")
else:
    print("INVALID ENTRY!\n")