def curr_pos():
    curr_x = get_pos_x()
    curr_y = get_pos_y()
    return [curr_x, curr_y]

def goto_next():
    ws = get_world_size()
    if (get_pos_x() != ws-1):
        move(East)
    else :
        move(East)    
        move(North)
        
def goto(target_x, target_y):
    # Move along X axis
    while get_pos_x() < target_x:
        move(East)
    while get_pos_x() > target_x:
        move(West)
    
    # Move along Y axis
    while get_pos_y() < target_y:
        move(North)
    while get_pos_y() > target_y:
        move(South)
        
def reset_pos():
    goto(0,0)    

def do_flip(n):
    for i in range(n):
        do_a_flip()

        