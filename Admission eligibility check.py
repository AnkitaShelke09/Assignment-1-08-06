# Admission eligibility check

name=input("Enter student name: ")
perc=float(input("Enter percent of student: "))
if perc>=80 and perc<=100:
    print("You are eligible for admission")
else:
    print("You are not eligible for admission")