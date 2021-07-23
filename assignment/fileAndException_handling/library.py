booksInLibrary = ['alice', 'history', 'hitler', 'oldman', 'oliver', 'pi_million_digits', 'siddartha','text', ]

userChoice = input("Enter the name of a book: ")

path = userChoice + ".txt"
try:
    with open(path) as book_obj:
        contents = book_obj.read()
        print(contents)
except FileNotFoundError:
    msg = "Sorry, the book " + userChoice + "is not available in the library."
    print(msg)

    