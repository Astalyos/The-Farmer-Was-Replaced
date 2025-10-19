petals = dict()

def farm(entity):
    groundType = Grounds.Grassland
    if (entity == Entities.Carrot or entity == Entities.Pumpkin or entity == Entities.Sunflower):
        groundType = Grounds.Soil
    
    # Special sunflower behavior
    if(get_entity_type() == Entities.Sunflower):
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
            #if (m in petals):
            #    petals[m].add(get_pos_x(),get_pos_y())
            #else:
            #    petals[m] = {(get_pos_x(),get_pos_y())}
       
    if(isGroundType(groundType)):
        # Special pumpkin behavior
        if(get_entity_type() == Entities.Dead_Pumpkin or get_entity_type() == Entities.Pumpkin):  
            
            
            # if dead pumpkin or nothing, plant
            if(get_entity_type() == Entities.Dead_Pumpkin or get_entity_type() == None):           
                plant(entity)
        
        if(can_harvest() and entity == Entities.Grass):
            harvest()
        else:
            harvest()
            plant(entity)
        return
    else: 
        if(can_harvest()):
            harvest()
        till()
        plant(entity)
    
def isGroundType(type):
    return type == get_ground_type()

#def isWaterEnough():
#    # If waterLevel is higher than 0.75, ground should be watered
#    if(get_water() > 0.75):
#        return True
#    return False

def giveWaterIfNeeded():
    while (get_water() <= 0.75 and num_items(Items.Water)>=1):
        use_item(Items.Water)
        if (get_water() > 0.75):
            return 
        
    if(num_items(Items.Water) <= 10): 
        print("Low water !")
        return

    
      