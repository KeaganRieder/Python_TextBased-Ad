from weapon import Weapon


class Inventory:
    def __init__(self):
        self.weapons = []
        self.weapons.append(Weapon())
        self.gold = 40

    def get_weapon_list(self):
        return self.weapons

    def get_first_weapon(self):
        return self.weapons[0]

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    # get weapon from inventory
    # if weapon is in inventory return the weapon
    # else return none
    def get_weapon(self, weapon_type):

        try:
            index = self.weapons.index(Weapon(weapon_type))
            return self.weapons[index]
        except ValueError:
            return None

    def get_gold(self):
        return self.gold

    def remove_gold(self, amount):
        if self.gold < amount:
            return False
        else:
            self.gold -= amount
            return True

    def to_string(self):
        inventory = '#######################################'
        for weapon in self.weapons:
            inventory += '\n> ' + weapon.get_weapon_type()
        inventory += '\ngold: %s' % self.gold
        inventory += '\n#######################################\n'

        return inventory
