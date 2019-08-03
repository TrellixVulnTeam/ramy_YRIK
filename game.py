import pygame
import os
from deck import Deck
from player import Player


class Game(object):
    def __init__(self):
        self.player1 = Player("Joao")
        self.player2 = Player("Diogo")
        self.deck = Deck()
        self.pile = (-1, -1)
        self.height = 750
        self.width = 1300
        self.win = pygame.display.set_mode((self.width, self.height))

    def give_first_cards(self):
        for i in range(13):
            self.player1.hand.append(self.deck.give_card())
        for f in range(13):
            self.player2.hand.append(self.deck.give_card())

        self.pile = self.deck.give_card()

    def run(self):
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.draw()
            self.draw_player_hand()
            pygame.display.update()

        pygame.quit()

    def draw(self):
        self.win.fill((34, 139, 34))

    def draw_player_hand(self):
        x = 300
        aux = self.player1.hand

        for i in range(len(aux)):
            img = pygame.transform.scale(pygame.image.load(os.path.join("resources/cards", str(aux[i][0]) + "_" + str(aux[i][1]) +".png")), (125, 182))
            self.win.blit(img, (x, 675))
            x = x + 50