from Grass import farm_grass
from Bush import farm_bush
from Carrot import farm_carrot 
from Tree import farm_tree      

def map_entity_function():
    return {
            Entities.Grass: farm_grass
            Entities.Bush: farm_bush
            Entities.Carrot: farm_carrot
            Entities.Tree: farm_tree
         }