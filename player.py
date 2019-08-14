class Player(object):
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.hand = []
        self.selected = -1

    def add_points(self, p):
        self.points += p

    def clear_hand(self):
        self.hand.clear()