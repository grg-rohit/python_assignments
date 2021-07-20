file = open("oliver.txt", "rt") # r -read t- text mode

data = file.read()
words = data.split()

print("Total number of words in oliver.txt: ", len(words))

