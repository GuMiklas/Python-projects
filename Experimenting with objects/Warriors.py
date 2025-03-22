class Weapon:
    def __init__(self, name: str, damage: float):
        self.name = name
        self.damage = damage

class Warrior:
    def __init__(self, name: str, health: float):
        self.name = name
        self.health = health
        self.weapon = None

    def warcry(self):
        if self.health > 0.0:
            print("RAAARGH")

    def equip_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self, enemy):
        if self.health <= 0.0:
            return

        if self.weapon:
            enemy.health -= self.weapon.damage
        else:
            enemy.health -= 2.0

        if enemy.health < 0.0:
            enemy.health = 0.0

warrior1 = Warrior('Beir', 70.0)

warrior2 = Warrior('Uldiir', 120.0)
battleaxe = Weapon('Battleaxe', 75.0)
warrior2.equip_weapon(battleaxe)

warrior1.warcry() # -> RAAARGH

warrior1.attack(warrior2)
print(warrior2.health) # -> 118.0

warrior2.attack(warrior1)
print(warrior1.health) # -> 0.0

warrior1.warcry() # -> (nothing)