number = [20, 7, 13, 22, 23, 9]

odd_count = 0
even_count = 0

for num in number :
    if num % 2 == 0:
        even_count +=1
    else :
        odd_count +=1

print("No even No's : ", even_count)
print("No of odd no's : ", odd_count)