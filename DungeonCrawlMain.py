# Import necessary modules
import random
import sys
# Define some variables for the game
max_hp = 20
C = 0

def drawroom():
    print("  _____________   ")
    print("  |           |   ")
    print("  |           |   ")
    print("  |   _____   |   ")
    print("  |   |   |   |   ")
    print("  |___|___|___|   ")
    print("  /           \   ")
    print(" /             \  ")
    print("/_______________\ \n")  

def generateroom():
    drawroom()
    C = random.randint(1,3)
    if C == 1:
        print("It is a stone room \n")
    elif C == 2:
        print("It is a wood room \n")
    else:
        print("It is a brick room \n")

# Start the game
print("You are in a dungeon and encounter a monster!")

# Keep playing until the player defeats 10 monsters or is defeated
while True:
    generateroom()
    monster_hp = random.randint(1, max_hp)
    player_hp = max_hp
    
    while monster_hp > 0 and player_hp > 0:
        # Print the current status of the game
        print(f"Player HP: {player_hp}, Monster HP: {monster_hp}")
    
        # Let the player choose to attack, flee, or heal
        action = input("Do you want to [A]ttack, [F]lee, or [H]eal? > ")
    
        # Attack the monster
        if action.lower() == "a":
            print("You attack the monster! \n")
            monster_hp -= random.randint(1, 5)
        
            # Check if the monster is still alive
            if monster_hp <= 0:
                print("You have defeated the monster! \n")
            else:
                print("The monster attacks you!")
                player_hp -= random.randint(1, 5)
        elif action.lower() == "f":
            print("You flee from the dungeon! \n")
            print("The End!")
            exit()
        elif action.lower() == "h":
            print("You heal yourself!")
            player_hp += random.randint(1, 5)
        else:
            print("Invalid action, try again. \n")
        
    # Check if the player is still alive
    if player_hp <= 0:
        print("You have been defeated by the monster! \n")
        break
    else:
        print("You have successfully defeated the monster and can continue fighting. \n")
