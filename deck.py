import random


class Deck(object):
    def __init__(self):
        self.cards = []

        self.create()

    def __str__(self):
        return str(self.cards)

    def size(self):
        return len(self.cards)

    def create(self):
        self.cards.clear()
        for j in range(2):
            for i in range(1, 5):
                for f in range(1,14):
                    self.cards.append((f, i))
        for i in range (4):
            self.cards.append((0, 0))

    def shuffle(self):
        for i in range(self.size()):
            new_pos = random.randint(0, self.size() - 1)
            aux = self.cards[i]
            self.cards[i] = self.cards[new_pos]
            self.cards[new_pos] = aux

    def count_suit_cards(self, suit):
        count = 0
        for i in range(self.size()):
            if self.cards[i][1] == suit:
                count += 1
        return count

    def give_card(self):
        return self.cards.pop(0)
