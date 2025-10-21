from drone import *
from utils import is_ground_type, give_water
from const import entity_list

entity_list = entity_list()
selected_entity = [Entities.Bush, Entities.Carrot, Entities.Grass, Entities.Tree]

def main():
    clear()
    while True:
        for entity in selected_entity:
            if (entity in entity_list):
               entity_list[entity]['function']()
               use_item(Items.Fertilizer)
            goto_next()

if __name__ == "__main__":
    main()