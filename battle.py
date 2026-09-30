from character import Character
from weapon import Weapon

class Battle:
    def __init__(self, hero: Character, hero_weap: Weapon, enemies: list[Character], enemy_weap: Weapon):
        self.hero = hero
        self.hero_weap = hero_weap
        self.enemies = enemies
        self.enemy_weap = enemy_weap

    def start(self):
        round_number = 1
        while True:
            alive, _ = self._split_enemies()
            if not self.hero.is_alive() or not alive:
                break

            print(f"\n========== Round {round_number} ==========")
            print(f"{self.hero.name} - {self.hero.health}/{self.hero.max_health} HP")
            print("\n-- Choose a target --")

            self._hero_turn()

            alive, _ = self._split_enemies()
            if not alive:
                break

            print("\n-- Enemies --")
            self._enemy_turn()

            if self.hero.is_alive():
                input("\nPress Enter to continue...")
            round_number += 1

        if self.hero.is_alive():
            print("Success! All enemies have been defeated.")
            return True
        else:
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
        print("\n-- You --")
        self._attack(self.hero, target, self.hero_weap)

    def _enemy_turn(self):
        alive, _ = self._split_enemies()
        for enemy in alive:
            if self.hero.is_alive():
                self._attack(enemy, self.hero, self.enemy_weap)
            else:
                return

    def _attack(self, attacker: Character, defender: Character, weapon: Weapon):
        damage_check = attacker.calculate_damage(weapon)
        if damage_check["hit"]:
            damage = round(damage_check["damage"])
            defender.take_damage(damage)
            print(f"{attacker.name} hits {defender.name} with {weapon.name} for {damage} damage.")
        else:
            print(f"{attacker.name} misses!")

        if not defender.is_alive():
            print(f"{defender.name} died!")