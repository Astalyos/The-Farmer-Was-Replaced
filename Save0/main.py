# from farmer import *
from drone import *
from auto import *

# autoFarm(Entities.Sunflower)

groundType = Grounds.Soil
entity = Entities.Sunflower

while True:

    giveWaterIfNeeded()
    #special behavior sunflower
    if(get_pos_x() == 0 or get_pos_x() == 1):
        # Special sunflower behavior
        if(isGroundType(groundType)):    
            #m = measure()
            #if (m in petals and max(petals) == m):
            #   petals[m].add(get_pos_x(),get_pos_y())
                    
            harvest()
            plant(entity)
            m = measure()
            if (m in petals):
               petals[m].add((get_pos_x(),get_pos_y()))
            else:
               petals[m] = {(get_pos_x(),get_pos_y())}
           
        else: 
            if(can_harvest()):
                harvest()
            till()
            plant(entity)
            m = measure()
            if (m in petals):
                petals[m].add((get_pos_x(),get_pos_y()))
            else:
                petals[m] = {(get_pos_x(),get_pos_y())}
        quick_print(petals)
    moveNextCell(total_x)


#harvest()
#till()
#plant(Entities.Sunflower)
#test = measure()
#print (test)


# autoFarm(Entities.Sunflower)
# autoFarm(Entities.Tree, Entities.Bush)
#autoFarm(Entities.Tree, Entities.Grass)


# while True:
    # giveWaterIfNeeded()
    # farmBush()
    # farmCarrot()
    # farmHay()    
    # moveNextCell(total_x)

# while True:
#   for i in range (get_world_size()): # Pour chaque ligne 
#     for j in range(get_world_size()): # Pour chaque colonne
#       if (can_harvest()):
#         harvest()
#         plant(Entities.Grass)
#         move(North)
#     move(East)



