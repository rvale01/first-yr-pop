try:
    f = open("myFie.txt", "r")
    f2 = open("yourFile.txt", "w")
    line = f.read
    y = 0
    for x in f:
        # if(y == 0)
        if(y == 1):
            line = x
        y += 1
    f2.write(line)
    f.close()   
    f2.close()
except FileNotFoundError:
    print("One of the files was not found")
else:
    print("No error!")
