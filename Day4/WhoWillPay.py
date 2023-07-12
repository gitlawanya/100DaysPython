import random

names_string = input("Give me everybody's name, separated by a comma. ")
names = names_string.split(", ")

num_items = len(names)
random.choice = random.randint(0, num_items - 1)
payer = names[random.choice]

print(f"The person who will pay the bill is {payer}")
