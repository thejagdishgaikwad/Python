#Write a python program to check if a number entered by user is odd or even?
Number = int(input("Enter Any Number Of Your Choice :"))
if(Number % 2 == 0):
    print("The Number",Number,"is Even!\n")
elif(Number % 2 != 0):
    print("The Number",Number,"is Odd!\n")
else:
    print("INVALID ENTRY!!!\n")