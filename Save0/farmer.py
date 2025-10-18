def farm(entity):
    groundType = Grounds.Grassland
    if (entity == Entities.Carrot):
        groundType = Grounds.Soil

    if(isGroundType(groundType)):
        if(can_harvest()):
            harvest()
            plant(entity)
    else: 
        if(can_harvest()):
            harvest()
        till()
        plant(entity)
    
def isGroundType(type):
    return type == get_ground_type()

def isWaterEnough():
    waterLevel = get_water()
    # Si le niveau d'eau est superieur a 0.75, le sol devrait etre arroser
    if(waterLevel > 0.75):
        return True
    return False

def giveWaterIfNeeded():
    if(num_items(Items.Water) <= 10): 
        print("Low water !")
        return

    if (not isWaterEnough() and num_items(Items.Water)>=1):
        use_item(Items.Water)
      