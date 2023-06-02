#import traceback

def fun1():

    def fun2():

       # try:
            a = int(input("Enter first number:"))
            b = int(input("Enter second number:")) 
            print(f"{a} / {b} is {a/b}")

       # except ZeroDivisionError as exc:
       #     print(exc)
           # print("Class:", exc.__class__)

          #  for line in traceback.format_stack():
          #      print(line.strip())

    fun2()


def fun3():
    fun1()


fun3()