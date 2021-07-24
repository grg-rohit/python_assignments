booksInLibrary = ['alice', 'history', 'hitler', 'oldman', 'oliver', 'pi_million_digits', 'siddartha','text', ]

userChoice = input("Enter the name of a book: ")

path = userChoice + ".txt"
try:
    with open(path, 'r') as book:
        first_line = book.readline()
        print(first_line)
        book.close()
    
except FileNotFoundError:
    msg = "Sorry, the book " + userChoice + " is not available in the library."
    print(msg)



    