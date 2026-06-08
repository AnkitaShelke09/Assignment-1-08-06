#Library Book Search

books = ["Python", "C", "C++", "AI/ML"]

book = input("Enter book name: ")

if book in books:
    print("Book available in library")
else:
    print("Book not available")