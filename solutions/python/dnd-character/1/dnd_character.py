import random

def modifier(constitution: int) -> int:
    return (constitution - 10) // 2


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self) -> int:
        dice = [random.randint(1, 6) for i in range(3)]
        return sum(sorted(dice)[1:])


    
