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
        