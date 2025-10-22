from drone import *
from utils import is_ground_type, give_water
from Entity_Map import to_ground

entity = Entities.Pumpkin
gt = to_ground[entity]

def main():
    goto(0,0)
    while True:
       farm_pumpkin()
       goto_next()

def farm_pumpkin():
    give_water()
    if(can_harvest()):
        harvest()
    if(not is_ground_type(gt)):
        till()
    plant(entity)
    
if __name__ == "__main__":
    main()

# To optimize for better rendering
# 6x6 chunk, find good algorithm