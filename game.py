import pygame
import os
from deck import Deck
from player import Player


class Game(object):
    def __init__(self):
        self.player1 = Player("Joao")
        self.player2 = Player("Diogo")
        self.deck = Deck()
        self.pile = []
        self.height = 750
        self.width = 1300
        self.win = pygame.display.set_mode((self.width, self.height))
        self.activePlayer = self.player1
        self.inactivePlayer = self.player2
        self.status = (1, 0)
        self.lastHand = []
        self.lastHandSelected = []
        self.checkedCombinations = []

    def give_first_cards(self):
        for i in range(13):
            self.player1.hand.append(self.deck.give_card())
        for f in range(13):
            self.player2.hand.append(self.deck.give_card())

        self.pile.append(self.deck.give_card())

    def run(self):

        pygame.init()
        print(self.pile)
        while self.status[0] != 0:

            if self.status[0] == 1:
                self.draw_menu()
                self.menu_logic()

            if self.status[0] == 2:
                self.draw_board()
                self.game_logic()

            pygame.display.update()

        pygame.quit()

    def draw_menu(self):
        text1 = pygame.font.SysFont(None, 25).render("PLAY", True, (0, 0, 0))
        text2 = pygame.font.SysFont(None, 25).render("RULES", True, (0, 0, 0))

        self.win.fill((0, 0, 0))
        pygame.draw.rect(self.win, (255, 0, 0), pygame.Rect(575, 200, 150, 75))
        pygame.draw.rect(self.win, (255, 0, 0), pygame.Rect(575, 300, 150, 75))
        self.win.blit(text1, (630, 230))
        self.win.blit(text2, (625, 330))

    def draw_board(self):
        self.win.fill((34, 139, 34))
        x = 300
        aux = self.activePlayer.hand

        name = pygame.font.SysFont(None, 50).render(self.activePlayer.name, True, (0, 0, 0))
        self.win.blit(name, (50, 680))

        if self.status != (2, 3):
            for i in range(len(aux)):
                img = pygame.transform.scale(pygame.image.load(os.path.join("resources/cards", str(aux[i][0]) + "_" + str(aux[i][1]) + ".png")), (125, 182))
                if i == self.activePlayer.selected:
                    self.win.blit(img, (x, 655))
                else:
                    self.win.blit(img, (x, 675))
                x = x + 50

        x = 300

        for i in range(len(self.inactivePlayer.hand)):
            img = pygame.transform.scale(pygame.image.load(os.path.join("resources/cards", "back.png")), (125, 182))

            self.win.blit(img, (x, -75))

            x = x + 50

        self.win.blit(img, (50, 300))

        if len(self.pile) is not 0:
            img = pygame.transform.scale(pygame.image.load(os.path.join("resources/cards", str(self.pile[0][0]) + "_" + str(self.pile[0][1]) + ".png")), (125, 182))
            self.win.blit(img, (600, 300))

        if self.status == (2, 1) and self.activePlayer.selected != -1:
            text1 = pygame.font.SysFont(None, 25).render("Give Card", True, (0, 0, 0))
            text2 = pygame.font.SysFont(None, 25).render("Finish game", True, (0, 0, 0))
            pygame.draw.rect(self.win, (255, 0, 0), pygame.Rect(1070, 350, 150, 75))
            pygame.draw.rect(self.win, (255, 0, 0), pygame.Rect(1070, 450, 150, 75))
            self.win.blit(text1, (1105, 380))
            self.win.blit(text2, (1100, 480))

        if self.status == (2, 2):
            text = pygame.font.SysFont(None, 60).render("PRESS THE MOUSE ANYWHERE TO SWITCH PLAYERS", True, (0, 0, 255))

            self.win.fill((0, 0, 0))
            self.win.blit(text, (100, 375))

    def menu_logic(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.status = (0, 0)

            pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 575 <= pos[0] <= 725 and 200 <= pos[1] <= 275:
                    self.status = (2, 0)

    def game_logic(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.status = (0, 0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x1 = 300
                x2 = 350
                if self.status[1] != 2 and self.status[1] != 3:
                    for i in range(len(self.activePlayer.hand)):
                        if i == len(self.activePlayer.hand) - 1:
                            x2 = x2 + 75
                        if x1 <= pos[0] <= x2 and 675 <= pos[1] <= 750:
                            if self.activePlayer.selected == -1:
                                self.activePlayer.selected = i
                            else:
                                self.switch_cards(i, self.activePlayer.selected)
                        x1 = x1 + 50
                        x2 = x2 + 50
                # Player gets a card from the deck or from the pit
                if self.status[1] == 0:
                    if 50 <= pos[0] <= 175 and 300 <= pos[1] <= 482:
                        self.activePlayer.hand.append(self.deck.give_card())
                        self.status = (2, 1)
                    if 600 <= pos[0] <= 725 and 300 <= pos[1] <= 482 and len(self.pile) is not 0:
                        self.activePlayer.hand.append(self.pile.pop(0))
                        self.status = (2, 1)
                # Player gives one of his 14 cards to the pit or finishes the round
                if self.status[1] == 1:
                    if 1070 <= pos[0] <= 1220 and 350 <= pos[1] <= 425 and self.activePlayer.selected != -1:
                        self.pile.insert(0, self.activePlayer.hand.pop(self.activePlayer.selected))
                        self.activePlayer.selected = -1
                        self.status = (2, 2)
                        self.switch_player()
                        return
                    if 1070 <= pos[0] <= 1220 and 450 <= pos[1] <= 525 and self.activePlayer.selected != -1:
                        self.status = (2, 3)
                        self.lastHand.clear()
                        self.lastHand = self.activePlayer.hand
                        return

                # Player clicks the screen to give the turn to the next player
                if self.status[1] == 2:
                    self.status = (2, 0)
                    return

                if self.status[1] == 3:
                    for i in range(len(self.lastHand)):
                        if i == len(self.lastHand) - 1:
                            x2 = x2 + 75
                        if x1 <= pos[0] <= x2 and 675 <= pos[1] <= 750:
                            if self.lastHandSelected.count(self.lastHand[i]) == 0:
                                self.lastHandSelected.append(self.lastHand[i])
                            else:
                                self.lastHandSelected.remove(self.lastHand[i])

                        x1 = x1 + 50
                        x2 = x2 + 50

    def switch_cards(self, pos1, pos2):
        if pos1 == pos2:
            self.activePlayer.selected = -1
            return

        aux = self.activePlayer.hand[pos1]

        self.activePlayer.hand[pos1] = self.activePlayer.hand[pos2]

        self.activePlayer.hand[pos2] = aux

        self.activePlayer.selected = - 1

    def switch_player(self):
        aux = self.activePlayer

        self.activePlayer = self.inactivePlayer
        self.inactivePlayer = aux
