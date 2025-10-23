from drone import goto_next, goto
from utils import is_ground_type, give_water, have_fertilizer, custom_clear
from Entity_Map import to_ground

entity = Entities.Pumpkin
gt = to_ground(entity)
valid_pumpkin = 0

#method = "optiOneDronew" # fixed and working, need grid setting
method = "classic" # fixed and working, need grid setting
#set_world_size(3)

def farm_pumpkin(method = "optiOneDrone"):
    give_water()
    if (method == "optiOneDrone"):
        plant_healthy_pumpkin(True)
    elif (method == "classic"):
        plant_healthy_pumpkin()
    else :
        plant_pumpkin()

def is_healthy_pumpkin(): 
    if (get_entity_type() == entity):
        return True
    else:
        return False

# PATTERN ONE : We wait until the pumpkin has grown to check if it is healthy or not
def plant_healthy_pumpkin(use_fertilizer = False):
    global valid_pumpkin
    # While there isn't "healthy" pumpkin, run in circle
    while (not is_healthy_pumpkin()):
        # if there is something planted, harvest if harvestable
        if (can_harvest()):
            harvest()
        
        # Ground verification
        if(not is_ground_type(gt)):
            till()

        # Now the cell should be "None", so until we can harvest again, we loop to use fertilizer if there is       
        plant(entity)
        
        # can_harvest() will return false if it is deadpumpkin so we have to make a check for it inside because itr will still loop
        while (not can_harvest()):
            if (get_entity_type() == Entities.Dead_Pumpkin):
                plant(entity)
                
            # If we want to use fertilizer and we have enough of it
            if (use_fertilizer and have_fertilizer()):
                use_item(Items.fertilizer)
            else:
                # We wait until the the pumpkin finish to grow to check if it's a healthy pumpkin
                pass
                
    # If we reach here, it means the we have a Pumpkin because we are out of the while loop
    valid_pumpkin +=1
    if (valid_pumpkin == get_world_size() * get_world_size()):
        harvest()
        valid_pumpkin = 0
    

# PATTERN 2 : We want to plant and do the check on the next time the drone pass on the cell
def plant_pumpkin():
    if (not is_healthy_pumpkin()):
        if (can_harvest() or Entities.Dead_Pumpkin):
            harvest()

        # Ground verification
        if(not is_ground_type(gt)):
            till()

        plant(entity)
    else :
        if (can_harvest()):
            harvest()
        plant(entity)

# todo : create a function that check the whole x or y matching a condition
def check_axis(axis):
    if (not is_healthy_pumpkin()):
        if (can_harvest() or Entities.Dead_Pumpkin):
            harvest()
            
        # Ground verification
        if(not is_ground_type(gt)):
            till()
        plant(entity)

# To optimize for better rendering
# 6x6 chunk, find good algorithm

def main():
    # todo : find WHEN to harvest
    while True:
       farm_pumpkin(method)
       goto_next()
       
if __name__ == "__main__":
    custom_clear()
    set_world_size(6)
    main()