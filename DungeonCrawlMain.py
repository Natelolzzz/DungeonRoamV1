# Import necessary modules
import random

# Define some variables for the game
max_hp = 20
random_num = 0

#Function definitions


def drawroom():
  print("   +----------+.        ")
  print("   |   ____   | `.      ")
  print("   |  /    \  |   `.    ")
  print("   |  |    |  |     +   ")
  print("   +--|----|--+.    |   ")
  print("    `.          `.  |   ")
  print("      `.          `.|   ")
  print("        `+----------+ \n")


def generateroom():
  drawroom()
  random_num = random.randint(1, 3)
  if random_num == 1:
    print("It is a stone room \n")
  elif random_num == 2:
    print("It is a wood room \n")
  else:
    print("It is a brick room \n")


# Start the game
print("You are in a dungeon and encounter a monster! \n")

player_hp = max_hp

# Keep playing

while True:
  #start generation
  generateroom()
  monster_hp = random.randint(1, max_hp)

  while monster_hp > 0 and player_hp > 0:
    # Print the current status of the game
    print(f"Player HP: {player_hp}, Monster HP: {monster_hp} \n")

    # Let the player choose to attack, flee, or heal
    action = input("Do you want to [A]ttack, [F]lee, or [H]eal? > ")

    # Attack the monster
    if action.lower() == "a":
      print("\nYou attack the monster! \n")
      monster_hp -= random.randint(1, 5)

      # Check if the monster is still alive
      if monster_hp <= 0:
        print("You have defeated the monster! \n")
      else:
        print("The monster attacks you!\n")
        player_hp -= random.randint(1, 5)
    #Healing commmand
    elif action.lower() == "h" and player_hp < 20:
      print("\nYou heal yourself! \n")
      heal_amount = random.randint(1, 5)
      #Prevent over heal
      if heal_amount + player_hp < 21:
        player_hp += heal_amount
      else:
        player_hp = 20
    #Can't heal test
    elif action.lower() == "h" and player_hp > 19:
      print("\nYou are at full health! \n")

    elif action.lower() == "f":
      break
    else:
      print("\nInvalid action, try again. \n")

  if action.lower() == "f":
    #Run!
    print("You fled in fear never to return!")
    break
  elif player_hp <= 0:
    # Check if the player is still alive
    print("You have been defeated by the monster! \n")
    break
  else:
    #or beat the monster
    print(
      "You have successfully defeated the monster and can continue fighting. \n"
    )
#Finish
print("The end!")
