import random
import winsound
import time

from data import Pokemon_data
from utils import typewriter


ege_team = [
    Pokemon_data[10].clone(), #Sceptile
    Pokemon_data[4].clone(),  #Delphox
    Pokemon_data[27].clone(), #Malamar
    Pokemon_data[30].clone()  #Luxray
]

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

def get_enemy():
    global battle_count

def get_enemy(battle_count):

    if battle_count == 3:
        winsound.PlaySound("sounds/Ege_theme.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
        typewriter("I'm impressed you made it this far. Congratulations... but this is where your journey ends.",0.07)
        time.sleep(1)
        return "Champion Ege", ege_team

    name = random.choice(trainer_names)
    team = [p.clone() for p in random.sample(list(Pokemon_data.values()), 4)]

    return name, team
