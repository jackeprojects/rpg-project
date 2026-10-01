from presets import ENEMY_PRESETS, ENCOUNTER_PRESETS
from character import Character
import random

def create_encounter(hero_level: int):
    allowed_encounters = []

    for encounter in ENCOUNTER_PRESETS:
        if hero_level >= encounter["min_level"]:
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
    if hero.health == hero.max_health:
        print("You rest, but you're already at full health.")
        return
    old_health = hero.health
    amount = hero.max_health * encounter["heal_percent"] // 100
    hero.heal(amount)
    print(f"You rest and recover {hero.health - old_health} HP.")