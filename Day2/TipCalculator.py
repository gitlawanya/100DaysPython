print("Welcome to the tip calculator")
bill = float(input("What was your total bill amount? $"))
tip = int(input("What percentage would you like to give as tip? 10, 12 or 15? "))
split = int(input("How many people to split the bill? "))

bill_with_tip = bill * (1 + (tip/100))
bill_upon_splitting = round((bill_with_tip/split), 2)
print(f"Each person should pay ${bill_upon_splitting}")

