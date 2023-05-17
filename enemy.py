class Monster():
    def __init__(self, name, health, attack, goldgain):
        self.name = name
        self.maxhealth = health
        self.health = health
        self.attack = attack
        self.goldgain = goldgain

    def _collect_gold(self):
        return self.goldgain

    def damage(self):
        return self.attack

    def get_health(self):
        return self.health


class Raider(Monster):
    def __init__(self):
        Monster.__init__(self, 'Raider', 120, 15, 50)


class MutantAnt(Monster):
    def __init__(self):
        Monster.__init__(self, 'Mutant Ant', 50, 5, 10)


class GientSpider(Monster):
    def __init__(self):
        Monster.__init__(self, 'Gient Spider', 100, 10, 30)


class Mutant(Monster):
    def __init__(self):
        Monster.__init__(self, 'Mutant', 200, 15, 50)


class ForgottenOne(Monster):
    def __init__(self):
        Monster.__init__(self, 'Forgotten One', 150, 15, 50)
