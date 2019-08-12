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
        status = 1

        pygame.init()

        while status != 0:

            if status == 1:
                self.draw_menu()
                status = self.menu_logic()

            if status == 2:
                self.draw()
                self.draw_player_hand()
                status = self.game_logic()

            pygame.display.update()

        pygame.quit()

    def draw(self):
        self.win.fill((34, 139, 34))

    def draw_menu(self):
        text1 = pygame.font.SysFont(None, 25).render("PLAY", True, (0, 0, 0))
        text2 = pygame.font.SysFont(None, 25).render("RULES", True, (0, 0, 0))

        self.win.fill((0, 0, 0))
        pygame.draw.rect(self.win, (255, 0, 0), pygame.Rect(575, 200, 150, 75))
        pygame.draw.rect(self.win, (255, 0, 0), pygame.Rect(575, 300, 150, 75))
        self.win.blit(text1, (630, 230))
        self.win.blit(text2, (625, 330))

    def draw_player_hand(self):
        x = 300
        aux = self.player1.hand

        for i in range(len(aux)):
            img = pygame.transform.scale(pygame.image.load(os.path.join("resources/cards", str(aux[i][0]) + "_" + str(aux[i][1]) +".png")), (125, 182))
            self.win.blit(img, (x, 675))
            x = x + 50

    def menu_logic(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0

            pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 575 <= pos[0] <= 725 and 200 <= pos[1] <= 275:
                    return 2

        return 1

    def game_logic(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0

        return 2