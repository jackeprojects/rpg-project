from presets import HERO_PRESETS, WOODEN_WEAPON_PRESETS
from character import Character
from weapon import Weapon
from battle import Battle
from encounters import create_encounter

hero_name = input("Enter a name: ")

while True:
    for n, key in enumerate(HERO_PRESETS, start=1):
        print(f"[{n}] {key.title()}")
    hero_role = input("Choose class: ")

    if hero_role.isdigit():
        hero_role = int(hero_role)
        if 1 <= hero_role <= len(HERO_PRESETS):
            role_index = hero_role - 1

            # Get role and weapon
            role_key = list(HERO_PRESETS)[role_index]
            weap_key = list(WOODEN_WEAPON_PRESETS)[role_index]
            break

    print("Must choose a valid role.\n")

# Create hero and their weapon
hero = Character(hero_name, role_key.title(), **HERO_PRESETS[role_key])
hero_weap = Weapon(**WOODEN_WEAPON_PRESETS[weap_key])

# Create enemy weapon
enemy_weap = Weapon("Scratch", "melee", 6)

while True:
    encounter_name, enemies = create_encounter(hero.level)
    print(f"\n{encounter_name} appears!")

    # Create battle and start it
    battle = Battle(hero, hero_weap, enemies, enemy_weap)
    won = battle.start()

    if not won:
        print("GAME OVER")
        break

    xp_gained = 0
    for enemy in enemies:
        xp_gained += enemy.xp_reward

    old_level = hero.level
    hero.gain_xp(xp_gained)
    print(f"You gained {xp_gained} XP")
    if hero.level > old_level:
        print(f"Level up! You are now level {hero.level}.")

    hero.heal(hero.max_health)

    if input("Fight again? (y/n): ").lower() != "y":
        break