class Item:
    def __init__(self, name, quantity=1, item_type='resource'):
        self.name = name
        self.quantity = quantity
        self.item_type = item_type

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item.name in self.items:
            self.items[item.name].quantity += item.quantity
        else:
            self.items[item.name] = item

    def remove_item(self, item_name, quantity):
        if item_name in self.items and self.items[item_name].quantity >= quantity:
            self.items[item_name].quantity -= quantity
            if self.items[item_name].quantity == 0:
                del self.items[item_name]
            return True
        return False

    def has_item(self, item_name, quantity=1):
        return item_name in self.items and self.items[item_name].quantity >= quantity

    def get_inventory(self):
        return {name: item.quantity for name, item in self.items.items()}
