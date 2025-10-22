from drone import goto_next
from utils import is_ground_type, give_water
from Function_Map import map_entity_function

entity_function = map_entity_function()
selected_entity = [Entities.Bush, Entities.Carrot, Entities.Grass, Entities.Tree]

def main():
    clear()
    while True:
        for entity in selected_entity:
            if (entity in entity_function):
               entity_function[entity]()
               use_item(Items.Fertilizer)
            goto_next()

if __name__ == "__main__":
    main()