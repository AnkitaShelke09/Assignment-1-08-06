 #Student marks calculation

print("Enter 5 subjects: ")
subject1=input("Enter subject 1: ")
subject2=input("Enter subject 2: ")
subject3=input("Enter subject 3: ")
subject4=input("Enter subject 4: ")
subject5=input("Enter subject 5: ")

mark1=float(input(f"Enter marks for {subject1}: "))
mark2=float(input(f"Enter marks for {subject2}: "))
mark3=float(input(f"Enter marks for {subject3}: "))
mark4=float(input(f"Enter marks for {subject4}: "))
mark5=float(input(f"Enter marks for {subject5}: "))

Total=mark1+mark2+mark3+mark4+mark5
print(Total)
Averagemarks=Total/5
print("Average Marks: ",Averagemarks)
print("percentage:",(Total/500*100))