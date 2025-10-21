def is_even(n):
    return n % 2 == 0

def is_ground_type(type):
    return type == get_ground_type()

def give_water(up_to = 0.75):
    if (get_water() > up_to):
        return 
        
    while (get_water() <= up_to and num_items(Items.Water)>=1):
        use_item(Items.Water) 

map_entity_item = {
    Entities.Carrot: Items.Carrot,
    Entities.Grass: Items.Hay,
    Entities.Bush: Items.Wood,
    Entities.Tree: Items.Wood,
    Entities.Pumpkin: Items.Pumpkin,
    Entities.Sunflower: Items.Power,
    Entities.Treasure: Items.Gold,
}

def to_item(entity):
    return map_entity_item[entity]
    
# def to_entity(Items: item):
    # return to_entity[entity]