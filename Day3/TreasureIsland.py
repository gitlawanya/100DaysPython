print('''Welcome to Treasure Island.
Your mission is to find the treasure.''')

question1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'\n")

if question1 == "right":
  
  question12 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")

  #Boat way
  
  if question12 == "wait":
    question13 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
    if question13 == "red":
      print("It's a room full of fire. Game Over!!")
    elif question13 == "yellow":
      print("You enter a room of beasts. Game Over!!")
    elif question13 == "blue":
      print("You found the treasure! You Win!")
    else:
      print("You chose a door that doesn't exist. Game Over! #No_room_for_typos.")

  #Swim way
  elif question12 == "swim":
    print("You were eaten by sea monsters. Game Over!!")

  else:
    print("Game Over!! #No_room_for_typos.")


elif question1 == "left":
  
  question2 = input("You're at a desert with no compass. Type 'continue' to explore desert or 'die' to commit suicide.\n")
  if question2 == "continue":
    question21 = input("You're still wandering. Type 'continue' to see what's next or 'die' to commit suicide.\n")
    if question21 == "continue":
      print("Seems you came the wrong way from the get go. You starve and die. Game Over!!")
    elif question21 == "die":
      print("You chose an easy death. Die Bitch!!")
    else:
      print("Game Over!! #No_room_for_typos.")
  elif question2 == "die":
    print("You chose an easy death. Die Bitch!!")
  else:
    print("Game Over!! #No_room_for_typos.")



else:
  print("Pay Attention!! Your game is already over! #No_room_for_typos.")