A = int(input("Enter A : "))
B = int(input("Enter B : "))
C = int(input("Enter C : "))
D = int(input("Enter D : "))

expn = (A+C)**B+D-A*(D/A)**C
print(f"Solution for {A} , {B}, {C}, and {D} is :", expn) #Accpoding to PEMDAS (Parentheses>>Exponent>>Multiplication>>Division>>Addition>>Subtraction)
