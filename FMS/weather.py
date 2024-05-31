# weather.py

import pygame
import constants as const
import random

class Weather:
    def __init__(self):
        self.current_weather = "sunny"
        self.temperature = 20  # in Celsius
        self.humidity = 50  # in percentage
        self.weather_conditions = ["sunny", "rainy", "cloudy", "stormy"]
    
    def update(self):
        # Update weather conditions periodically
        self.current_weather = random.choice(self.weather_conditions)
        self.temperature += random.randint(-5, 5)
        self.humidity += random.randint(-10, 10)

        # Ensure temperature and humidity are within reasonable bounds
        self.temperature = max(min(self.temperature, 40), -10)
        self.humidity = max(min(self.humidity, 100), 0)

    def apply_weather_effects(self, farm):
        # Apply effects of weather on farm
        if self.current_weather == "rainy":
            for crop in farm.crops:
                crop.water()
        elif self.current_weather == "stormy":
            for animal in farm.animals:
                animal.health -= 1  # Storms decrease animal health

    def draw(self, screen):
        font = pygame.font.Font(None, 36)
        weather_text = f"Weather: {self.current_weather}"
        temperature_text = f"Temperature: {self.temperature}°C"
        humidity_text = f"Humidity: {self.humidity}%"

        weather_surface = font.render(weather_text, True, const.BLACK)
        temperature_surface = font.render(temperature_text, True, const.BLACK)
        humidity_surface = font.render(humidity_text, True, const.BLACK)

        screen.blit(weather_surface, (50, 10))
        screen.blit(temperature_surface, (50, 50))
        screen.blit(humidity_surface, (50, 90))
