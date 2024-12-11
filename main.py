# Enter your height in meters e.g., 1.55
height = float(input("What is your height in meters? "))

# Enter your weight in kilograms e.g., 72
weight = int(input("What is your weight in kilograms? "))

# Calculat BMI (weight / height^2)
bmi = (weight / (height ** 2))
print(bmi)

# Solution #1 to handle conditions:
# if bmi >= 35:
#   print(f"Your BMI is {bmi}, you are clinically obese.")
# elif bmi >= 30:
#   print(f"Your BMI is {bmi}, you are obese.")
# elif bmi >= 25:
#   print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi >= 18.5:
#   print(f"Your BMI is {bmi}, you have a normal weight.")
# else:
#   print(f"Your BMI is {bmi}, you are underwight.")

# Solution #2 (provided as answer - more elegant code:
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underwight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

