Numbers = [8, 6, 3, 0, -4, 11]
print(Numbers)
idx = int(input("Enter the index address where the element to be inserted :"))
element = int(input("Enter the element to be inserted :"))
Numbers.insert(idx, element)
print("The list after insertion :",Numbers)