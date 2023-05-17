import unittest

from map import Map, Point


class PointTestCase(unittest.TestCase):

    def test_point_creation(self):
        point = Point(1, 2)

        self.assertEqual(1, point.x())
        self.assertEqual(2, point.y())


class MapTestCase(unittest.TestCase):

    def test_initialization(self):
        my_map = Map()

        map_layout = '=========================\n'
        map_layout += '| X | * | * | * | * | * |\n'
        map_layout += '=========================\n'
        map_layout += '| * | * | * | * | * | * |\n'
        map_layout += '=========================\n'
        map_layout += '| * | * | * | * | * | * |\n'
        map_layout += '=========================\n'
        map_layout += '| * | * | * | $ | * | * |\n'
        map_layout += '=========================\n'
        map_layout += '| * | * | * | * | * | * |\n'
        map_layout += '=========================\n'
        map_layout += '| * | * | * | * | * | * |\n'
        map_layout += '=========================\n'

        self.assertEqual(map_layout, my_map.show_map())

    def test_fog_cleared(self):
        my_map = Map()

        map_layout = '=========================\n'
        map_layout += '|   |   | * | * | * | * |\n'
        map_layout += '=========================\n'
        map_layout += '| * | X | * | * | * | * |\n'
        map_layout += '=========================\n'
        map_layout += '| * | * | * | * | * | * |\n'
        map_layout += '=========================\n'
        map_layout += '| * | * | * | $ | * | * |\n'
        map_layout += '=========================\n'
        map_layout += '| * | * | * | * | * | * |\n'
        map_layout += '=========================\n'
        map_layout += '| * | * | * | * | * | * |\n'
        map_layout += '=========================\n'

        my_map.move('east')
        my_map.move('south')

        self.assertEqual(map_layout, my_map.show_map())

    def test_get_map_info(self):
        my_map = Map()
        map_info = my_map.get_map_info(Point(1, 1))
        print(map_info.has_enemy)
        print(map_info.has_treasure)

    def test_player_valid_move_uppereast(self):
        my_map = Map()

        self.assertTrue(my_map.move('east'))
        self.assertTrue(my_map.move('east'))
        self.assertTrue(my_map.move('east'))
        self.assertTrue(my_map.move('east'))
        self.assertTrue(my_map.move('east'))
        self.assertFalse(my_map.move('east'))

    def test_player_valid_move_uppereast(self):
        my_map = Map()

        self.assertTrue(my_map.move('south'))
        self.assertTrue(my_map.move('south'))
        self.assertTrue(my_map.move('south'))
        self.assertTrue(my_map.move('south'))
        self.assertTrue(my_map.move('south'))
        self.assertFalse(my_map.move('south'))


if __name__ == '__main__':
    unittest.main()
