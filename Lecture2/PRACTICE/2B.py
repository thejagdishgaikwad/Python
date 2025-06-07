#"Write a python program to check if a list contains a palindrome of elemebts or not"
Data = []
Data.append(int(input("Enter the data element 1:")))
Data.append(int(input("Enter the data element 2:")))
Data.append(int(input("Enter the data element 3:")))

print(Data)
Data2 = Data.copy()
Data2.reverse()
print(Data2.reverse())
print(Data == Data2)
if(Data2 == Data):
    print("The Given Number Is Palindrome!\n")
else:
    print("The Given Number Is Not Palindrome!\n")