from map import Map


# class to play out the story of the game
class GameStory:
    def __init__(self):
        self.storyLinePosition = 1
        self.game_map = Map()

    def move_story(self):
        self.storyLinePosition += 1

    def get_story_position(self):
        return self.storyLinePosition

    def get_map(self):
        return self.game_map

    def is_valid(self, option):
        return self.game_map.is_valid_option(option.upper())

    #clear the current section of the map called after treasure collected or enemy killed
    def map_cleared(self):
        self.game_map.clear_map()
