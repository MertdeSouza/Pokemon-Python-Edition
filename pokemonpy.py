import time
import sys
import random
import json
import winsound



def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 

class Pokemon:

    def __init__(self, name, hp, attack, defense, type):
        self.name =name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.type = type
    def clone(self):
        return Pokemon(
            self.name,
            self.max_hp,
            self.attack,
            self.defense,
            self.type
        )


    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense

        if damage < 1:
            damage = 1

        enemy.hp -= damage

        print(f"{self.name} attacked {enemy.name}!")
        print(f"{enemy.name} lost {damage} HP!")
        print(f"{enemy.name} remaining HP: {enemy.hp}\n")


    




# data aralığı

Pokemon_data = {
    1: Pokemon("Charizard", 10000, 3000, 10, "Fire"),
    2: Pokemon("Arcanine", 110, 32, 12, "Fire"),
    3: Pokemon("Infernape", 95, 34, 9, "Fire"),
    4: Pokemon("Delphox", 90, 28, 10, "Fire"),

    5: Pokemon("Blastoise", 120, 25, 15, "Water"),
    6: Pokemon("Gyarados", 110, 33, 12, "Water"),
    7: Pokemon("Greninja", 95, 30, 10, "Water"),
    8: Pokemon("Vaporeon", 115, 27, 13, "Water"),

    9: Pokemon("Venusaur", 110, 28, 14, "Grass"),
    10: Pokemon("Sceptile", 95, 30, 10, "Grass"),
    11: Pokemon("Decidueye", 100, 29, 11, "Grass"),
    12: Pokemon("Rillaboom", 115, 32, 12, "Grass"),

    13: Pokemon("Scizor", 110, 35, 15, "Bug"),
    14: Pokemon("Heracross", 105, 34, 12, "Bug"),
    15: Pokemon("Volcarona", 100, 33, 10, "Bug"),
    16: Pokemon("Butterfree", 90, 25, 8, "Bug"),

    17: Pokemon("Gengar", 95, 35, 8, "Ghost"),
    18: Pokemon("Mimikyu", 100, 30, 10, "Ghost"),
    19: Pokemon("Dragapult", 95, 33, 9, "Ghost"),
    20: Pokemon("Chandelure", 100, 34, 10, "Ghost"),

    21: Pokemon("Gardevoir", 100, 30, 10, "Psychic"),
    22: Pokemon("Metagross", 120, 35, 18, "Psychic"),
    23: Pokemon("Espeon", 95, 29, 9, "Psychic"),
    24: Pokemon("Mewtwo", 130, 40, 15, "Psychic"),

    25: Pokemon("Umbreon", 120, 20, 20, "Dark"),
    26: Pokemon("Tyranitar", 130, 38, 18, "Dark"),
    27: Pokemon("Malamar", 100, 28, 12, "Dark"),
    28: Pokemon("Darkrai", 110, 36, 12, "Dark"),

    29: Pokemon("Pikachu", 90, 30, 8, "Electric"),
    30: Pokemon("Luxray", 105, 34, 12, "Electric"),
    31: Pokemon("Jolteon", 95, 32, 9, "Electric"),
    32: Pokemon("Electivire", 110, 36, 13, "Electric"),

    33: Pokemon("Garchomp", 120, 38, 15, "Ground"),
    34: Pokemon("Excadrill", 110, 35, 14, "Ground"),
    35: Pokemon("Donphan", 115, 30, 16, "Ground"),
    36: Pokemon("Krookodile", 105, 34, 12, "Ground"),

    37: Pokemon("Lapras", 120, 28, 14, "Ice"),
    38: Pokemon("Weavile", 95, 35, 9, "Ice"),
    39: Pokemon("Glaceon", 100, 30, 12, "Ice"),
    40: Pokemon("Mamoswine", 115, 36, 13, "Ice"),
}

