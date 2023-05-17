from random import randint

from enemy import Raider, MutantAnt, GientSpider, Mutant, ForgottenOne


# class to handle storing the x and y position (point) of the player
class Point:
    PLAYER_STARTING_X = 0
    PLAYER_STARTING_Y = 0

    def __init__(self, x=PLAYER_STARTING_X, y=PLAYER_STARTING_Y):
        self.coord = (x, y)

    def x(self):
        return self.coord[0]

    def y(self):
        return self.coord[1]

    # To handle comparing one point to another point.
    # https: // docs.python.org / 3 / reference / datamodel.html  # object.__eq__
    def __eq__(self, other):
        return (
                self.__class__ == other.__class__ and
                self.coord == other.coord)


# class to handle defining what it within a grid cell in the map
class MapInfo:

    # create the map grid and randomly with enemy or treasure or nothing
    # all monster are seeded based on equal change
    # called when a object in created
    # https: // docs.python.org / 3 / reference / datamodel.html  # object.__init__
    def __init__(self):
        map_seed = randint(1, 15)
        self.treasureGold = 0
        self.has_treasure = False
        self.is_store = False
        self.has_explored = False

        if map_seed == 1:
            self.enemy = Raider()
            self.has_enemy = True
        elif map_seed == 2:
            self.enemy = MutantAnt()
            self.has_enemy = True
        elif map_seed == 3:
            self.enemy = GientSpider()
            self.has_enemy = True
        elif map_seed == 4:
            self.enemy = Mutant()
            self.has_enemy = True
        elif map_seed == 5:
            self.enemy = ForgottenOne()
            self.has_enemy = True
        elif map_seed == 6:
            self.has_treasure = True
            self.treasureGold = 100
        else:
            self.has_enemy = False

    # set the location as the store
    def set_as_store(self):
        self.is_store = True
        self.has_treasure = False
        self.has_enemy = False

    # used to clear the monster from this cell after they die
    def enemy_dead(self):
        self.has_enemy = False

    # indicates if the gold has been collected
    def gold_collected(self):
        self.has_treasure = False

    def player_has_explored(self):
        self.has_explored = True

    # to output the class as a string and help in displaying the map
    # https://docs.python.org/3/reference/datamodel.html#object.__str__
    def __str__(self):

        if self.is_store:
            return '$'
        elif self.has_explored:
            return ' '
        else:
            return '*'


# The class that represents the overall map in the game. currently is 6 x 6 map
# as defined in the map creation
class Map:
    # Create the constant for Max Width by Max Depth
    MAP_X = 6
    MAP_Y = 6
    DIRECTION = {'WEST': -1, 'EAST': +1, 'SOUTH': +1, 'NORTH': -1}

    # Create the Game Map
    def __init__(self):
        self._map = [[MapInfo() for x in range(Map.MAP_X)] for y in
                     range(Map.MAP_Y)]  # Create a list containing 6 (MAP_X) lists, each of 6 items, all set to 0
        self._player_location = Point()

        self._map[3][3].set_as_store()
        self.storeLocation = Point(3, 3)
        self.has_explored()

    def get_map_info(self, point):
        return self._map[point.x()][point.y()]

    @staticmethod
    def draw_border():
        map_border = ''
        for x in range(Map.MAP_X):
            map_border += '===='
        return map_border + '=\n'

    # display the map
    def show_map(self):
        map_output = self.draw_border()
        for y in range(0, Map.MAP_Y):
            for x in range(0, Map.MAP_X):
                map_output += '|'
                map_info = self._map[x][y]
                if self._player_location == Point(x, y):
                    map_output += ' X '

                else:
                    map_output += ' {0} '.format(map_info)

            map_output += '|\n'
            map_output += self.draw_border()

        return map_output

    # Function to move the player
    def move(self, direction):
        compass = str(direction).upper()
        amount = Map.DIRECTION[compass]
        y = 0
        x = 0
        if compass == 'NORTH' or compass == 'SOUTH':
            y = amount

        elif compass == 'EAST' or compass == 'WEST':
            x = amount

        y = self._player_location.y() + y
        x = self._player_location.x() + x

        # check if this is a valid X and Y move
        if x < 0 or x >= Map.MAP_X:
            return False

        if y < 0 or y >= Map.MAP_Y:
            return False

        self._player_location = Point(x, y)

        # now indicate the play has looked at this location
        self.has_explored()

        return True

    def map_location_option(self):
        map_info = self._map[self._player_location.x()][self._player_location.y()]

        location_option = ''

        if map_info.has_treasure:
            location_option += "6) Open"
        elif map_info.has_enemy:
            location_option += "6) Fight"
        elif map_info.is_store:
            location_option += "6) shop"
        return location_option

    def is_valid_option(self, option):
        map_info = self._map[self._player_location.x()][self._player_location.y()]
        is_valid = False

        if option == 'OPEN' and map_info.has_treasure:
            is_valid = True
        elif option == 'FIGHT' and map_info.has_enemy:
            is_valid = True
        elif option == 'SHOP' and map_info.is_store:
            is_valid = True

        return is_valid

    # used to get the enemy if one exists for this map cell
    def get_enemy(self):
        map_info = self._map[self._player_location.x()][self._player_location.y()]
        return map_info.enemy

    # used to indicate if the player has explored this map
    def has_explored(self):
        map_info = self._map[self._player_location.x()][self._player_location.y()]
        map_info.has_explored = True

    def clear_map(self):
        map_info = self._map[self._player_location.x()][self._player_location.y()]
        map_info.enemy_dead()
        map_info.gold_collected()