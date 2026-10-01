from presets import ENEMY_PRESETS, ENCOUNTER_PRESETS
from character import Character
import random

def create_encounter(hero: Character):
    allowed_encounters = []

    for encounter in ENCOUNTER_PRESETS:
        if hero.level < encounter["min_level"]:
            continue
        if encounter["type"] == "rest" and hero.health == hero.max_health:
            continue
        allowed_encounters.append(encounter)

    chosen_encounter = random.choice(allowed_encounters)

    return chosen_encounter


def build_enemies(chosen_encounter):
    enemies = []
    for enemy_name in chosen_encounter["enemies"]:
        new_enemy = Character(enemy_name.title(), enemy_name, **ENEMY_PRESETS[enemy_name])
        enemies.append(new_enemy)

    return enemies


def rest(hero: Character, encounter):
    if encounter["heal_percent"] <= 0:
        raise ValueError("Must be positive")
    old_health = hero.health
    amount = hero.max_health * encounter["heal_percent"] // 100
    hero.heal(amount)
    print(f"You rest and recover {hero.health - old_health} HP.")


def train(hero: Character):
    stats = ["strength", "dexterity", "wisdom"]
    while True:
        print()
        for index, stat in enumerate(stats, start=1):
            print(f"[{index}] {stat.title()} ({getattr(hero, stat)})")
        choice = input("Choose stat: ")

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(stats):
                stat = stats[choice - 1]
                setattr(hero, stat, getattr(hero, stat) + 1)
                print(f"Your {stat.title()} is now {getattr(hero, stat)}")
                return

        print("Not a valid choice")