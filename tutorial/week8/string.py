def printString(string):
    if(string.isupper()):
        print(string.lower())
    else:
        print(string.upper())

def getString():
    string = input("Input a string")
    return string

str = getString()
printString(str)