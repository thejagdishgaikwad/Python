name = input("Enter Your Name :")
age  = int(input("Enter Your Age :"))
Mathematics = float(input("Enter Mathematics Marks :"))
Physics = float(input("Enter Physics Marks :"))
Chemistry = float(input("Enter Chemistry Marks :"))

Data = {
    "Name" : name,
    "Age" : age,
    "Marks" : {
        "maths " : Mathematics, 
        "physics " : Physics,
        "chemistry " : Chemistry,
    }
}
print(Data)
print(type(Data))
print("The Marks From Data :",Data["Marks"])