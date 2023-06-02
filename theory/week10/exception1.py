a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
# try:
#   print(f"{a} / {b} is {a/b}")
# except:
#   print("Some exception caught")

# try:
#   print(f"{a} / {b} is {a/b}")
# except ZeroDivisionError:
#   print("Caught ZeroDivisionError")


# try:
#   print(f"{a} / {b} is {a/b}")
# except TypeError:
#   print("Caught TypeError")
# except ZeroDivisionError:
#   print("Caught ZeroDivisionError")


# try:
#   print(f"{a} / {b} is {a/b}")
# except (TypeError, ZeroDivisionError):
#   print("Caught TypeError OR ZeroDivisionError")

# try:
#   print(f"{a} / {b} is {a/b}")
# except Exception as exc:
#   print(exc)

try:
  print(f"{a} / {b} is {a/b}")
except ZeroDivisionError as exc:
  print(exc)

# try:
#   print(f"{a} / {b} is {a/b}")
# except (TypeError, ZeroDivisionError) as exc:
#   print(exc)


# try:
#   print(f"{a} / {b} is {a/b}")
# except TypeError:
#   print("Caught TypeError")
# except:
#   print("Some exception caught")



# try:
#   print(f"{a} / {b} is {a/b}")
# except TypeError:
#   print("Caught TypeError")
# except:
#   print("Some exception caught")
# else:
#   print("NO exception!")


try:
  print(f"{a} / {b} is {a/b}")
except TypeError:
  print("Caught TypeError")
except:
  print("Some exception caught")
else:
  print("NO exception!")
finally:
  print("Resource released")