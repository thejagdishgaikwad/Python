Name = input("Enter Your Name :")
Age = int(input("Enter Your Age :"))

if(Age>=20):
    print("Do Your Have Driving License> (Y/N) :")
    license = input("Enter Y/N :")
    if(license == "Y"):
        print("EXCELLENT!, ", Name)
    elif(license == "N"):
        print("Try Getting Driving License!, All the BEST",Name)
    else:
        print("Invalid Entry!, TRY AGAIN!",Name)
elif(20>Age >15):
    print("You are Eligible for Learner's License,",Name)
else:
    print("GROW UP", Name)