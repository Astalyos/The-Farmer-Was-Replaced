def getCurrentPosition():
    curr_x = get_pos_x()
    curr_y = get_pos_y()
    return [curr_x, curr_y]

def moveNextCell(total_x, total_y):
    global x
    current_x = get_pos_x()
    if (current_x != total_x-1):
        move(East)
    else :
        move(East)    
        move(North)

        