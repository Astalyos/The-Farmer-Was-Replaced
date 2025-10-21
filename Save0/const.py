from Grass import farm_grass
from Bush import farm_bush
from Carrot import farm_carrot 
from Tree import farm_tree      

def entity_list():
    return {Entities.Grass: {
          'ground': Grounds.Grassland,
          'function': farm_grass
         },
        Entities.Bush: {
            'ground': Grounds.Grassland,
            'function': farm_bush
         },
        Entities.Carrot: {
            'ground': Grounds.Soil,
            'function': farm_carrot
         },
        Entities.Tree: {
            'ground': Grounds.Grassland,
            'function': farm_tree
         },
       }