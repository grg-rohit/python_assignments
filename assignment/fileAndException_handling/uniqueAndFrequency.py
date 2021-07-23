import string

text = open("oldman.txt", "r")

UniqueWords = dict() # creates an empty ditionary called new

for line in text:

    line = line.strip()

    line = line.lower()

    #Removing the punctuation marks from the line
    line = line.translate(line.maketrans("", "", string.punctuation))

    # Split the line into words
    words = line.split(" ")

    for word in words: 
        if word in UniqueWords:
            UniqueWords[word] = UniqueWords[word] + 1
        else:
            UniqueWords[word] = 1

for key in UniqueWords.keys():
    print(key, ":", UniqueWords[key])

 