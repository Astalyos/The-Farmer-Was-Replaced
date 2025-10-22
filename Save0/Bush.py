from drone import goto_next
from utils import is_ground_type, give_water
from Entity_Map import to_ground

entity = Entities.Bush
gt = to_ground[entity]

def main():
    clear()
    while True:
       farm_bush()
       goto_next()

def farm_bush():
    give_water()
    if(can_harvest()):
        harvest()
    if(not is_ground_type(gt)):
        till()
    plant(entity)
    
if __name__ == "__main__":
    main()