# Display 1-9 Multiplication Table
# Compare with MultiplicationTable.c from Week 3

print("Multiplication table")

# Display column headings 1 to 9
print("    ", end = "")
for j in range(1,9):
    print(j, end="    ")

print ("\n      -------------------------------------------")
for x in range(1,10):
    print("%i |  " %x, end = " ")
    for y in range(1,10):
        print("%i" %(y*x), end=" ")
    print("\n")