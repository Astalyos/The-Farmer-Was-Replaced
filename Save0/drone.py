def getCurrentPosition():
    curr_x = get_pos_x()
    curr_y = get_pos_y()
    return [curr_x, curr_y]

def moveNextCell(total_x):
    global x
    if (get_pos_x() != total_x-1):
        move(East)
    else :
        move(East)    
        move(North)
        
def moveTo(target_x, target_y):
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
        
def resetPosition():
    moveTo(0,0)    

def doFlip(n):
    for i in range(n):
        do_a_flip()

        