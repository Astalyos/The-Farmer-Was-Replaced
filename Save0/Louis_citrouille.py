clear()
set_world_size(16)
ws = get_world_size() +1

def waterIfNeeded():
    while get_water() < 0.75:
          use_item(Items.Water)

def groundTypeSoil():
    if get_ground_type() != Grounds.Soil:
        till()
    
def drone_function():
    def main_1():
        allGood = 0
        for column in range(ws):
             groundTypeSoil()
             waterIfNeeded()
             curr_ent = get_entity_type()
             if curr_ent == Entities.Dead_Pumpkin or curr_ent == None:
                 if can_harvest():
                     harvest()  # Remove Dead One
             if curr_ent == Entities.Pumpkin:
                 allGood += True
             plant(Entities.Pumpkin)
             move(North)
        if (allGood == ws):
            harvest()
            
    while True:
        main_1()


def main():
    for column in range(ws):
        while num_drones() >= max_drones():
            spawn_drone(drone_function())
            move(East)
            
main()