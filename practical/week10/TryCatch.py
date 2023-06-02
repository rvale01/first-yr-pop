def input_numbers():
    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))

    try:
        print(f"{a} / {b} is {a/b}")
    except ZeroDivisionError as exp:
        print(exp)
        print("\nCannot divide by zero\n")
        input_numbers()


def read_mark():
    mark = int(input("Enter your POP In-class tests mark: "))
    if mark < 0 or mark > 500:
        raise ValueError("Invalid mark")

    return mark


try:
    a = ['a', 'b', 'c']
    print(a[0])
except LookupError:
    print("Index Error Exception: list index out of range")
else:
    print("No error!")

try:
    val = read_mark()
    print(f"Your mark is {val}")
except ValueError as e:
    print(e)

