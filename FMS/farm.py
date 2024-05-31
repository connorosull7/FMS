import pygame
import constants as const
from assets import load_assets

class Crop:
    def __init__(self, crop_type, x, y):
        self.crop_type = crop_type
        self.images = load_assets()['crops'][crop_type]
        self.rect = self.images[0].get_rect(topleft=(x, y))
        self.growth_stage = 0
        self.growth_time = const.CROPS[crop_type]['growth_time']
        self.price = const.CROPS[crop_type]['price']
        self.watered = False
        self.water_status = 100

    def water(self):
        self.watered = True
        self.water_status = 100

    def update(self):
        if self.water_status > 0:
            self.water_status -= 1
        if self.watered and self.growth_stage < self.growth_time:
            self.growth_stage += 1
            self.rect = self.images[self.growth_stage].get_rect(topleft=self.rect.topleft)
            if self.growth_stage == self.growth_time:
                self.watered = False  # Stop watering when fully grown

    def draw(self, screen):
        screen.blit(self.images[self.growth_stage], self.rect)
        self.draw_status_bar(screen)

    def draw_status_bar(self, screen):
        # Draw water status bar
        bar_color = (0, 0, 255)  # Blue
        bar_background = (255, 0, 0)  # Red
        bar_position = (self.rect.x, self.rect.y - 10, self.rect.width, 5)
        pygame.draw.rect(screen, bar_background, bar_position)
        pygame.draw.rect(screen, bar_color, (self.rect.x, self.rect.y - 10, self.rect.width * (self.water_status / 100), 5))

class Animal:
    def __init__(self, animal_type, x, y):
        self.animal_type = animal_type
        self.image = load_assets()['animals'][animal_type]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.health = const.ANIMALS[animal_type]['health']
        self.hunger = const.ANIMALS[animal_type]['hunger']
        self.price = const.ANIMALS[animal_type]['price']

    def feed(self):
        self.hunger = 100

    def update(self):
        if self.hunger > 0:
            self.hunger -= 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Farm:
    def __init__(self):
        self.crops = []
        self.animals = []
        self.buildings = [Farmhouse(400, 300)]  # Example building

    def add_crop(self, crop_type, x, y):
        self.crops.append(Crop(crop_type, x, y))

    def add_animal(self, animal_type, x, y):
        self.animals.append(Animal(animal_type, x, y))

    def update(self):
        for crop in self.crops:
            crop.update()
        for animal in self.animals:
            animal.update()

    def draw(self, screen):
        for building in self.buildings:
            building.draw(screen)
        for crop in self.crops:
            crop.draw(screen)
        for animal in self.animals:
            animal.draw(screen)

class Farmhouse(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        assets = load_assets()
        self.image = assets['farmhouse']
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