type_chart = {
    "Fire": {
        "Grass": 2,
        "Ice": 2,
        "Bug": 2,
        "Water": 0.5,
        "Rock": 0.5,
        "Fire": 0.5
    },

    "Water": {
        "Fire": 2,
        "Ground": 2,
        "Rock": 2,
        "Water": 0.5,
        "Grass": 0.5,
        "Dragon": 0.5
    },

    "Grass": {
        "Water": 2,
        "Ground": 2,
        "Rock": 2,
        "Fire": 0.5,
        "Grass": 0.5,
        "Bug": 0.5,
        "Poison": 0.5,
        "Flying": 0.5
    },

    "Electric": {
        "Water": 2,
        "Flying": 2,
        "Electric": 0.5,
        "Grass": 0.5,
        "Ground": 0
    },

    "Ground": {
        "Fire": 2,
        "Electric": 2,
        "Rock": 2,
        "Poison": 2,
        "Flying": 0,
        "Grass": 0.5
    },

    "Rock": {
        "Fire": 2,
        "Ice": 2,
        "Flying": 2,
        "Bug": 2,
        "Fighting": 0.5,
        "Ground": 0.5
    },

    "Ice": {
        "Grass": 2,
        "Ground": 2,
        "Flying": 2,
        "Dragon": 2,
        "Fire": 0.5,
        "Water": 0.5,
        "Ice": 0.5
    },

    "Fighting": {
        "Normal": 2,
        "Ice": 2,
        "Rock": 2,
        "Dark": 2,
        "Flying": 0.5,
        "Psychic": 0.5,
        "Fairy": 0.5
    },

    "Poison": {
        "Grass": 2,
        "Fairy": 2,
        "Poison": 0.5,
        "Ground": 0.5,
        "Rock": 0.5
    },

    "Flying": {
        "Grass": 2,
        "Fighting": 2,
        "Bug": 2,
        "Electric": 0.5,
        "Rock": 0.5
    },

    "Psychic": {
        "Fighting": 2,
        "Poison": 2,
        "Psychic": 0.5,
        "Dark": 0
    },

    "Bug": {
        "Grass": 2,
        "Psychic": 2,
        "Dark": 2,
        "Fire": 0.5,
        "Fighting": 0.5,
        "Flying": 0.5
    },


    "Ghost": {
        "Psychic": 2,
        "Ghost": 2,
        "Normal": 0,
        "Dark": 0.5
    },

    "Dragon": {
        "Dragon": 2,
        "Ice": 0.5,
        "Fairy": 0
    },

    "Dark": {
        "Psychic": 2,
        "Ghost": 2,
        "Fighting": 0.5,
        "Dark": 0.5,
        "Fairy": 0.5
    },

    "Steel": {
        "Ice": 2,
        "Rock": 2,
        "Fairy": 2,
        "Fire": 0.5,
        "Water": 0.5,
        "Electric": 0.5
    },

    "Fairy": {
        "Dragon": 2,
        "Fighting": 2,
        "Dark": 2,
        "Fire": 0.5,
        "Poison": 0.5,
        "Steel": 0.5
    }
}


type_attacks = {
    "Fire": [("Flame Burst", 3), ("Fire Punch", 5), ("Heat Wave", 6)],

    "Water": [("Water Gun", 3), ("Aqua Jet", 5), ("Surf", 6)],

    "Grass": [("Leaf Blade", 3), ("Vine Whip", 5), ("Razor Leaf", 6)],

    "Electric": [("Thunder Shock", 3), ("Volt Strike", 5), ("Thunderbolt", 6)],

    "Ground": [("Mud Slap", 3), ("Dig", 5), ("Earthquake", 6)],

    "Rock": [("Rock Throw", 3), ("Rock Slide", 5), ("Stone Edge", 6)],

    "Ice": [("Ice Shard", 3), ("Ice Beam", 5), ("Blizzard", 6)],

    "Fighting": [("Karate Chop", 3), ("Brick Break", 5), ("Close Combat", 6)],

    "Poison": [("Poison Sting", 3), ("Sludge Bomb", 5), ("Toxic", 6)],

    "Flying": [("Gust", 3), ("Wing Attack", 5), ("Air Slash", 6)],

    "Psychic": [("Confusion", 3), ("Psybeam", 5), ("Psychic", 6)],

    "Bug": [("Bug Bite", 3), ("X-Scissor", 5), ("Signal Beam", 6)],

    "Ghost": [("Lick", 3), ("Shadow Ball", 5), ("Night Shade", 6)],

    "Dragon": [("Dragon Breath", 3), ("Dragon Claw", 5), ("Outrage", 6)],

    "Dark": [("Bite", 3), ("Dark Pulse", 5), ("Night Slash", 6)],

    "Steel": [("Metal Claw", 3), ("Iron Head", 5), ("Flash Cannon", 6)],

    "Fairy": [("Fairy Wind", 3), ("Moonblast", 5), ("Dazzling Gleam", 6)]
}


