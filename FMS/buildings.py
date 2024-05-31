import pygame
from assets import load_assets

class Building:
    def __init__(self, building_type, x, y):
        self.building_type = building_type
        self.image = load_assets()['buildings'][building_type]
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Farmhouse(Building):
    def __init__(self, x, y):
        super().__init__('farmhouse', x, y)

class Barn(Building):
    def __init__(self, x, y):
        super().__init__('barn', x, y)
