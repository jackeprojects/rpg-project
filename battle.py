from character import Character
from weapon import Weapon

class Battle:
    def __init__(self, hero: Character, hero_weap: Weapon, enemies: list[Character], enemy_weap: Weapon):
        self.hero = hero
        self.hero_weap = hero_weap
        self.enemies = enemies
        self.enemy_weap = enemy_weap

    def start(self):
        while True:
            alive, _ = self._split_enemies()
            if not self.hero.is_alive() or not alive:
                break
            self._hero_turn()
            self._enemy_turn()

        if self.hero.is_alive():
            print("Success! All enemies have been defeated")
            return True
        else:
            print("Defeat!", self.hero.name, "has died!")
            return False

    def _split_enemies(self):
        alive = []
        dead = []
        for enemy in self.enemies:
            if enemy.is_alive():
                alive.append(enemy)
            else:
                dead.append(enemy)

        return alive, dead

    def _show_enemies(self):
        alive, dead = self._split_enemies()
        for index, enemy in enumerate(alive, start=1):
            print(f"[{index}] {enemy.name} - {enemy.health}/{enemy.max_health} HP")
        for enemy in dead:
            print(f"[x] {enemy.name} - Dead")

    def _choose_target(self):
        alive, _ = self._split_enemies()
        while True:
            self._show_enemies()
            choice = input("Choose enemy: ")

            if choice.isdigit():
                choice = int(choice)
                if choice in range(1, len(alive) + 1):
                    target = alive[choice - 1]
                    return target
                else:
                    print("Not a valid choice")

            else:
                print("Not a valid choice")

    def _hero_turn(self):
        target = self._choose_target()
        damage_check = self.hero.calculate_damage(self.hero_weap)
        if damage_check["hit"]:
            damage = round(damage_check["damage"])
            target.take_damage(damage)
            print(f"{target.name} was hit with {self.hero_weap.name} for {damage}")
            if not target.is_alive():
                print(target.name, "died!")
        else:
            print(self.hero.name, "missed!")

    def _enemy_turn(self):
        alive, _ = self._split_enemies()
        for enemy in alive:
            if self.hero.is_alive():
                damage_check = enemy.calculate_damage(self.enemy_weap)
                if damage_check["hit"]:
                    damage = round(damage_check["damage"])
                    self.hero.take_damage(damage)
                    print(f"{self.hero.name} was hit with {self.enemy_weap.name} by {enemy.name} for {damage}")
                else:
                    print(enemy.name, "missed!")
            else:
                return