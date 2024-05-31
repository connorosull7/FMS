# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player settings
PLAYER_START_X = SCREEN_WIDTH // 2
PLAYER_START_Y = SCREEN_HEIGHT // 2
PLAYER_SPEED = 5
PLAYER_HEALTH = 100

# Crop settings
CROP_GROWTH_TIME = 10  # Number of updates to grow

# Animal settings
ANIMAL_HEALTH = 100
ANIMAL_HUNGER = 100

# Market settings
INITIAL_CROP_PRICE = 10
INITIAL_ANIMAL_PRICE = 50
INITIAL_PRODUCE_PRICE = 5
INITIAL_CROP_SUPPLY = 100
INITIAL_ANIMAL_SUPPLY = 50
INITIAL_PRODUCE_SUPPLY = 200
INITIAL_CROP_DEMAND = 50
INITIAL_ANIMAL_DEMAND = 25
INITIAL_PRODUCE_DEMAND = 100

# Weather settings
WEATHER_UPDATE_INTERVAL = 60  # Number of updates to change weather

# Game settings
FPS = 60
BACKGROUND_COLOR = WHITE

# Farm assets
CROPS = {
    "wheat": {"growth_time": 5, "price": 15},
    "corn": {"growth_time": 7, "price": 20},
    "carrot": {"growth_time": 4, "price": 10},
}

ANIMALS = {
    "chicken": {"health": 100, "hunger": 100, "price": 20},
    "cow": {"health": 150, "hunger": 150, "price": 50},
    "sheep": {"health": 120, "hunger": 120, "price": 40},
}

RESOURCES = {
    "water": {"price": 1},
    "feed": {"price": 2},
    "fertilizer": {"price": 5},
}
