year = int(input("Which year do you want to check?"))

if year % 4 == 0:    #It should be cleanly divisible by 4
    if year % 100 == 0:  #Except if it's cleanly divible by 100
        if year % 400 == 0:   #Unless it's cleanly divisible by 400
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap year")
else:
    print("Not a Leap Year")
