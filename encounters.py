from presets import ENEMY_PRESETS, ENCOUNTER_PRESETS, SHOP_PRESETS
from character import Character
import random

def create_encounter(hero: Character):
    """Chooses and returns a random encounter that the hero's level allows"""

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
    """Creates enemies from the given encounter"""

    enemies = []

    for enemy_name in chosen_encounter["enemies"]:
        new_enemy = Character(enemy_name.title(), enemy_name, **ENEMY_PRESETS[enemy_name])
        enemies.append(new_enemy)

    return enemies


def rest(hero: Character, encounter):
    """Heals the hero by the encounter's percentage of max health and reports the amount healed"""

    if encounter["heal_percent"] <= 0:
        raise ValueError("Must be positive")

    print("\n-- Rest --")

    old_health = hero.health
    amount = hero.max_health * encounter["heal_percent"] // 100
    hero.heal(amount)
    print(f"You rest and recover {hero.health - old_health} HP.")


def train(hero: Character):
    """Asks which stat to raise and increases it by 1"""

    stats = ["strength", "dexterity", "wisdom"]
    while True:
        print("\n-- Training --")

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

        print("\nNot a valid choice")


def shop(hero, encounter):
    """Lets the player spend their gold on the items in the shop"""

    stock = encounter["stock"]
    leave_shop = len(stock) + 1

    while True:
        print("\n-- Shop --")
        print(f"{hero.name} - {hero.health}/{hero.max_health} HP | {hero.gold} Gold | {hero.potions} Potion(s)")
        print()

        for index, item in enumerate(stock, start=1):
            print(f"[{index}] {item.title()} - {SHOP_PRESETS[item]['price']} gold")
        print(f"[{leave_shop}] Leave")

        choice = input("Choose option: ")

        if choice.isdigit():
            choice = int(choice)

            if choice == leave_shop:
                return

            if 1 <= choice <= len(stock):
                item = stock[choice - 1]
                price = SHOP_PRESETS[item]["price"]

                if hero.gold < price:
                    print("Not enough gold.")
                    continue

                attribute = SHOP_PRESETS[item]["attribute"]
                hero.gold -= price
                setattr(hero, attribute, getattr(hero, attribute) + 1)
                print(f"You've bought a {item.title()} for {price} gold.")
                continue

        print("\nNot a valid choice")