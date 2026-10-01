from presets import HERO_PRESETS, WOODEN_WEAPON_PRESETS
from character import Character
from weapon import Weapon
from battle import Battle
from encounters import create_encounter, build_enemies, rest, train

def create_hero():
    """Asks for name and class, then returns their new hero and starter weapon"""

    hero_name = ""
    while not hero_name:
        hero_name = input("Enter a name: ").strip()

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

    # Give hero 2 starting potions
    hero.potions = 2

    return hero, hero_weap


def award_rewards(hero: Character, enemies: list):
    """Gives the hero the xp and gold of the defeated enemies and reports any level up"""

    old_level = hero.level
    xp_gained = 0
    gold_gained = 0

    for enemy in enemies:
        xp_gained += enemy.xp_reward
        gold_gained += enemy.gold_reward

    hero.gain_xp(xp_gained)
    print(f"You gained {xp_gained} XP")

    if hero.level > old_level:
        print(f"Level up! You are now level {hero.level}.")

    hero.gain_gold(gold_gained)
    print(f"You found {gold_gained} gold")


def main():
    """Runs encounters one after another until the hero dies or the player quits"""

    hero, hero_weap = create_hero()

    # Create enemy weapon
    enemy_weap = Weapon("Scratch", "melee", 6)

    while True:
        encounter = create_encounter(hero)
        print(f"\n{encounter['name']} appears!")

        if encounter["type"] == "battle":
            enemies = build_enemies(encounter)

            # Create battle and start it
            battle = Battle(hero, hero_weap, enemies, enemy_weap)
            won = battle.start()

            if not won:
                print(f"{hero.name} has fallen... GAME OVER")
                break

            print("Success! All enemies have been defeated.")

            award_rewards(hero, enemies)

        elif encounter["type"] == "rest":
            rest(hero, encounter)

        elif encounter["type"] == "train":
            train(hero)

        if input("Continue or quit? (Enter/q): ").lower() == "q":
            break


if __name__ == "__main__":
    main()