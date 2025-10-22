from drone import goto_next
from utils import is_ground_type, give_water, is_even
from Entity_Map import map_entity_ground

entity = Entities.Tree
grounds = map_entity_ground()
gt = grounds(entity)

def main(entity_second = None, optimized = True):
    clear()
    while True:
       farm_tree(entity_second, optimized)
       goto_next()

def farm_tree(entity_second = None, optimized = True):
    give_water()
    if(can_harvest()):
        harvest()
    if(not is_ground_type(gt)):
        till()
    if (optimized):
        if (is_even(get_pos_y() + get_pos_x())):
            plant(entity)
        elif (entity_second != None and entity_second != entity) : 
            if (entity_second in grounds):
                if (get_ground_type() != grounds[entity_second]):
                    till()
            plant(entity_second)
    else:
        plant(entity)
    
if __name__ == "__main__":
    main(Entities.Carrot)