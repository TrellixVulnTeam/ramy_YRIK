from game import Game

g = Game()

g.deck.shuffle()

g.give_first_cards()

# g.player1.hand.append(g.deck.give_card())

print(g.player1.hand)

g.run()