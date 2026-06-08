#Loan eligibility checker

name = input("Enter your name: ")
is_job=input("Do you have a job(Y/N):")
bank_bal=float(input("Enter your bank balance: "))

if is_job=="Y" and bank_bal>700000:
    print("You are eligible for loan")

else:
    print("You are not eligible for loan")