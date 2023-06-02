size = int(input("Enter the number of real numbers: "))

myList = [0]*(size)

print("Enter real numbers: ")
sum = 0
for x in range(size):
    myList[x] = int(input())
    sum += myList[x]

average = sum/size
count = 0
for x in myList:
    if x > average:
        count += 1


print("Average is %.2f" % average)
print("Number of real numbers above the average is %i" % count)
