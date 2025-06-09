name = input("Enter Your Name :")
age  = int(input("Enter Your Age :"))
marks= float(input("Enter Your Marks :"))

Data = {
    "Name" : name,
    "Age" : age,
    "Marks" : marks,
}
print(Data)
print(type(Data))
print("The Marks From Data :",Data["Marks"])