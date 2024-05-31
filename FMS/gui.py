import pygame
import constants as const

class GUI:
    def __init__(self, screen, assets):
        pygame.font.init()
        self.screen = screen
        self.font = assets['font']

        # Define GUI elements
        self.elements = {
            'money': self.create_text_element('Money: $100', (10, 10)),
            'season': self.create_text_element('Season: Spring', (10, 50)),
            'weather': self.create_text_element('Weather: Sunny', (10, 90)),
        }

    def create_text_element(self, text, position):
        return {
            'surface': self.font.render(text, True, const.BLACK),
            'position': position,
        }

    def update_element(self, element, new_text):
        self.elements[element]['surface'] = self.font.render(new_text, True, const.BLACK)

    def update(self, money, season, weather):
        self.update_element('money', f'Money: ${money}')
        self.update_element('season', f'Season: {season}')
        self.update_element('weather', f'Weather: {weather}')

    def draw(self):
        for element in self.elements.values():
            self.screen.blit(element['surface'], element['position'])

