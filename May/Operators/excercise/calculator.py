#trying to create a simple calculator

A = float(input(""))
B = float(input(""))
operation = input(("Operation of choice? +, -, *, / : "))

if(operation == '+'):
    print("Addition : ", A+B)
elif(operation == '-'):
    print("Subtraction : ", A-B)
elif(operation == '/'):
    print("Diviion : ", A/B)
elif(operation == '*'):
    print("Multiplication : ", A*B)
else:
    print("INVALID ENTRY!\n")