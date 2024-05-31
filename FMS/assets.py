import pygame
import os

def load_image(file_name, placeholder_name):
    try:
        image = pygame.image.load(file_name)
        return image
    except pygame.error as e:
        print(f"Warning: {file_name} not found, using placeholder.")
        return pygame.image.load(placeholder_name)

def load_assets():
    assets = {}

    try:
        assets['crops'] = {
            'wheat': [
                load_image('assets/crops/wheat_seedling.png', 'assets/placeholder.png'),
                load_image('assets/crops/wheat_growing.png', 'assets/placeholder.png'),
                load_image('assets/crops/wheat_mature.png', 'assets/placeholder.png')
            ],
            'corn': [
                load_image('assets/crops/corn_seedling.png', 'assets/placeholder.png'),
                load_image('assets/crops/corn_growing.png', 'assets/placeholder.png'),
                load_image('assets/crops/corn_mature.png', 'assets/placeholder.png')
            ],
            'carrot': [
                load_image('assets/crops/carrot_seedling.png', 'assets/placeholder.png'),
                load_image('assets/crops/carrot_growing.png', 'assets/placeholder.png'),
                load_image('assets/crops/carrot_mature.png', 'assets/placeholder.png')
            ]
        }
    except FileNotFoundError:
        print("Warning: Crop images not found, using placeholders.")
        assets['crops'] = {
            'wheat': [pygame.Surface((20, 20)) for _ in range(3)],
            'corn': [pygame.Surface((20, 20)) for _ in range(3)],
            'carrot': [pygame.Surface((20, 20)) for _ in range(3)],
        }
        for crop_stage in assets['crops']['wheat']:
            crop_stage.fill((255, 255, 0))  # Fill with yellow as a placeholder
        for crop_stage in assets['crops']['corn']:
            crop_stage.fill((255, 223, 0))  # Fill with a different yellow as a placeholder
        for crop_stage in assets['crops']['carrot']:
            crop_stage.fill((255, 165, 0))  # Fill with orange as a placeholder

    try:
        assets['animals'] = {
            'chicken': load_image('assets/animals/chicken.png', 'assets/placeholder.png'),
            'cow': load_image('assets/animals/cow.png', 'assets/placeholder.png'),
            'sheep': load_image('assets/animals/sheep.png', 'assets/placeholder.png'),
        }
    except FileNotFoundError:
        print("Warning: Animal images not found, using placeholders.")
        assets['animals'] = {
            'chicken': pygame.Surface((20, 20)),
            'cow': pygame.Surface((20, 20)),
            'sheep': pygame.Surface((20, 20)),
        }
        assets['animals']['chicken'].fill((255, 255, 0))  # Fill with yellow as a placeholder
        assets['animals']['cow'].fill((255, 223, 0))      # Fill with a different yellow as a placeholder
        assets['animals']['sheep'].fill((255, 165, 0))    # Fill with orange as a placeholder

    try:
        assets['farmhouse'] = load_image('assets/buildings/farmhouse.png', 'assets/placeholder.png')
    except FileNotFoundError:
        print("Warning: Farmhouse image not found, using placeholder.")
        assets['farmhouse'] = pygame.Surface((50, 50))
        assets['farmhouse'].fill((139, 69, 19))  # Fill with brown as a placeholder

    ui_elements = ['button_normal', 'button_hover', 'button_pressed', 'button_disabled', 'button_active']
    for element in ui_elements:
        try:
            assets[element] = load_image(f'assets/ui/{element}.png', 'assets/placeholder.png')
        except FileNotFoundError:
            print(f"Warning: {element}.png not found, using placeholder.")
            assets[element] = pygame.Surface((100, 50))
            assets[element].fill((200, 200, 200))  # Fill with gray as a placeholder

    return assets
