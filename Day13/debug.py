#1

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    #b_list.append(new_item)
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])



#2

number = int(input("Which number do you want to check for even or odd?"))

#if number % 2 = 0:
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")



#3

#year = input("Which year do you want to check?")
year = int(input("Which year do you want to check for leap or not?"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
  print("Not leap year.")


#4

for number in range(1, 101):
    #if number % 3 == 0 or number % 5 == 0:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
        print([number])