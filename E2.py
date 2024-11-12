num = int(input("Enter a no : "))
no_of_digits = len(str(num))
sum_of_powers = 0
temp = num

while temp > 0 :
    digit = temp % 10
    sum_of_powers += digit ** no_of_digits
    temp //=10

if num == sum_of_powers:
    print(num, "is an armstrong no!\n")
else :
    print(num, "is not an armstrong no!\n")