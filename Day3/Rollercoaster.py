print("Welcome to the Rollercoaster")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    elif 45 <= age <= 55:  #Going through mid-life crisis
        bill = 0
        print("Ride fare is on us, please enjoy your time.")
    else:
        bill = 12

    wants_photo = input("Do you want a photo to be taken? y/n \n")
    if wants_photo == "y":
        bill += 3
        
    print(f"Your total bill is ${bill}")

else:
    print("You have to grow taller before you can ride")