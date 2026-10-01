from presets import ENEMY_PRESETS, ENCOUNTER_PRESETS
from character import Character
import random

def create_encounter(hero_level: int):
    allowed_encounters = []

    for encounter in ENCOUNTER_PRESETS:
        if hero_level >= encounter["min_level"]:
            allowed_encounters.append(encounter)

    chosen_encounter = random.choice(allowed_encounters)

    enemies = []
    for enemy_name in chosen_encounter["enemies"]:
        new_enemy = Character(enemy_name.title(), enemy_name, **ENEMY_PRESETS[enemy_name])
        enemies.append(new_enemy)

    return chosen_encounter["name"], enemies