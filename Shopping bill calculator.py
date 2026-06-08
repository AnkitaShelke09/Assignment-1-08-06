# shopping bill calculator
number = int(input("Enter the number of items: "))
Total_bill = 0
for i in range(number):
    item = input(f"Enter the item {i + 1}: ")
    price = float(input(f"Enter the price of {item}: "))
    Total_bill += price
print(f"Total Bill: {Total_bill}")