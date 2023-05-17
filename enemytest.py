import unittest

from enemy import Combat


class CombatTestCase(unittest.TestCase):

    def test_fight(self):
        combat = Combat()

        testString = 'Your health: 120'
        testString += '1) Fight'
        testString += '2) run'
        self.assertEqual(testString, combat.Fight())


if __name__ == '__main__':
    unittest.main()
