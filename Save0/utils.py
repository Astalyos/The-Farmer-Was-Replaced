from globals import WS, WATER_LIMIT

def is_even(n):
    return n % 2 == 0

def is_ground_type(type):
    return type == get_ground_type()

def have_fertilizer():
    if (num_items(Items.Fertilizer)>=1):
        return True
    else: 
        # Out of fertilizer
        quick_print("Unsufficient Fertilizer")
        return False

def give_water(up_to = WATER_LIMIT):
    if (get_water() > up_to):
        return 
        
    while (get_water() <= up_to and num_items(Items.Water)>=1):
        use_item(Items.Water) 

def custom_clear(force_ws = True):
    clear()
    if (force_ws):
        # global WS
        set_world_size(WS)
    
