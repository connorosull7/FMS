import constants as const

class Market:
    def __init__(self):
        self.supply = {
            'crop': const.INITIAL_CROP_SUPPLY,
            'animal': const.INITIAL_ANIMAL_SUPPLY,
            'produce': const.INITIAL_PRODUCE_SUPPLY,
        }
        self.demand = {
            'crop': const.INITIAL_CROP_DEMAND,
            'animal': const.INITIAL_ANIMAL_DEMAND,
            'produce': const.INITIAL_PRODUCE_DEMAND,
        }
        self.prices = {
            'crop': const.INITIAL_CROP_PRICE,
            'animal': const.INITIAL_ANIMAL_PRICE,
            'produce': const.INITIAL_PRODUCE_PRICE,
        }

    def buy(self, item_type, quantity):
        if self.supply[item_type] >= quantity:
            self.supply[item_type] -= quantity
            return self.prices[item_type] * quantity
        return 0

    def sell(self, item_type, quantity):
        self.supply[item_type] += quantity
        return self.prices[item_type] * quantity

    def update(self):
        # Update market prices based on supply and demand
        for item_type in self.prices.keys():
            self.prices[item_type] = max(1, self.prices[item_type] * (self.demand[item_type] / (self.supply[item_type] + 1)))

        # Adjust demand and supply periodically (example logic)
        for item_type in self.demand.keys():
            self.demand[item_type] = max(1, self.demand[item_type] + (self.supply[item_type] // 10) - 5)

