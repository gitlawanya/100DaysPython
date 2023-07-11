print("Welcome to Love Calculator")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

combined_name = str(name1 + name2).lower()
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

count = t + r + u + e    #Counting each alphabet of true in combined name

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

count2 = l + o + v + e   #Counting each alphabet of love in combined name

love_score = str(count) + str(count2)   #Making two digit score out of individual counts

if int(love_score) < 10 or int(love_score) > 90:
    print(f"Your score is {love_score}, you go together like coke & mentos")
elif 40 <= int(love_score) <= 50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")



