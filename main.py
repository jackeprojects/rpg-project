from presets import HERO_PRESETS, ENEMY_PRESETS
from character import Character
import random

# Randomize amount of enemies in a battle
enemy_count = random.randint(1, 5)
enemies = []
for _ in range(1, enemy_count + 1):
    enemy_preset = random.choice(list(ENEMY_PRESETS.keys()))
    new_enemy = Character(enemy_preset.title(), enemy_preset, **ENEMY_PRESETS[enemy_preset])
    enemies.append(new_enemy)