import unittest

from inventory import Inventory
from weapon import Weapon


class InventoryTestCase(unittest.TestCase):

    def test_GetWeaponFirst(self):
        inventory = Inventory()
        weapon = Weapon()
        weapon_type = inventory.get_first_weapon().get_weapon_type()
        check_type = weapon.get_weapon_type()
        self.assertEqual(check_type, weapon_type)

    def test_AddWeapon(self):
        inventory = Inventory()
        inventory.add_weapon(Weapon(Weapon.GREAT_SWORD))

        self.assertEqual(2, len(inventory.get_weapon_list()))
        self.assertEqual(Weapon.GREAT_SWORD, inventory.get_weapon_list()[1].get_weapon_type())

    def test_get_weapon(self):
        inventory = Inventory()
        weapon = inventory.get_weapon(Weapon.RUSTY_SWORD)

        self.assertIsNotNone(weapon)

    def test_no_weapon_found(self):
        inventory = Inventory()
        weapon = inventory.get_weapon(Weapon.GREAT_SWORD)

        self.assertIsNone(weapon)

    def test_ToString(self):
        inventory = Inventory()

        test_string = '#######################################'
        test_string += '\n> RUSTY SWORD'
        test_string += '\ngold: 40'
        test_string += '\n#######################################\n'

        self.assertEqual(test_string, inventory.to_string())

    def test_ToStringTwoWeapons(self):
        inventory = Inventory()
        inventory.add_weapon(Weapon('GREAT SWORD'))

        test_string = '#######################################'
        test_string += '\n> RUSTY SWORD'
        test_string += '\n> GREAT SWORD'
        test_string += '\ngold: 40'
        test_string += '\n#######################################\n'

        self.assertEqual(test_string, inventory.to_string())

    def test_gold(self):
        inventory = Inventory()
        self.assertEqual(40, inventory.get_gold())

    def test_RemoveGold(self):
        inventory = Inventory()
        self.assertTrue(inventory.remove_gold(5))
        self.assertEqual(35, inventory.get_gold())

    def test_RemoveToMuchGold(self):
        inventory = Inventory()
        self.assertFalse(inventory.remove_gold(45))


if __name__ == '__main__':
    unittest.main()
