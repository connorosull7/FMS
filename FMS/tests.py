import unittest
import pygame
from main import main
from player import Player
from farm import Farm
from market import Market
from weather import Weather
from gui import GUI
from pathfinding import Pathfinding
from farm import Animal
from inventory import Inventory, Item

class TestGameComponents(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.player = Player((400, 300), {})
        self.farm = Farm()
        self.market = Market()
        self.weather = Weather()
        self.gui = GUI(self.screen, {})
        self.grid = [
            [0, 0, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0]
        ]
        self.pathfinder = Pathfinding(self.grid)
        self.animal = Animal((0, 0), self.grid)
        self.inventory = Inventory()

    def tearDown(self):
        pygame.quit()

    def test_player_initial_position(self):
        self.assertEqual(self.player.rect.x, 400)
        self.assertEqual(self.player.rect.y, 300)

    def test_player_movement(self):
        initial_x = self.player.rect.x
        self.player.move(dx=5)
        self.assertEqual(self.player.rect.x, initial_x + 5)

    def test_farm_plant_crop(self):
        self.farm.plant_crop(100, 100)
        self.assertEqual(len(self.farm.crops), 1)
        self.assertEqual(self.farm.crops[0].rect.topleft, (100, 100))

    def test_farm_add_animal(self):
        self.farm.add_animal(200, 200)
        self.assertEqual(len(self.farm.animals), 1)
        self.assertEqual(self.farm.animals[0].rect.topleft, (200, 200))

    def test_market_buy_sell(self):
        initial_supply = self.market.supply['crop']
        cost = self.market.buy('crop', 5)
        self.assertEqual(self.market.supply['crop'], initial_supply - 5)
        self.assertEqual(cost, 50)

        earnings = self.market.sell('crop', 5)
        self.assertEqual(self.market.supply['crop'], initial_supply)
        self.assertEqual(earnings, 50)

    def test_weather_update(self):
        initial_weather = self.weather.current_weather
        self.weather.update()
        self.assertNotEqual(self.weather.current_weather, initial_weather)

    def test_gui_update(self):
        self.gui.update(100, 'Spring', 'Sunny')
        money_surface = self.gui.elements['money']['surface']
        self.assertEqual(money_surface.get_text(), 'Money: $100')

    def test_heuristic(self):
        self.assertEqual(self.pathfinder.heuristic((0, 0), (4, 4)), 8)

    def test_get_neighbors(self):
        neighbors = self.pathfinder.get_neighbors((2, 2))
        expected_neighbors = [(3, 2), (2, 3), (1, 2)]
        self.assertEqual(neighbors, expected_neighbors)

    def test_a_star_search(self):
        start = (0, 0)
        goal = (4, 4)
        path = self.pathfinder.a_star_search(start, goal)
        expected_path = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4)]
        self.assertEqual(path, expected_path)

    def test_animal_move_to(self):
        target = (4, 4)
        self.animal.move_to(target)
        self.animal.update()
        self.assertEqual(self.animal.position, (1, 0))  # First step in the path

    def test_inventory_add_item(self):
        item = Item("Apple", 3)
        self.inventory.add_item(item)
        self.assertTrue(self.inventory.has_item("Apple", 3))

    def test_inventory_remove_item(self):
        item = Item("Apple", 3)
        self.inventory.add_item(item)
        self.inventory.remove_item("Apple", 1)
        self.assertTrue(self.inventory.has_item("Apple", 2))

    def test_inventory_has_item(self):
        item = Item("Apple", 3)
        self.inventory.add_item(item)
        self.assertTrue(self.inventory.has_item("Apple", 3))
        self.assertFalse(self.inventory.has_item("Apple", 4))

    def test_player_pick_up_item(self):
        item = Item("Apple", 3)
        self.player.pick_up_item(item)
        self.assertTrue(self.player.inventory.has_item("Apple", 3))

    def test_player_use_item(self):
        item = Item("Apple", 3)
        self.player.pick_up_item(item)
        self.player.use_item("Apple")
        self.assertTrue(self.player.inventory.has_item("Apple", 2))

if __name__ == '__main__':
    unittest.main()
