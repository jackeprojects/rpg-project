HERO_PRESETS = {
    "swordsman": {"strength": 15, "dexterity": 8, "wisdom": 3, "accuracy": 55},
    "archer": {"strength": 6, "dexterity": 16, "wisdom": 4, "accuracy": 60},
    "mage": {"strength": 4, "dexterity": 6, "wisdom": 18, "accuracy": 45}
}

ENEMY_PRESETS = {
    "rat": {"strength": 3, "dexterity": 6, "wisdom": 1, "accuracy": 35, "max_health": 40, "xp_reward": 10, "gold_reward": 5},
    "goblin": {"strength": 6, "dexterity": 9, "wisdom": 2, "accuracy": 45, "max_health": 60, "xp_reward": 20, "gold_reward": 10},
    "skeleton": {"strength": 10, "dexterity": 7, "wisdom": 2, "accuracy": 55, "max_health": 80, "xp_reward": 35, "gold_reward": 20}
}

ENCOUNTER_PRESETS = [
    {"name": "A lone rat", "type": "battle", "min_level": 1, "enemies": ["rat"]},
    {"name": "A pair of rats", "type": "battle", "min_level": 1, "enemies": ["rat", "rat"]},
    {"name": "A wandering goblin", "type": "battle", "min_level": 1, "enemies": ["goblin"]},
    {"name": "A goblin and its pet", "type": "battle", "min_level": 2, "enemies": ["goblin", "rat"]},
    {"name": "A goblin raiding party", "type": "battle", "min_level": 2, "enemies": ["goblin", "goblin", "rat"]},
    {"name": "A restless skeleton", "type": "battle", "min_level": 3, "enemies": ["skeleton"]},
    {"name": "Skeleton and goblin ambush", "type": "battle", "min_level": 3, "enemies": ["skeleton", "goblin"]},
    {"name": "The crypt guards", "type": "battle", "min_level": 4, "enemies": ["skeleton", "skeleton", "goblin"]},
    {"name": "A horde", "type": "battle", "min_level": 5, "enemies": ["skeleton", "goblin", "goblin", "rat", "rat"]},

    {"name": "A quiet campfire", "type": "rest", "min_level": 1, "heal_percent": 50},
    {"name": "A mossy spring", "type": "rest", "min_level": 1, "heal_percent": 35},
    {"name": "An abandoned hunter's cabin", "type": "rest", "min_level": 2, "heal_percent": 60},
    {"name": "A friendly healer's wagon", "type": "rest", "min_level": 3, "heal_percent": 80},
    {"name": "A moonlit shrine", "type": "rest", "min_level": 4, "heal_percent": 100},

    {"name": "A training ground", "type": "train", "min_level": 1},

    {"name": "A travelling merchant", "type": "shop", "min_level": 1, "stock": ["potion"]}
]

SHOP_PRESETS = {
    "potion": {"price": 30}
}

WOODEN_WEAPON_PRESETS = {
    "wooden sword": {"name": "Wooden Sword", "archetype": "melee", "base_damage": 20},
    "wooden bow": {"name": "Wooden Bow", "archetype": "ranged", "base_damage": 20},
    "wooden staff": {"name": "Wooden Staff", "archetype": "magic", "base_damage": 20}
}