print("pokemon_types loaded")
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