""" 
reversing a string in one line
def reverse(str):
    return str[::-1]

"""

def reverse(str):
    result = ""
    i = len(str) - 1
    while(i >= 0):
        result += str[i]
        i -= 1
    return result


print(reverse("hello"))

