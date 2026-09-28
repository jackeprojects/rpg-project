# Template for characters (hero/enemies)

class Character:
    def __init__(self, name: str, role: str, strength: int, dexterity: int, wisdom: int, level=1):
        self.name = name
        self.role = role
        self.strength = strength
        self.dexterity = dexterity
        self.wisdom = wisdom
        self.level = level

        self.max_health = 100
        self.max_stamina = 100
        self.max_mana = 100
        self.health = self.max_health
        self.stamina = self.max_stamina
        self.mana = self.max_mana

    def take_damage(self, amount):
        if amount < 0:
            raise ValueError("Cannot be negative")
        if amount > self.health:
            amount = self.health
        self.health -= amount

    def is_alive(self):
        return self.health > 0