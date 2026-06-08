# employee record
employee_ids = [23, 24, 25, 26,27,28,29,30]

eid = int(input("Enter Employee ID: "))

if eid in employee_ids:
    print("Employee Record Available")
else:
    print("Employee Record Not Available")