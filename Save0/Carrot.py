from drone import *
from utils import is_ground_type, give_water

gt = Grounds.Soil
entity = Entities.Carrot

def main():
    clear()
    while True:
       farm_carrot()
       goto_next()

def farm_carrot():
    # Todo : Check if there is materials to plant carrot
    give_water()
    if(can_harvest()):
        harvest()
    if(not is_ground_type(gt)):
        till()
    plant(entity)
    
if __name__ == "__main__":
    main()