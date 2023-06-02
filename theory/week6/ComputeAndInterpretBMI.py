KILOGRAMS_PER_POUND = 0.4535923
METERS_PER_INCH = 0.0254

weight = float(input("Input the weight in pounds: "))
height = float(input("Input the weight in inches: "))

weightInKg = weight * KILOGRAMS_PER_POUND
heightInMeaters = height * METERS_PER_INCH

bmi = weightInKg/(heightInMeaters * heightInMeaters)

print("Bmi is %.2f " % (bmi))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25: 
    print("Normal")
elif bmi<38:
    print("Overweight")
else:
    print("Obese")