ege_team = [
    Pokemon_data[10].clone(), #Sceptile
    Pokemon_data[4].clone(),  #Delphox
    Pokemon_data[27].clone(), #Malamar
    Pokemon_data[30].clone()  #Luxray
]

battle_count = 0

trainer_names = [
    "Alex", "Luna", "Kai", "Zara", "Leo", "Maya", "Mina", "Bob",
    "Ethan", "Olivia", "Noah", "Ava", "Liam", "Sophia", "Mason", "Isabella",
    "Logan", "Amelia", "Lucas", "Mia", "James", "Charlotte", "Benjamin", "Harper",
    "Elijah", "Evelyn", "Daniel", "Abigail", "Henry", "Emily", "Sebastian", "Ella",
    "Jack", "Avery", "Aiden", "Scarlett", "Owen", "Grace", "Caleb", "Chloe",
    "Nathan", "Victoria", "Ryan", "Aria", "Luke", "Lily", "Isaac", "Zoe",
    "Gabriel", "Hannah", "Julian", "Layla", "David", "Nora", "Mina", "Riley",
    "Andrew", "Ellie", "Leo", "Stella", "Hunter", "Aurora", "Christian", "Savannah",
    "Aaron", "Skylar", "Dylan", "Penelope", "Thomas", "Lucy", "Charles", "Bella"
]


# data aralığı


playerteam = []

print("  _____   ____  _  ________ __  __  ____  _   _                       ")
print(" |  __ \ / __ \| |/ /  ____|  \/  |/ __ \| \ | |                      ")
print(" | |__) | |  | | ' /| |__  | \  / | |  | |  \| |                      ")
print(" |  ___/| |  | |  < |  __| | |\/| | |  | | . ` |                      ")
print(" | |    | |__| | . \| |____| |  | | |__| | |\  |                      ")
print(" |_|     \____/|_|\_\______|_|  |_|\____/|_| \_|_ _ _   _             ")
print("              | | | |                          | (_) | (_)            ")
print("   _ __  _   _| |_| |__   ___  _ __     ___  __| |_| |_ _  ___  _ __  ")
print("  | '_ \| | | | __| '_ \ / _ \| '_ \   / _ \/ _` | | __| |/ _ \| '_ \ ")
print("  | |_) | |_| | |_| | | | (_) | | | | |  __/ (_| | | |_| | (_) | | | |")
print("  | .__/ \__, |\__|_| |_|\___/|_| |_|  \___|\__,_|_|\__|_|\___/|_| |_|")
print("  | |     __/ |                                                       ")
print("  |_|    |___/                                                        ")
print("                                                                      ")
 
typewriter("Welcome to our Pokemon World ",0.07)
name=input("What is your name ")
typewriter("Nice to meet you "+ name +" My name is Proffesor X",0.07)
typewriter("In this world you need to select 4 pokemon for your team ",0.07)
typewriter("You are in a tournament and try to win against Last Champion Ege",0.07)
typewriter("You can choose this 40 pokemons for your team")
  
 
 
for i in Pokemon_data:
    print(i, "-", Pokemon_data[i].name)
    
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

    if selected in playerteam:
        print("You already chose this Pokemon!")
        continue

    playerteam.append(selected)

    print(selected.name, "added to your team!")
    print("Current team:", [p.name for p in playerteam])


