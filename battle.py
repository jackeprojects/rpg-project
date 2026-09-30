from character import Character
from weapon import Weapon

class Battle:
    def __init__(self, hero: Character, hero_weap: Weapon, enemies: list[Character], enemy_weap: Weapon):
        self.hero = hero
        self.hero_weap = hero_weap
        self.enemies = enemies
        self.enemy_weap = enemy_weap

    def start(self):
        pass

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