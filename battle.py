import random

from utils import *
from pokemon_types import type_chart, type_attacks

def hp_bar(current, maximum, length=20):
    filled = int((current / maximum) * length)
    empty = length - filled

    percent = current / maximum

    if percent > 0.6:
        color = color_green
    elif percent > 0.3:
        color = color_yellow
    else:
        color = color_red

    return color + "█" * filled + "░" * empty + color_reset

def reset_team(team):
    for p in team:
        p.hp = p.max_hp


def team_battle(playerteam, enemy_team):
    
    reset_team(playerteam)
    reset_team(enemy_team)

    if len(playerteam) == 0:
     print("No Pokemon in team!")
     return

    p_index = 0
    e_index = 0
    turn = 1

    p1 = playerteam[p_index]
    p2 = enemy_team[e_index]

    typewriter(f"\n Battle starts!",0.03)
    typewriter(f"You send out {p1.name}!",0.03,color_blue)
    typewriter(f"Enemy sends out {p2.name}!\n",0.03,color_red)

    while True:
        #team_battle(playerteam, enemyteam)
        print("\n===================")
        print("TURN", turn)
        print("===================")

        print(color_blue + f"\nYOU: {p1.name}" + color_reset)
        print(f"{hp_bar(p1.hp, p1.max_hp)} {p1.hp}/{p1.max_hp}")

        print(color_red + f"\nENEMY: {p2.name}" + color_reset)
        print(f"{hp_bar(p2.hp, p2.max_hp)} {p2.hp}/{p2.max_hp}")

        print("\nWhat do you want to do?")
        print("1 - Attack")
        print("2 - Switch Pokemon")

        try:
          action = int(input("> "))
        except ValueError:
            print("Please enter a number!")
            continue

# ================= ATTACK =================
        if action == 1:

            moves = type_attacks[p1.type]

            print("\nChoose your move:")
            for i, move in enumerate(moves):
                print(f"{i+1} - {move[0]} (+{move[1]})")

            while True:
                try:
                    choice = int(input("> ")) - 1
                except ValueError:
                    print("Please enter a number!")
                    continue

                if 0 <= choice < len(moves):
                    break

                print("Invalid move!")

            move_name, bonus = moves[choice]

            multiplier = type_chart.get(p1.type, {}).get(p2.type, 1)

            damage = (p1.attack + bonus - p2.defense) * multiplier
            damage = max(1, int(damage))

            p2.hp = max(0, p2.hp - damage)

            typewriter(f"\n{p1.name} used {move_name}!", 0.03, color_blue)
            typewriter(f"It dealt {damage} damage!", 0.03, color_blue)

            if multiplier == 2:
                typewriter(color_light_blue + "It's super effective!" + color_reset, 0.03)
            elif multiplier == 0.5:
                typewriter(color_orange + "It's not very effective..." + color_reset, 0.03)
        # ================= SWITCH =================
        elif action == 2:

            cancelled = False

            print(color_yellow + "\nChoose Pokemon to switch:" + color_reset)

            valid_indexes = []

            for i, p in enumerate(playerteam):
                if p.hp > 0:
                    valid_indexes.append(i)
                    print(f"{i+1} - {p.name} (HP: {p.hp})")

            print("0 - Cancel")

            while True:
                try:
                    switch = int(input("> "))
                except ValueError:
                    print("Please enter a number!")
                    continue

                if switch == 0:
                    cancelled = True
                    print("Cancelled.")
                    break

                switch -= 1

                if switch not in valid_indexes:
                    print("Invalid switch!")
                    continue

                if playerteam[switch] == p1:
                    print("This Pokemon is already battling!")
                    continue

                p1 = playerteam[switch]
                print(f"\nGo {p1.name}!")
                break

            if cancelled:
                continue
        # ================= ENEMY DEAD =================
        if p2.hp <= 0:

            print(f"\n{p2.name} fainted!")

            e_index += 1

            #  SKIP DEAD ENEMY POKEMON
            while e_index < len(enemy_team) and enemy_team[e_index].hp <= 0:
                e_index += 1

            if e_index >= len(enemy_team):
                print(color_green + "\n YOU WIN THE BATTLE!" + color_reset)
                return True

            p2 = enemy_team[e_index]
            print(f"\nEnemy sends out {p2.name}!")
            
            turn += 1
            continue
        # ================= ENEMY ATTACK =================
        if p2.hp > 0:

            enemy_moves = type_attacks[p2.type]
            enemy_move_name, enemy_bonus = random.choice(enemy_moves)

            enemy_multiplier = type_chart.get(p2.type, {}).get(p1.type, 1)

            enemy_damage = (p2.attack + enemy_bonus - p1.defense) * enemy_multiplier
            enemy_damage = max(1, int(enemy_damage))



            typewriter(f"\nEnemy {p2.name} used {enemy_move_name}!", 0.03, color_red)
            typewriter(f"It dealt {enemy_damage} damage!", 0.03, color_red)
            p1.hp = max(0, p1.hp - enemy_damage)

            if enemy_multiplier == 2:
             print(color_light_blue + "It's super effective!" + color_reset)

            elif enemy_multiplier == 0.5:
                print(color_orange + "It's not very effective..." + color_reset)

        # ================= PLAYER DEAD =================
        if p1.hp <= 0:

            print(f"\n{p1.name} fainted!")

            alive = [p for p in playerteam if p.hp > 0]

            if not alive:
                print(color_red + "\n YOU LOST THE BATTLE!" + color_reset)
                return False

            print("\nChoose your next Pokemon:")

            while True:
                for i, p in enumerate(playerteam):
                    if p.hp > 0:
                        print(f"{i+1} - {p.name} (HP: {p.hp})")

                try:
                    choice = int(input("> ")) - 1
                except ValueError:
                    print("Please enter a number!")
                    continue

                if 0 <= choice < len(playerteam) and playerteam[choice].hp > 0:
                    p1 = playerteam[choice]
                    print(color_blue,f"\nGo {p1.name}!",color_reset)
                    break

                print("Invalid choice!")
        turn += 1

