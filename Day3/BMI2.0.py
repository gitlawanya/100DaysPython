height = float(input("Enter your height in metres: "))
weight = float (input("Enter your weight in kgs: "))

bmi = round(weight / (height**2))

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, your weight is normal")
elif bmi < 30:
    print(f"Your bmi is {bmi},you are overweight")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese")
else:
    print(f"Your bmi is {bmi}, you are clinically obese")