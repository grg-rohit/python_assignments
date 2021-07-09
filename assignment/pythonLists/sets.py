A = ['a', 'b', 'c', 'd']
B = ['1', 'a', '2', 'b']

def setUnion(x,y):
    unionList = list(set().union(x, y))
    unionList.sort()
    return unionList

def setIntersection(x, y):
    intersectionList = list(set(A).intersection(B))
    intersectionList.sort()
    return intersectionList

print("A union B : ", setUnion(A, B))

print("A intersection B: ", setIntersection(A, B))