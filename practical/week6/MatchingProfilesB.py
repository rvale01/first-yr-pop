def checkSuspect(one, two):
    b = True
    for x in range(10):
        if suspec1[x] != suspec2[x]:
            b = False
        break

    return b


suspec1 = []
suspec2 = []

# read from keyboard suspec 1
print("First suspect")
for x in range(10):
    dna = float(input())
    suspec1.append(dna)

# read from keyboard suspect 2
print("Second suspect")
for x in range(10):
    dna = float(input())
    suspec2.append(dna)

b = checkSuspect(suspec1, suspec2)

if(b == True):
    print("DNAs match")
else:
    print("DNAs do not match")
