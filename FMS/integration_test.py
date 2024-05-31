import pygame
from player import Player
from farm import Farm
from market import Market
from weather import Weather
from gui import GUI
from interface import Interface
from assets import load_assets

def integration_test():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    # Load assets
    assets = load_assets()

    # Initialize components
    player = Player((400, 300), assets)
    farm = Farm()
    market = Market()
    weather = Weather()
    gui = GUI(screen, assets)
    interface = Interface(screen)

    # Create example buttons and tooltips
    interface.create_button("Buy Seeds", (50, 50), (100, 50), lambda: print("Buying seeds!"))
    interface.create_tooltip("This is a tooltip", (200, 50))

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            interface.handle_event(event)

        # Update components
        player.update()
        farm.update()
        market.update()
        weather.update()
        interface.update()

        # Draw components
        screen.fill((255, 255, 255))
        player.draw(screen)
        farm.draw(screen)
        gui.draw()
        interface.draw()

        # Update display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    integration_test()
