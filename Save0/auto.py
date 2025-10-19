from farmer import *
from drone import *
from utils import *

total_x = get_world_size()
total_y = get_world_size()

def autoFarm(entity = None, entity_second = None):
    if (entity == None):
        entity = Entities.Grass
    elif (entity == Entities.Tree or entity_second == Entities.Tree):
        if (entity_second == None):
            entity_second = Entities.Grass
    while True: 
        giveWaterIfNeeded()
        #special behavior sunflower
        if(get_pos_x() == 0 or get_pos_x() == 1):
            farm(Entities.Sunflower)
            moveNextCell(total_x)
        else:
            
            
            if (entity_second):
                if ((is_even(get_pos_y()) and is_even(get_pos_x())) or (not is_even(get_pos_y()) and not is_even(get_pos_x()))):
                    farm(entity)
                else : 
                    farm(entity_second)
            else: 
              farm(entity)
            moveNextCell(total_x)

def autoFarmGrass():
    while True: 
        giveWaterIfNeeded()
        farm(Entities.Grass)
        moveNextCell(total_x)
        
def autoFarmCarrot():
    while True: 
        giveWaterIfNeeded()
        farm(Entities.Carrot)
        moveNextCell(total_x, total_y)
        
def autoFarmWTree(entity = None):
    if (entity == None):
        entity = Entities.Grass
    while True:
        giveWaterIfNeeded()
        if ((is_even(get_pos_y()) and is_even(get_pos_x())) or (not is_even(get_pos_y()) and not is_even(get_pos_x()))):
            farm(Entities.Tree)
        else : 
            farm(entity)
        moveNextCell(total_x, total_y)

#def autoFarmPumpkin():
    
                
