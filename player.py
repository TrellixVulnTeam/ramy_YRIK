import pygame

class player(object):
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.hand = []

    def add_points(self, p):
        self.points += p
