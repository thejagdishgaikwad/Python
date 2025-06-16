name = input("Enter Your Name :")
age  = int(input("Enter Your Age :")) #age can never be in the decimal format
Mathematics = float(input("Enter Mathematics Marks :")) #the marks can be in decimal format or whole format so better to declare the bigger variable type
Physics = float(input("Enter Physics Marks :"))
Chemistry = float(input("Enter Chemistry Marks :"))

Data = {
    "Name" : name,
    "Age" : age,
    "Marks" : {
        "maths" : Mathematics, 
        "physics" : Physics,
        "chemistry" : Chemistry,
    }
}
Data["Surname"] = "Gaikwad" #Insertion
print(type(Data)) #type of data printing
print(Data) #all the data available in the "Data" Dictionary
print("The Marks From Data :",Data["Marks"]) #the marks available from the nested dictionary
print(Data ["Marks"] ["physics"]) #printing the data from nested dictionary
print("The keys in this Data Dictionary :",Data.keys()) #Printing the variables from the dictionary "Data"
print("The all keys from the Marks Sub-Dict :", Data["Marks"].keys()) #Printing the keys from the nested dictionary
print("The pairs from the main Data Dictionary :", Data.items()) #Getting the (key, val) pairs from the main dictionary
print("The pairs from the Nested 'Marks' Dictionary :",Data["Marks"].items())#Getting the (key, val) pairs from the nested dictionary marks
print(Data["Age"]) #demonstration if we search the value of an non existing key
print(Data.get("Ae")) #to get the value of a existing or non existing key without getting error
Data["Marks"].update({"Biology" : 33}) #using update function
print("Marks :", Data["Marks"])