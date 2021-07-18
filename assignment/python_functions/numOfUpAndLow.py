userString = input("Enter a string: ")

def caseCheck(strings):
    uCount = 0
    lCount = 0
    for letter in strings:
        if letter.isupper(): 
            uCount += 1
        if letter.islower():
            lCount += 1
    display = print("num of uppercase: ", uCount,"\n", "num of lowercase: ", lCount)
    return display

caseCheck(userString)