#simple interest calculator 
#SI = (P*R*T)/100 here p=principal, r=rate, time = tenurity

principal = int(input("Enter the principal amount lended : "))
roi = float(input("Enter the ROI : "))
time = int(input("Enter the tenurity in months : "))

print(f"The Simple Interest Based upon Principal = {principal}, ROI = {roi} and tenurity = {time} will be : ", (principal*roi*time)/100)