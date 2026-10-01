from weapon import Weapon
import random

class Character:
    """A hero or enemy with stats, health and ability to fight and level"""

    def __init__(self, name: str, role: str, strength: int, dexterity: int, wisdom: int, accuracy: int, max_health=100, xp_reward=0, gold_reward=0, level=1):
        self.name = name
        self.role = role
        self.strength = strength
        self.dexterity = dexterity
        self.wisdom = wisdom
        self.accuracy = accuracy
        self.max_health = max_health
        self.gold_reward = gold_reward
        self.xp_reward = xp_reward
        self.level = level

        self.health = self.max_health
        self.potions = 0
        self.gold = 0
        self.xp = 0

    def take_damage(self, amount):
        """Reduces health by the amount without going below zero"""

        if amount < 0:
            raise ValueError("Cannot be negative")

        if amount > self.health:
            amount = self.health

        self.health -= amount

    def is_alive(self):
        """Checks if character is alive and returns result"""
        return self.health > 0

    def calculate_damage(self, weapon: Weapon):
        """Rolls to hit and returns dict with result and how much damage"""

        if weapon.archetype == "melee":  # use Strength to scale damage
            weapon_stat = self.strength

        elif weapon.archetype == "ranged":  # use Dexterity to scale damage
            weapon_stat = self.dexterity

        elif weapon.archetype == "magic":  # use Wisdom to scale damage
            weapon_stat = self.wisdom

        else:
            raise ValueError("Must have a valid archetype")

        is_hit = random.randint(1, 100) <= self.accuracy

        damage = weapon.base_damage * (1 + weapon_stat / 100)

        if is_hit:
            return {"hit": is_hit, "damage": damage}

        else:
            return {"hit": is_hit, "damage": 0}

    def heal(self, amount: int):
        """Heals the character up to max health"""

        if amount < 0:
            raise ValueError("Cannot be negative")

        if self.health + amount > self.max_health:
            self.health = self.max_health

        else:
            self.health += amount

    def gain_xp(self, amount: int):
        """Applies xp to character and levels up if it can"""

        if amount < 0:
            raise ValueError("Cannot be negative")

        self.xp += amount

        while self.xp >= self.level * 50:
            self.xp -= self.level * 50
            self._level_up()

    def gain_gold(self, amount: int):
        """Adds gold to the character"""

        if amount < 0:
            raise ValueError("Cannot be negative")

        self.gold += amount

    def use_potion(self):
        """Uses a potion to heal and returns the amount healed"""

        if self.potions <= 0:
            raise ValueError("No potions left")

        old_health = self.health
        self.potions -= 1
        self.heal(self.max_health // 2)

        return self.health - old_health

    def _level_up(self):
        """Raises the level and stats, max health and fully heals character"""

        self.level += 1
        self.strength += 1
        self.dexterity += 1
        self.wisdom += 1
        self.max_health += 10
        self.heal(self.max_health)