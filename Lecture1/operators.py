OP1=10
OP2=5

#arithmetic operators
print(OP1+OP2) #addition
print(OP1-OP2) #subtraction
print(OP1*OP2) #multiplication
print(OP1/OP2) #division
print(OP1%OP2) #remainder
print(OP1**OP2) #OP1^OP2

#relational operators
print(OP1==OP2) #equal to equal to
print(OP1!=OP2) #not equal to
print(OP1>OP2) #greater than
print(OP1<OP2) #less than
print(OP1>=OP2) #greater than equal to
print(OP1<=OP2) #less than equal to

#assignment operators
OP1+=22 #OP1=OP1=22
print(OP1)
OP2-=8  #OP2=OP2-8
print(OP2)
OP1/=4  #OP1=OP1/4
print(OP1)
OP2*=2  #OP2=OP2*2
print(OP2)
OP1%=4  #OP1=OP1%4
print(OP1)
OP2**=2 #OP2=OP2**2
print(OP2)  

#Logical Operators
a=5
b=2

print("Not of (A>B) : ",not (a>b))
print("Not of (A<B)",not (a<b))
print("AND : ", (a>b) and (b>a))
print("Or :", (a>b) or (b>a))
