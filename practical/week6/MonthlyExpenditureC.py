# Print monthly expenditure
# Practical 6, Part 2 (a)
# author your name

foodExpenses = float(input("\n Enter food expenses: "))
leisureExpenses = float(input("\n Enter leisure expenses: "))
accommodationExpenses = int(input("\n Enter accomodation expenses: "))
travelExpenses = int(input("\n Enter travel expenses: "))
clothesExpenses = float(input("\n Enter clothes expenses: "))
totalSpent = 0.0

totalSpent = foodExpenses + leisureExpenses + clothesExpenses + accommodationExpenses + travelExpenses

print("The total expenditure this month was: %f" %(totalSpent))
