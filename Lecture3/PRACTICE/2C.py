'''write a python program to 1.Count the number of students got "A" grade from the following Tuple Tup=[C, D, A, A, B, B ,A]
2. Store the values above from the list and sort them from "A" to "D" '''

Data = ("C", "D", "A", "A", "B", "B", "A")
print("The no of students got Grade A :", Data.count("A"))

DataLS = []
DataLS.append(input("Enter Grade :"))
DataLS.append(input("Enter Grade :"))
DataLS.append(input("Enter Grade :"))
DataLS.append(input("Enter Grade :"))
DataLS.append(input("Enter Grade :"))
DataLS.append(input("Enter Grade :"))
DataLS.append(input("Enter Grade :"))
print(DataLS)
DataLS.sort()
print("The Data In Sorted Sequence from A TO D :", DataLS)