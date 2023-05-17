class Weapon:
    RUSTY_SWORD = 'RUSTY SWORD'
    GREAT_SWORD = 'GREAT SWORD'
    HEROIC_SWORD = 'HEROIC SWORD'
    BATTLE_AXE = 'BATTLE AXE'
    HEROIC_BATTLE_AXE = 'HEROIC BATTLE AXE'

    # Dictionary that define the Cost for a given weapon
    WEAPON_COST = {GREAT_SWORD: 40, HEROIC_SWORD: 100, BATTLE_AXE: 45, HEROIC_BATTLE_AXE: 120}

    # Dictionary that define the Damage for a given weapon
    WEAPON_DAMAGE = {GREAT_SWORD: 15, HEROIC_SWORD: 35, BATTLE_AXE: 30, HEROIC_BATTLE_AXE: 40, RUSTY_SWORD: 5}

    @staticmethod
    def get_weapon_list():
        return Weapon.WEAPON_COST

    def get_weapon_value(self):
        return self._weapon_value

    def get_weapon_type(self):
        return self.weapon_type

    def get_weapon_damage(self):
        return self._weapon_damage

    def __init__(self, weapon_type=RUSTY_SWORD):
        self.weapon_type = weapon_type
        self._weapon_damage = Weapon.WEAPON_DAMAGE[weapon_type]

        if weapon_type == Weapon.RUSTY_SWORD:
            self._weapon_value = 0
        else:
            self._weapon_value = Weapon.WEAPON_COST[weapon_type]

    def __eq__(self, other):
        return (
                self.__class__ == other.__class__ and
                self.weapon_type == other.weapon_type
         )
