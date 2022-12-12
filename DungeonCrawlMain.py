# Import necessary modules
import random

# Define some variables for the game
max_monsters = 5
max_hp = 20

# Start the game
print("You are in a dungeon and encounter a monster!")

# Keep playing until the player defeats 10 monsters or is defeated
while True:
    monster_hp = random.randint(1, max_hp)
    player_hp = max_hp
    num_monsters_defeated = 0
    
    while monster_hp > 0 and player_hp > 0:
        # Print the current status of the game
        print(f"Player HP: {player_hp}, Monster HP: {monster_hp}")
    
        # Let the player choose to attack or flee
        action = input("Do you want to [A]ttack or [F]lee? ")
    
        # Attack the monster
        if action.lower() == "a":
            print("You attack the monster!")
            monster_hp -= random.randint(1, 5)
        
            # Check if the monster is still alive
            if monster_hp <= 0:
                print("You have defeated the monster!")
            else:
                print("The monster attacks you!")
                player_hp -= random.randint(1, 5)
        elif action.lower() == "f":
            print("You flee from the dungeon!")
            break
        else:
            print("Invalid action, try again.")
        
    # Check if the player is still alive
    if player_hp <= 0:
        print("You have been defeated by the monster!")
        break
    else:
        print("You can continue fighting monsters.")
