import pygame
from assets import load_assets
from player import Player
from farm import Farm
from market import Market
from weather import Weather
from gui import GUI
from interface import Interface
from saves import save_game, load_game

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Farm Manager Simulator")

# Load assets
assets = load_assets()

# Initialize game components
player = Player((100, 100), assets)
farm = Farm()
market = Market()
weather = Weather()
gui = GUI(screen, assets)
interface = Interface(screen)

# Create example buttons and tooltips
interface.create_button("Buy Seeds", (50, 50), (100, 50), lambda: print("Buying seeds!"))
interface.create_tooltip("This is a tooltip", (200, 50))

# Load game if save file exists
try:
    load_game(player, farm)
except FileNotFoundError:
    print("No save file found. Starting a new game.")

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_game(player, farm)
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.plant_crop(farm, 'wheat', 5, 5)
            if event.key == pygame.K_w:
                player.water_crop(farm, 5, 5)
            if event.key == pygame.K_h:
                player.harvest_crop(farm, 5, 5)
        interface.handle_event(event)

    # Update game components
    player.update()
    farm.update()
    market.update()
    weather.update()
    interface.update()

    # Draw game components
    screen.fill((255, 255, 255))
    player.draw(screen)
    farm.draw(screen)
    gui.draw()
    interface.draw()

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
