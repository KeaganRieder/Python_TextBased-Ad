from random import randint
from inventory import Inventory


class Player:
    #creating values for the player
    def __init__(self, name,):
        self.name = name
        self.max_health = 100
        self.health = self.max_health
        self.base_attack = 10
        self.inventory = Inventory()
        self.playerLocation = 7
        self.currentWeapon = self.inventory.get_first_weapon()

    def damage(self):
        damage = self.base_attack
        damage += self.currentWeapon.get_weapon_damage()
        return damage

    def player_location(self):
        return self.playerLocation

    def equip_weapon(self, weapon_type):
        weapon = self.inventory.get_weapon(weapon_type)

        if weapon is not None:
            self.currentWeapon = weapon
            return True
        else:
            return False
    #adding gold to players inventory
    def add_gold(self, gold_gain):
        self.inventory.gold += gold_gain
        return self.inventory.gold

    def get_weapon_list(self):
        weapons = []

        for weapon in self.inventory.weapons:
            weapons.append(weapon.weapon_type)

        return weapons


    # allows the player to rest in order to gain back hp
    def rest(self):

        new_health = self.health
        new_health += randint(10, 30)

        if new_health > 100:
            self.health = 100
        else:
            self.health = new_health
