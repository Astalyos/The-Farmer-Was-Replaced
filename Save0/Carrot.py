from drone import goto_next
from utils import is_ground_type, give_water, have_fertilizer
from Entity_Map import to_ground

entity = Entities.Carrot
gt = to_ground(entity)

def main():
    clear()
    while True:
       farm_carrot()
       goto_next()

def multi_farm_carrot():
   return false 
       
def quick_farm_carrot():
    clear()
    while True:
        give_water()
        if(can_harvest()):
            harvest()
        if(not is_ground_type(gt)):
            till()
        plant(entity)
        if (have_fertilizer()):
            use_item(Items.fertilizer)
            use_item(Items.Weird_Substance)

def farm_carrot():
    # Todo : Check if there is materials to plant carrot
    give_water()
    if(can_harvest()):
        harvest()
    if(not is_ground_type(gt)):
        till()
    plant(entity)
    
if __name__ == "__main__":
    quick_farm_carrot()
    #main()