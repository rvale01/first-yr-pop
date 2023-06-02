f = open("d:\Rakib\PythonCode\Python programming\lecture10\input-int.txt", "r") 
f2 = open(r"d:\Rakib\PythonCode\Python programming\lecture10\target-file.txt", "w")

# Reading from the file 
content = f.readlines() 
  
# Varaible for storing the sum 
sum = 0
# Varaible for storing the numbers 
value = []
  
# Iterating through the content of the file and storing into the array value
for line in content:    
    for i in line: 
        if i.isdigit():               
         value.append(int(i))
        
for i in value:
    sum = sum + i

f2.write("The sum is: ")
f2.write(str(sum)) 
f.close()
f2.close()