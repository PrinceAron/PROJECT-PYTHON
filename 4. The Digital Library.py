def find_book():
    # Dictionary of books (Key: Title, Value: Author)
    library = {
        "The Great Gatsby": "F. Scott Fitzgerald",
        "1984": "George Orwell",
        "To Kill a Mockingbird": "Harper Lee",
        "The Hobbit": "J.R.R. Tolkien"
    }
##
##
##asdasd
    # User input
    title = input("Enter the book title: ").title().replace("A", "a")
    # Lookup using .get() to handle missing keys gracefully
    author = library.get(title)

    if author:
        print(f"Written by {author}")
    else:
        print("Book not found in the library.")

# Call the function
find_book()
