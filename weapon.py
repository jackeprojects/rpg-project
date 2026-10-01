class Weapon:
    """A weapon with a name, archetype, and base damage"""

    def __init__(self, name: str, archetype: str, base_damage: int):
        self.name = name
        self.archetype = archetype
        self.base_damage = base_damage