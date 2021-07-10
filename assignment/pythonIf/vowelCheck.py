userInput = input("Enter an alphabet: ")[0]
alph = userInput.upper()

if alph == "A" or alph == "E" or alph == "I" or alph == "O" or alph == "U":
    print("Given alphabet {} is vowel".format(userInput)) 
else:
    print("Given alphabet {} is consonant".format(userInput))  