typewriter("Nice team good luck...", 0.07)

# rakip AI

enemyteam = random.sample(list(Pokemon_data.values()), 4)



# dövüş sistemi





def reset_team(team):
    for p in team:
        p.hp = p.max_hp


def get_enemy():
    global battle_count

    battle_count += 1

    if battle_count == 2:
        winsound.PlaySound("sounds/Ege_theme.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
        return "Champion Ege", ege_team

    name = random.choice(trainer_names)
    team = [p.clone() for p in random.sample(list(Pokemon_data.values()), 4)]

    return name, team


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
    typewriter(f"You send out {p1.name}!",0.03)
    typewriter(f"Enemy sends out {p2.name}!\n",0.03)

    while True:
        #team_battle(playerteam, enemyteam)
        print("\n===================")
        print("TURN", turn)
        print("===================")

        typewriter(f"\nYOU: {p1.name} HP: {p1.hp}",0.03)
        typewriter(f"ENEMY: {p2.name} HP: {p2.hp}",0.03)

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

            choice = int(input("> ")) - 1

            if 0 <= choice < len(moves):

                move_name, bonus = moves[choice]

                multiplier = type_chart.get(p1.type, {}).get(p2.type, 1)

                damage = (p1.attack + bonus - p2.defense) * multiplier
                damage = max(1, int(damage))

                p2.hp = max(0, p2.hp - damage)

                print(f"\n{p1.name} used {move_name}!")
                print(f"It dealt {damage} damage!")

            else:
                print("Invalid move! turn wasted ")

        # ================= SWITCH =================
        elif action == 2:

            print("\nChoose Pokemon to switch:")

            valid_indexes = []

            for i, p in enumerate(playerteam):
                if p.hp > 0:
                    valid_indexes.append(i)
                    print(f"{i+1} - {p.name} (HP: {p.hp})")

            switch = int(input("> ")) - 1

            if switch in valid_indexes:
                p1 = playerteam[switch]
                print(f"\nGo {p1.name}!")
            else:
                print("Invalid switch!")

        else:
            print("Invalid action!")

        # ================= ENEMY DEAD =================
        if p2.hp <= 0:

            print(f"\n{p2.name} fainted!")

            e_index += 1

            #  SKIP DEAD ENEMY POKEMON
            while e_index < len(enemy_team) and enemy_team[e_index].hp <= 0:
                e_index += 1

            if e_index >= len(enemy_team):
                print("\n YOU WIN THE BATTLE!")
                return True

            p2 = enemy_team[e_index]
            print(f"\nEnemy sends out {p2.name}!")

        # ================= ENEMY ATTACK =================
        if p2.hp > 0:

            enemy_moves = type_attacks[p2.type]
            enemy_move_name, enemy_bonus = random.choice(enemy_moves)

            enemy_multiplier = type_chart.get(p2.type, {}).get(p1.type, 1)

            enemy_damage = (p2.attack + enemy_bonus - p1.defense) * enemy_multiplier
            enemy_damage = max(1, int(enemy_damage))

            p1.hp = max(0, p1.hp - enemy_damage)

            print(f"\nEnemy {p2.name} used {enemy_move_name}!")
            print(f"It dealt {enemy_damage} damage!")

        # ================= PLAYER DEAD =================
        if p1.hp <= 0:

            print(f"\n{p1.name} fainted!")

            p_index += 1

            #  SKIP DEAD PLAYER POKEMON
            while p_index < len(playerteam) and playerteam[p_index].hp <= 0:
                p_index += 1

            if p_index >= len(playerteam):
                print("\n YOU LOST THE BATTLE!")
                return False

            p1 = playerteam[p_index]
            print(f"\nGo {p1.name}!")

        turn += 1


while battle_count < 4:
    enemy_name, enemyteam = get_enemy()
    print(f"\n Your opponent: {enemy_name}")
    won=team_battle(playerteam, enemyteam)

    if won:
        typewriter("CONGRATULATIONS! You defated Champion Ege and won the tournament...",0.07)
    if not won:
        typewriter("Game Over!",0.5)
        break
