import unittest
from weapon_shop import WeaponShop
from inventory import Inventory
from weapon import Weapon


class WeaponShopTestCase(unittest.TestCase):

    def test_item_for_sale(self):
        weapon_shop = WeaponShop()
        test_string = 'welcome to the store\n'
        test_string += '1) GREAT SWORD: 40 gold\n'
        test_string += '2) HEROIC SWORD: 100 gold\n'
        test_string += '3) BATTLE AXE: 45 gold\n'
        test_string += '4) HEROIC BATTLE AXE: 120 gold\n'
        self.assertEqual(test_string, weapon_shop.ItemForSale())

    def test_buy_weapon_enough_money(self):
        weapon_shop = WeaponShop()
        inventory = Inventory()
        self.assertTrue(weapon_shop.BuyWeapon(Weapon.GREAT_SWORD, inventory))

    def test_buy_weapon_not_enough_money(self):
        # Check adding a weapon of over $40
        weapon_shop = WeaponShop()
        inventory = Inventory()

        self.assertFalse(weapon_shop.BuyWeapon(Weapon.HEROIC_SWORD, inventory))


if __name__ == '__main__':
    unittest.main()
