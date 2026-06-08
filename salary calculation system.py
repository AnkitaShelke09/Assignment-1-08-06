n = int(input("Enter Number of Employees: "))

for i in range(n):
    print("\nEmployee", i + 1)

    basic = float(input("Enter Basic Salary: "))

    hra = basic * 0.15
    da = basic * 0.08

    gross = basic + hra + da

    deduction = gross * 0.05

    net = gross - deduction

    print("Gross Salary =", gross)
    print("Deduction =", deduction)
    print("Net Salary =", net)