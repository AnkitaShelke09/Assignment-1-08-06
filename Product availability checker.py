# Product checker

products = ["BMW", "Honda", "Maruti Suzuki", "Kia"]

item = input("Enter product name: ")

if item in products:
    print("Product is available")
else:
    print("Product is not available")