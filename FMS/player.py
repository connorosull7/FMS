import pygame
from inventory import Inventory, Item

class Farm:
    def __init__(self):
        self.crops = []
        self.animals = []
        self.plots = [[None for _ in range(10)] for _ in range(10)]  # Example grid for plots

    def plant_crop(self, crop_type, x, y):
        if self.plots[x][y] is None:
            crop = crop(crop_type, x * 40, y * 40)  # Example size and position
            self.crops.append(crop)
            self.plots[x][y] = crop

    def add_animal(self, animal_type, x, y):
        animal = animal(animal_type, x, y)
        self.animals.append(animal)

    def update(self):
        for crop in self.crops:
            crop.update()
        for animal in self.animals:
            animal.update()

    def draw(self, screen):
        for crop in self.crops:
            crop.draw(screen)
        for animal in self.animals:
            animal.draw(screen)

class Player:
    def __init__(self, position, assets):
        self.rect = pygame.Rect(position, (50, 50))  # Example size
        self.speed = 5  # Example speed
        self.inventory = Inventory()
        self.assets = assets
        self.money = 100  # Example starting money

    def move(self, dx=0, dy=0):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def plant_crop(self, farm, crop_type, x, y):
        if self.money >= const.CROPS[crop_type]['price']:
            farm.plant_crop(crop_type, x, y)
            self.money -= const.CROPS[crop_type]['price']

    def water_crop(self, farm, x, y):
        if farm.plots[x][y]:
            farm.plots[x][y].water()

    def harvest_crop(self, farm, x, y):
        if farm.plots[x][y] and farm.plots[x][y].growth_stage == farm.plots[x][y].growth_time:
            crop = farm.plots[x][y]
            self.inventory.add_item(Item(crop.crop_type, 1))
            farm.plots[x][y] = None
            farm.crops.remove(crop)
            self.money += crop.price  # Earn money from harvesting

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)  # Example draw method
