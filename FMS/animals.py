import pygame
from assets import load_assets
import constants as const
from pathfinding import Pathfinding

class Animal:
    def __init__(self, animal_type, x, y, grid):
        self.animal_type = animal_type
        self.image = load_assets()['animals'][animal_type]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.health = const.ANIMALS[animal_type]['health']
        self.hunger = const.ANIMALS[animal_type]['hunger']
        self.pathfinding = Pathfinding(grid)
        self.target = None
        self.path = []

    def set_target(self, target):
        self.target = target
        self.path = self.pathfinding.a_star_search(self.rect.topleft, self.target)

    def update(self):
        self.hunger -= 1
        if self.hunger <= 0:
            self.health -= 1
            self.hunger = 0
        if self.path:
            next_step = self.path.pop(0)
            self.rect.topleft = next_step

    def feed(self):
        self.hunger = const.ANIMALS[self.animal_type]['hunger']
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
