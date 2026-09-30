from presets import HERO_PRESETS, ENEMY_PRESETS, WOODEN_WEAPON_PRESETS
from character import Character
from weapon import Weapon
import random

# Randomize amount of enemies in a battle
enemy_count = random.randint(1, 5)
enemies = []
for _ in range(1, enemy_count + 1):
    enemy_preset = random.choice(list(ENEMY_PRESETS.keys()))
    new_enemy = Character(enemy_preset.title(), enemy_preset, **ENEMY_PRESETS[enemy_preset])
    enemies.append(new_enemy)

hero_name = input("Enter a name: ")

while True:
    n = 0
    for n, key in enumerate(HERO_PRESETS, start=1):
        print(f"[{n}] {key.title()}")
    hero_role = input("Choose class: ")

    if hero_role.isdigit():
        hero_role = int(hero_role)

        # If choice is Swordsman
        if hero_role == 1:
            # Get name of role
            role_key = list(HERO_PRESETS)[hero_role - 1]

            # Get name of weapon based on hero role choice
            weap_key = list(WOODEN_WEAPON_PRESETS)[hero_role - 1]
            print(role_key.title())
            break
        # If choice is Archer
        elif hero_role == 2:
            # Get name of role
            role_key = list(HERO_PRESETS)[hero_role - 1]

            # Get name of weapon based on hero role choice
            weap_key = list(WOODEN_WEAPON_PRESETS)[hero_role - 1]
            print(role_key.title())
            break
        # If choice is Mage
        elif hero_role == 3:
            # Get name of role
            role_key = list(HERO_PRESETS)[hero_role - 1]

            # Get name of weapon based on hero role choice
            weap_key = list(WOODEN_WEAPON_PRESETS)[hero_role - 1]
            print(role_key.title())
            break
        # If choice doesn't exists
        else:
            print("Illegal choice\n")

    # If choice is not a int
    else:
        print("Illegal input\n")

# Create hero
hero = Character(hero_name, role_key.title(), **HERO_PRESETS[role_key])
# Create weapon
hero_weap = Weapon(**WOODEN_WEAPON_PRESETS[weap_key])