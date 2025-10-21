from drone import *
from utils import is_ground_type, give_water

gt = Grounds.Grassland
entity = Entities.Bush

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