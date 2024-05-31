import json

def save_game(player, farm, filepath='savegame.json'):
    data = {
        'player': {
            'position': (player.rect.x, player.rect.y),
            'money': player.money,
            'inventory': player.inventory.get_inventory(),
        },
        'farm': {
            'crops': [
                {
                    'type': crop.crop_type,
                    'position': (crop.rect.x, crop.rect.y),
                    'growth_stage': crop.growth_stage,
                }
                for crop in farm.crops
            ],
            'animals': [
                {
                    'type': animal.animal_type,
                    'position': (animal.rect.x, animal.rect.y),
                }
                for animal in farm.animals
            ],
        },
    }
    with open(filepath, 'w') as file:
        json.dump(data, file)

def load_game(player, farm, filepath='savegame.json'):
    with open(filepath, 'r') as file:
        data = json.load(file)
    
    player.rect.topleft = tuple(data['player']['position'])
    player.money = data['player']['money']
    player.inventory.items = {
        item['name']: Item(item['name'], item['quantity'])
        for item in data['player']['inventory']
    }

    farm.crops = []
    for crop_data in data['farm']['crops']:
        crop = Crop(crop_data['type'], crop_data['position'][0], crop_data['position'][1])
        crop.growth_stage = crop_data['growth_stage']
        farm.crops.append(crop)
    
    farm.animals = []
    for animal_data in data['farm']['animals']:
        animal = Animal(animal_data['type'], animal_data['position'][0], animal_data['position'][1])
        farm.animals.append(animal)
