import winsound
import random
from utils import *
from pokemon import Pokemon
from data import Pokemon_data
from battle import team_battle
from trainers import get_enemy
from pokemon_types import type_chart, type_attacks

playerteam = []

print(color_red,"  _____   ____  _  ________ __  __  ____  _   _                       ",color_reset)
print(color_red," |  __ \ / __ \| |/ /  ____|  \/  |/ __ \| \ | |                      ",color_reset)
print(color_red," | |__) | |  | | ' /| |__  | \  / | |  | |  \| |                      ",color_reset)
print(color_red," |  ___/| |  | |  < |  __| | |\/| | |  | | . ` |                      ",color_reset)
print(color_red," | |    | |__| | . \| |____| |  | | |__| | |\  |                      ",color_reset)
print(color_red," |_|     \____/|_|\_\______|_|  |_|\____/|_| \_|_ _ _   _             ",color_reset)
print(color_green,"              | | | |                          | (_) | (_)            ",color_reset)
print(color_green,"   _ __  _   _| |_| |__   ___  _ __     ___  __| |_| |_ _  ___  _ __  ",color_reset)
print(color_green,"  | '_ \| | | | __| '_ \ / _ \| '_ \   / _ \/ _` | | __| |/ _ \| '_ \ ",color_reset)
print(color_green,"  | |_) | |_| | |_| | | | (_) | | | | |  __/ (_| | | |_| | (_) | | | |",color_reset)
print(color_green,"  | .__/ \__, |\__|_| |_|\___/|_| |_|  \___|\__,_|_|\__|_|\___/|_| |_|",color_reset)
print(color_green,"  | |     __/ |                                                       ",color_reset)
print(color_green,"  |_|    |___/                                                        ",color_reset)
print("                                                                      ")
 
typewriter("Welcome to our Pokemon World ",0.07)
name=input("What is your name ")
typewriter("Nice to meet you "+ name +" My name is Proffesor X",0.07)
typewriter("In this world you need to select 4 pokemon for your team ",0.07)
typewriter("You are in a tournament and try to win against Last Champion Ege",0.07)
typewriter("You can choose this 40 pokemons for your team")
time.sleep(1)
 
 
print("\nAvailable Pokemon:\n")

for i, p in Pokemon_data.items():
    print(f"{i:02d} - {p.name:<12} {p.type:<9} HP:{p.hp:<3} ATK:{p.attack:<2} DEF:{p.defense:<2}")
    
while len(playerteam) < 4:
    try:
        choice = int(input("Which pokemon do you want 1-40: "))
    except ValueError:
        print("Enter a number!")
        continue

    if choice not in Pokemon_data:
        print("Invalid choice!")
        continue

    selected = Pokemon_data[choice].clone()

    if any(p.name == selected.name for p in playerteam):
     print("You already chose this Pokemon!")
     continue

    playerteam.append(selected)

    print(selected.name, "added to your team!")
    print("Current team:", [p.name for p in playerteam])


typewriter("Nice team good luck...", 0.07)

# rakip AI

enemyteam = random.sample(list(Pokemon_data.values()), 4)
battle_count = 0

while battle_count < 4:
    print("\n===== TOURNAMENT =====")

    for i in range(1, 5):
        if i <= battle_count:
            print(f"Round {i}: ✓")
        elif i == 4:
            print("Champion Battle")
        else:
            print(f"Round {i}")

    print("======================")

    enemy_name, enemyteam = get_enemy(battle_count)

    print(f"\nYour opponent: {enemy_name}")

    won = team_battle(playerteam, enemyteam)

    if enemy_name == "Champion Ege" and won:
        typewriter("Congratulations! You are the new Champion!", 0.07)
        break

    if not won:
        typewriter("Game Over!", 0.07)
        break

    battle_count += 1