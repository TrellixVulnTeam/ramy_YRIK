import pygame
from deck import Deck

"""pygame.init()

win = pygame.display.set_mode((1300,750))

pygame.display.set_caption("Ramy")


exit_game = False
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True


pygame.quit()

"""

d = Deck()

d.shuffle()

print(d)

print(d.size())

print(d.count_suit_cards(0))
print(d.count_suit_cards(1))
print(d.count_suit_cards(2))
print(d.count_suit_cards(3))
print(d.count_suit_cards(4))

x = d.give_card()

print("Given card: ", x)

print(d)

print(d.size())

print(d.count_suit_cards(0))
print(d.count_suit_cards(1))
print(d.count_suit_cards(2))
print(d.count_suit_cards(3))
print(d.count_suit_cards(4))