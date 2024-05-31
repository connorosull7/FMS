import pygame
from assets import load_assets

class Interface:
    def __init__(self, screen):
        self.screen = screen
        self.assets = load_assets()
        self.buttons = []
        self.tooltips = []
        self.animations = []

    def create_button(self, text, position, size, callback, state='normal'):
        button = Button(text, position, size, callback, self.assets, state)
        self.buttons.append(button)

    def create_tooltip(self, text, position, delay=500):
        tooltip = Tooltip(text, position, self.assets, delay)
        self.tooltips.append(tooltip)

    def create_animation(self, images, position, speed, anim_type='loop'):
        animation = Animation(images, position, speed, anim_type)
        self.animations.append(animation)

    def update(self):
        for button in self.buttons:
            button.update()
        for animation in self.animations:
            animation.update()
        self.check_tooltips()

    def draw(self):
        for button in self.buttons:
            button.draw(self.screen)
        for tooltip in self.tooltips:
            tooltip.draw(self.screen)
        for animation in self.animations:
            animation.draw(self.screen)

    def check_tooltips(self):
        mouse_pos = pygame.mouse.get_pos()
        for tooltip in self.tooltips:
            tooltip.update_visibility(mouse_pos)

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)

class Button:
    def __init__(self, text, position, size, callback, assets, state='normal'):
        self.text = text
        self.position = position
        self.size = size
        self.callback = callback
        self.assets = assets
        self.state = state
        self.rect = pygame.Rect(position, size)
        self.font = assets['font']
        self.images = {
            'normal': assets['button_normal'],
            'hover': assets['button_hover'],
            'pressed': assets['button_pressed'],
            'disabled': assets['button_disabled'],
            'active': assets['button_active']
        }

    def update(self):
        if self.state == 'disabled':
            return
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        if self.rect.collidepoint(mouse_pos):
            if mouse_click[0]:
                self.state = 'pressed'
                self.callback()
            else:
                self.state = 'hover'
        else:
            self.state = 'normal'

    def draw(self, screen):
        image = self.images[self.state]
        screen.blit(image, self.position)
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surf, text_surf.get_rect(center=self.rect.center))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and self.state != 'disabled':
                self.callback()

class Tooltip:
    def __init__(self, text, position, assets, delay=500):
        self.text = text
        self.position = position
        self.assets = assets
        self.font = assets['font']
        self.visible = False
        self.rect = pygame.Rect(position, (200, 50))  # Example size
        self.delay = delay
        self.show_time = 0

    def update_visibility(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if not self.visible:
                self.show_time = pygame.time.get_ticks()
            elif pygame.time.get_ticks() - self.show_time > self.delay:
                self.visible = True
        else:
            self.visible = False
            self.show_time = 0

    def draw(self, screen):
        if self.visible:
            text_surf = self.font.render(self.text, True, (255, 255, 255))
            screen.blit(text_surf, self.position)

class Animation:
    def __init__(self, images, position, speed, anim_type='loop'):
        self.images = images
        self.position = position
        self.speed = speed
        self.type = anim_type
        self.index = 0
        self.timer = 0

    def update(self):
        self.timer += 1
        if self.timer >= self.speed:
            self.timer = 0
            self.index = (self.index + 1) % len(self.images)
            if self.type == 'once' and self.index == len(self.images) - 1:
                self.index = len(self.images) - 1

    def draw(self, screen):
        screen.blit(self.images[self.index], self.position)
