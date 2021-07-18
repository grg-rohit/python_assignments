def unique(List):
    newList = []
    for element in List:
        if element not in newList:
            newList.append(element)
            newList.sort()
    return newList

userList = [1, 2, 3, 3, 4, 5, 5, 6]

print(unique(userList))