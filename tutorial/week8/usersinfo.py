class Infos:
    phone: []
    address: ""

    def getInput(self, phone, address):
        self.phone = phone
        self.address = address

    def display(self):
        print("Address: ", self.address)
        print("Number/s: ")
        for x in self.phone:
            print(x)

    def storeInput(self, phone, address):
        self.getInput(phone, address)
        self.display()


add = str(input("Input the address: "))

isNumb = True
x = 0
numb = []

while(isNumb):
    numb.append(int(input("Input a number")))
    if(x >= 1):
        isNumb = False
    else:
        x += 1
        ans = str(input("Do you want to add a new number? y or n"))
        if(ans == "n"):
            isNumb = False

user1 = Infos()
user1.storeInput(numb, add)
