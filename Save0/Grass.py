from drone import goto_next
from utils import is_ground_type, give_water

def main():
    clear()
    while True:
       farm_grass()
       goto_next()

def farm_grass():
    give_water()
    if(can_harvest()):
        harvest()
    if(not is_ground_type(Grounds.Grassland)):
        till()
    # no need replant because grass is the default seed for Grounds.Grassland
    
if __name__ == "__main__":
    main()