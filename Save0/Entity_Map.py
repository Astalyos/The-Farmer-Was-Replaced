entity_ground = {
            Entities.Grass: Grounds.Grassland,
            Entities.Bush: Grounds.Grassland,
            Entities.Carrot: Grounds.Soil,
            Entities.Tree: Grounds.Grassland,
            Entities.Pumpkin: Grounds.Soil,
            Entities.Sunflower: Grounds.Soil
         }

entity_item = {
            Entities.Carrot: Items.Carrot,
            Entities.Grass: Items.Hay,
            Entities.Bush: Items.Wood,
            Entities.Tree: Items.Wood,
            Entities.Pumpkin: Items.Pumpkin,
            Entities.Sunflower: Items.Power,
            Entities.Treasure: Items.Gold,
        }

def map_entity_ground():
    return entity_ground
    
def map_entity_item():
    return entity_item
    
def to_item(entity):
    return entity_item[entity]

def to_ground(entity):
    return entity_ground[entity]