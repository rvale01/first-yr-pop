class Sum:
    # a = 0
    # b = 0
    # c = 0

    # def __init__(self):
    #     se
        # self.a = a
        # self.b = b
        # self.c = c

    # def sumFunction1(self, a, b, c):
    #     return a + b + c

    def sumFunction2(self):
        a = int(input("num. 1: "))
        b = int(input("num. 2: "))
        c = int(input("num. 3: "))
        return a + b + c
    
    # def sumFunction3(self):
    #     a = 3
    #     b = 1
    #     c = 8
    #     return a + b + c

    
sum1 = Sum()
sum2 = Sum()

# sum1 = Sum(3, 4, 5)
# sum2 = Sum(0, 0, 0)

# print("Sum 1: ", sum1.sumFunction2())
# print("Sum 2: ", sum2.sumFunction1(1, 2, 3))
# print("Sum 3: ", sum1.sumFunction3())

print("Sum 1: ", sum1.sumFunction2())
print("Sum 2: ", sum2.sumFunction2())
