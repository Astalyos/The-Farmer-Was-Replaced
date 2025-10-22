def map_entity_ground():
    return {
            Entities.Grass: Grounds.Grassland,
            Entities.Bush: Grounds.Grassland,
            Entities.Carrot: Grounds.Soil,
            Entities.Tree: Grounds.Grassland,
         }

def map_entity_item():
    return {
            Entities.Carrot: Items.Carrot,
            Entities.Grass: Items.Hay,
            Entities.Bush: Items.Wood,
            Entities.Tree: Items.Wood,
            Entities.Pumpkin: Items.Pumpkin,
            Entities.Sunflower: Items.Power,
            Entities.Treasure: Items.Gold,
        }

def to_item(entity):
    return map_entity_item()[entity]

def to_ground(entity)
    return map_entity_ground()[entity]