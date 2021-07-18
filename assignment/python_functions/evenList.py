def evenList(List):
    newList = []
    for element in List:
        if element % 2 == 0:
            newList.append(element)
            newList.sort()
    return newList

userList = [1, 2, 3, 3, 4, 5, 5, 6]

print(evenList(userList))