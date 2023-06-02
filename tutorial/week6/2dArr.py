def checkSuspect(one, two):
    for x in range(2):
        b = True
        for y in range(10):
            if(one[y]!=two[x][y]):
                b = False
                break
        if b:
            return b, x
    return False, -1


suspec1 = [] * 10
suspec2 = [] * 2

# read from keyboard suspec 1
print("First suspect")
for x in range(10):
    dna = float(input())
    suspec1.append(dna)

# read from keyboard suspect 2
print("Second suspect")
for x in range(2):
    temp = [0]*10
    print("dna n.%i" % (x))
    for y in range(10):
        dna = float(input())
        temp[y] = dna
    suspec2.append(temp)


b, x = checkSuspect(suspec1, suspec2)

if(b == True):
    print("DNA is match with suspect n.%i" %(x+1))
else:
    print("DNA does not match")
