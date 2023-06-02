class A:
    def fun(self):
        print("A has fun")

class B(A):
    def fun(self):
        print("B has fun")

class C(A):
    def fun(self):
        print("C has fun")

class D(A):
    def fun(self):
        print("D has fun")

class E(C, D, B):
    pass

e = E()
e.fun()