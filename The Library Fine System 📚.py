# The Library Fine System 📚 50
#
#make it green

restricted_books = ["necronomicon", "forbidden spells", "unauthorized history"]
library_patrons = []

for i in range(2):
    partons = {}
    partons["name"] = input("What is your name dear sir/maam: ")
    stored_books = []
    for x in range(3):
        book = input(f"please enter book {x+1}: ").lower().strip()
        stored_books.append(book) # I did not put this before MISTAKE
        partons["storedBooks"] = stored_books # and add the empty list
    library_patrons.append(partons)

for Validation in library_patrons:
    validaty = True

    for check in Validation["storedBooks"]:
        if check in restricted_books:
            validaty = False
            break
#         else:
#             validaty = True  # Still working but not necessary 

    if validaty:
        Validation["status"] = "ACCEPTED"
        Validation["fine"] = 0
    else: # don't for got add else only
        Validation["status"] = "REJECTED"
        Validation["fine"] = 100


for final in library_patrons:
        print(final)