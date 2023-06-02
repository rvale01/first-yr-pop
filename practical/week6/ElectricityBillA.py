# Electricity bill
# Practical 6, Part 3
# author your name

# Enter previous meter reading
previousMeterReading = int(input("\nEnter previous meter reading: "))
# Enter current meter reading
currentMeterReading = int(input("\nEnter current meter reading: "))
# Enter the day of the meter reading
dayReading = int(input("Enter the day of the meter reading: "))
# Enter the month of the meter reading
monthReading = int(input("Enter the month of the reading: "))
# Input Validation
# previous meter reading within range 0..9999
if previousMeterReading < 0 or previousMeterReading > 9999:
    print("Error: previous meter reading out of range \n")

# previous not greater than present
if(previousMeterReading > currentMeterReading):
    print("Error: previous meter more than present \n")

# electricity used not more than 1000
if((previousMeterReading - currentMeterReading) > 1000):
    print("Error: electricity used more than 1000")

# month in range 1..12
if(monthReading > 12 or monthReading < 1):
    print("Error: month out of range")

# days in month must be correct (Jan, March etc) #days in month must be correct (Apr, June etc)
if(monthReading == 1 or monthReading == 3 or monthReading == 5 or monthReading == 7 or monthReading == 8 or monthReading == 10 or monthReading == 12):
    if(dayReading > 31 or dayReading < 1):
        print("Error: day out of range")

if(monthReading == 11 or monthReading == 4 or monthReading == 6 or monthReading == 9):
    if(dayReading > 30 or dayReading < 1):
        print("Error: day out of range")
# days in month must be correct (Feb assuming 29 days)
if(monthReading == 2):
    if(dayReading < 1 or monthReading > 29):
        print("Error: day out of range")

else:
    print("All good")