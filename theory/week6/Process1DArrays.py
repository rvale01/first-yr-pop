f = open("mylist_input.txt", "rt")

size = 10
myList = [0]*size

print("Read %i values from a file: " % size)

# read the file into an array of strings (separate data items by space)

arrayList = f.read().split(" ")
f.close()

counter = 0
while counter < 10:
    myList[counter] = float(arrayList[counter])
    counter += 1

total = 0
max = 0.0

for value in myList:
    total += value
    if max < value:
        max = value
    print("%.2f " %value)

print()
print(f'The total is {total}')
print(f'The max is {max}')
