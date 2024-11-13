no = int(input("Initial No :"))
no2 = int(input("Final No :"))

for i in range(no , no2):
    if i % 3 == 0 :
        continue
    elif i == 35:
        break
    print(i ,end=" ")