from drone import goto_next
from utils import is_ground_type, give_water
from Entity_Map import to_ground

entity = Entities.Sunflower
gt = to_ground(entity)
set_world_size(6)

def main():
    clear()
    while True:
       farm_sunflower()
       goto_next()

def farm_sunflower():
    give_water()
    if(can_harvest()):
        harvest()
    if(not is_ground_type(gt)):
        till()
    plant(entity)
    
if __name__ == "__main__":
    main()