from character import Character
from weapon import Weapon

class Battle:
    """A turn-based fight between the hero and a group of enemies"""

    def __init__(self, hero: Character, hero_weap: Weapon, enemies: list[Character], enemy_weap: Weapon):
        self.hero = hero
        self.hero_weap = hero_weap
        self.enemies = enemies
        self.enemy_weap = enemy_weap

    def start(self):
        """Runs rounds until the hero or all enemies are dead and returns True if the hero won"""

        round_number = 1
        while True:
            alive, _ = self._split_enemies()

            if not self.hero.is_alive() or not alive:
                break

            print(f"\n========== Round {round_number} ==========")
            print(f"{self.hero.name} - {self.hero.health}/{self.hero.max_health} HP | {self.hero.gold} Gold")

            self._hero_turn()

            alive, _ = self._split_enemies()
            if not alive:
                break

            print("\n-- Enemies --")
            self._enemy_turn()

            if self.hero.is_alive():
                input("\nPress Enter to continue...")

            round_number += 1

        return self.hero.is_alive()

    def _split_enemies(self):
        """Returns the living and dead enemies as two lists"""

        alive = []
        dead = []

        for enemy in self.enemies:
            if enemy.is_alive():
                alive.append(enemy)

            else:
                dead.append(enemy)

        return alive, dead

    def _show_enemies(self):
        """Prints the enemies, numbering the alive and marking the dead"""

        alive, dead = self._split_enemies()
        for index, enemy in enumerate(alive, start=1):
            print(f"[{index}] {enemy.name} - {enemy.health}/{enemy.max_health} HP")

        for enemy in dead:
            print(f"[x] {enemy.name} - Dead")

    def _choose_target(self):
        """Asks the player to choose a living enemy and returns it"""

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
        """Asks the player whether to attack or use a potion"""

        while True:
            self._show_enemies()

            print(f"\n[1] Attack\n[2] Use potion ({self.hero.potions} left)")
            choice = input("Choose option: ")

            if choice.isdigit():
                choice = int(choice)

                if choice == 1:
                    print("\n-- Choose a target --")
                    target = self._choose_target()
                    print("\n-- You --")
                    self._attack(self.hero, target, self.hero_weap)
                    return

                elif choice == 2:
                    if self.hero.potions > 0:
                        print("\n-- You --")
                        hp_recovered = self.hero.use_potion()
                        print(f"You drink potion and recover {hp_recovered} HP")
                        return

                    else:
                        print("You have no potions left!")
                        continue

            print("Not a valid choice")

    def _enemy_turn(self):
        """Has each living enemy attack the hero"""

        alive, _ = self._split_enemies()
        for enemy in alive:
            if self.hero.is_alive():
                self._attack(enemy, self.hero, self.enemy_weap)

            else:
                return

    def _attack(self, attacker: Character, defender: Character, weapon: Weapon):
        """Checks if the attack hits, applies damage and prints the result"""

        damage_check = attacker.calculate_damage(weapon)
        if damage_check["hit"]:
            damage = round(damage_check["damage"])
            defender.take_damage(damage)
            print(f"{attacker.name} hits {defender.name} with {weapon.name} for {damage} damage.")

        else:
            print(f"{attacker.name} misses!")

        if not defender.is_alive():
            print(f"{defender.name} died!")