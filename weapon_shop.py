from weapon import Weapon
from inventory import Inventory


class WeaponShop():

    def ItemForSale(self):

        weaponList = Weapon.get_weapon_list()
        shopKeeper = 'welcome to the store\n'
        itemNum = 1

        for weapon, value in weaponList.items():
            menuItem = str(itemNum) + ') ' + weapon + ': ' + str(value) + ' gold\n'
            shopKeeper += menuItem
            itemNum += 1

        return shopKeeper

    def BuyWeapon(self, weapon, inventory):

        weapon = Weapon(weapon)

        if inventory.get_gold() >= weapon.get_weapon_value():
            inventory.remove_gold(weapon.get_weapon_value())
            inventory.add_weapon(weapon)
            return True

        else:
            return False
