string_= input("Enter String :")
print("This is the string,",string_, "now put -ve indices for slicing as per your convenience!")

start_in = int(input("Enter -ve start index :"))
end_in = int(input("Enter -ve end index :"))

print("The string after slicing :", string_[start_in:end_in:-1])