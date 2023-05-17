import unittest
from weapon import Weapon


class WeaponTestCase(unittest.TestCase):

    def test_get_weapon_list(self):
        self.assertEqual(4, len(Weapon.get_weapon_list()))

    def test_GetWeaponDamageDefault(self):
        weapon = Weapon()
        self.assertEqual(5, weapon.get_weapon_damage())

    def test_WeaponDamage(self):
        weapon = Weapon(Weapon.GREAT_SWORD)
        self.assertEqual(15, weapon.get_weapon_damage())

    def test_WeaponValue(self):
        weapon = Weapon(Weapon.GREAT_SWORD)
        self.assertEqual(40, weapon.get_weapon_value())

    def test_WeaponType(self):
        weapon = Weapon()
        self.assertEqual(Weapon.RUSTY_SWORD, weapon.get_weapon_type())

    def test_compareEquality(self):
        weapon1 = Weapon(Weapon.BATTLE_AXE)
        weapon2 = Weapon(Weapon.BATTLE_AXE)

        self.assertTrue(weapon1 == weapon2)

    def test_compareNotQEqual(self):
        weapon1 = Weapon(Weapon.BATTLE_AXE)
        weapon2 = Weapon(Weapon.GREAT_SWORD)

        self.assertFalse(weapon1 == weapon2)

    def test_rustysword(self):
        weapon = Weapon()
        self.assertEqual(5, weapon.get_weapon_damage())


if __name__ == '__main__':
    unittest.main()
