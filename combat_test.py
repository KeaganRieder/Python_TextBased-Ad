import unittest

from combat import Combat
from enemy import Raider, Mutant
from player import Player


class CombatTestCase(unittest.TestCase):

    def test_damage(self):
        player = Player('tim')
        monster = Raider()
        combat = Combat(monster, player)
        combat.attack()
        self.assertTrue(player.health >= 85)
        self.assertTrue(monster.health >= 105)
        self.assertTrue(player.health <= 100)
        self.assertTrue(monster.health <= 120)

    def test_Mutant_damage(self):
        player = Player('tim')
        monster = Mutant()
        combat = Combat(monster, player)
        combat.attack()
        self.assertTrue(player.health >= 85)
        self.assertTrue(monster.health >= 105)
        self.assertTrue(player.health <= 100)
        self.assertTrue(monster.health <= 200)


if __name__ == '__main__':
    unittest.main()
