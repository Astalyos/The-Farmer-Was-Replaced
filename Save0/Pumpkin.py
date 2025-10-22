from drone import goto_next
from utils import is_ground_type, give_water
from Entity_Map import to_ground

entity = Entities.Pumpkin
gt = to_ground[entity]

method = "optiOneDrone"
#method = "optiFullDrone"
#method = "classic"

def farm_pumpkin(method = "optiOneDrone"):
    give_water()
    if (method === "optiOneDrone"):
        plant_healthy_pumpkin(True)
    else :
        plant_pumpkin()

def have_fertilizer():
    if (num_items(Items.Fertilizer)>=1):
        return True
    else: 
        # Out of fertilizer
        quick_print("Unsufficient Fertilizer")
        return False

def is_healthy_pumpkin(): 
    if (get_entity_type() == entity):
        return True
    else:
        return False

# PATTERN ONE : We wait until the pumpkin has grown to check if it is healthy or not
def plant_healthy_pumpkin(use_fertilizer = False):
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
        while (not can_harvest):
            # If we want to use fertilizer and we have enough of it
            if (use_fertilizer and have_fertilizer()):
                use_item(Items.fertilizer)
            else:
                # We wait until the the pumpkin finish to grow to check if it's a healthy pumpkin
                pass

    # If we reach here, it means the we have a Pumpkin because we are out of the while loop


# PATTERN 2 : We want to plant and do the check on the next time the drone pass on the cell
def plant_pumpkin():
    if (not is_healthy_pumpkin()):
        if (can_harvest()):
            harvest()

        # Ground verification
        if(not is_ground_type(gt)):
            till()

        plant(Entities.Pumpkin)


# To optimize for better rendering
# 6x6 chunk, find good algorithm

def main():
    # todo : find WHEN to harvest
    clear()
    while True:
       farm_pumpkin(method)
       goto_next()

if __name__ == "__main__":
    main()