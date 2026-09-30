# Template for characters (hero/enemies)

from weapon import Weapon
import random

class Character:
    def __init__(self, name: str, role: str, strength: int, dexterity: int, wisdom: int, accuracy: int, max_health=100, level=1):
        self.name = name
        self.role = role
        self.strength = strength
        self.dexterity = dexterity
        self.wisdom = wisdom
        self.accuracy = accuracy
        self.max_health = max_health
        self.level = level
        
        self.health = self.max_health

    def take_damage(self, amount):
        if amount < 0:
            raise ValueError("Cannot be negative")
        if amount > self.health:
            amount = self.health
        self.health -= amount

    def is_alive(self):
        return self.health > 0

    def calculate_damage(self, weapon: Weapon):
        weapon_stat = 0
        if weapon.archetype == "melee":
            # use STR to scale dmg
            weapon_stat = self.strength
        elif weapon.archetype == "ranged":
            weapon_stat = self.dexterity
            # use DEX to scale dmg
        elif weapon.archetype == "magic":
            # use WIS to scale dmg
            weapon_stat = self.wisdom
        else:
            raise ValueError("Must have a valid archetype")
        
        is_hit = random.randint(1, 100) <= self.accuracy

        damage = weapon.base_damage * (1 + weapon_stat / 100)

        if is_hit:
            return {"hit": is_hit, "damage": damage}
        else:
            return {"hit": is_hit, "damage": 0}