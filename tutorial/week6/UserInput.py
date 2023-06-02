
def addition(a, b):
    return a + b


def subtruction(a, b):
    return a-b


def multp(a, b):
    return a*b


def division(a, b):
    return a/b


def operation(a, b):
    # arr = [a*b, a+b, a-b, a/b]
    # return arr
    return a+b, a*b, a-b


numb1 = int(input("Enter first number: "))
numb2 = int(input("Enter second number: "))

add = addition(numb1, numb2)
sub = subtruction(numb1, numb2)
mul = multp(numb1, numb2)
div = division(numb1, numb2)

# arr = operation(numb1, numb2)
a, b, c = operation(numb1, numb2)

# print("Add: %i" %(add))
# print("subtruction: ", sub)
# print("multp: ", mul)
# print("division: ", div)
print(a, b, c)

# for x in arr:
#     print(x)
