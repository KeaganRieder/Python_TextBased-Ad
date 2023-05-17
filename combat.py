from random import randint


class Combat:

    def __init__(self, monster, player):
        self.monster = monster
        self.player = player

    def attack(self):
        # setting up chance for player to hit
        hit_chance = randint(1, 10)
        # The players damage could be 100% or could be a miss
        if hit_chance == 2 or hit_chance == 4 or hit_chance == 6 or hit_chance == 8:
            player_damage = self.player.damage() * 1
        else:
            player_damage = self.monster.damage() * 0

        # The monster damage could be 100% or could be a miss
        if hit_chance == 2 or hit_chance == 4:
            monster_damage = self.monster.damage() * 1
        else:
            monster_damage = self.monster.damage() * 0

        # Remove the amount of damage from the players health
        self.player.health -= monster_damage

        # Remove the amount of damage from the monsters health
        self.monster.health -= player_damage
