Name = input("\nEnter Your Name :")
Age = int(input("\nEnter Your Age :"))
PvtCode = int(input("\nEnter The SECRET CODE To gain access :"))

if(Name == "Jagdish") and (Age == 20) and (PvtCode == 1309):
    print("Welcome Master, Reign Your Legacy!\n")
elif(Name == "Jagdish") and (Age == 20) and (PvtCode != 1309):
    print("Name and Age Is Correct, BUT PVT CODE ERRORRRR!!!!\n")
elif(Name != "Jagdish") and (Age == 20) and (PvtCode == 1309):
    print("THE MASTER's Name is WRONGGGGG!!\n")
elif(Name == "Jagdish") and (Age != 20) and (PvtCode == 1309):
    print("Master's age is not correct! GET LOST NOWWWW!!!!\n")
else:
    print("Nothing's CORRECT!\n")
    

