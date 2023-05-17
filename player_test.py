import unittest
from player import Player
from weapon import Weapon


class PlayerTestCase(unittest.TestCase):

    def test_PlayerPosition(self):
        player = Player("Tom")
        self.assertEqual(7, player.player_location())

    def test_Damage(self):
        player = Player("Tom")
        self.assertEqual(15, player.damage())

    def test_equip_sword_inventory(self):
        player = Player("Tom")
        self.assertTrue(player.equip_weapon(Weapon.RUSTY_SWORD))

    def test_equip_sword_not_in_inv(self):
        player = Player("Tom")
        self.assertFalse(player.equip_weapon(Weapon.GREAT_SWORD))

    def test_rest_full_health(self):
        player = Player('tim')
        player.rest()
        self.assertEqual(100, player.health)

    def test_rest_damage_taken(self):
        player = Player('tim')
        player.health = 40
        player.rest()
        self.assertLessEqual(50, player.health)
        self.assertGreaterEqual(70,player.health)


if __name__ == '__main__':
    unittest.main()
