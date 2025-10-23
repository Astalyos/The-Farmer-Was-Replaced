from globals import AXIS, WS, GOTO_METHOD, GOTO_NEXT_OPTI
from utils import is_even

def get_pos():
	return (get_pos_x(), get_pos_y())

def shortest_delta(curr, dest, size=WS):
    # Distance will be destination - current, divided by the given size (e.g. worldsize)
    # If the distance to travel is superior to the half of the axis, it mean we can reach it faster by going backward 
    # (drone loops when reaching the end of the world)
	d = (dest - curr) % size
	if d > size / 2:
		d -= size
	return d

def goto_next(axis=AXIS, opti=GOTO_NEXT_OPTI):
    global WS
    is_ws_even = is_even(WS)
    x = get_pos_x()
    y = get_pos_y()

    def goto_next_opti():
        # if last row and world is even, will return to 0,0 when last cell completed
        if (is_ws_even and y = WS-1 and x == WS-1):
            move(North)
            move(East)
            return

        # if last row and world is NOT even, will return to 0,0 when last cell completed
        if (not is_ws_even and y = WS-1 x == 0):
            move(North)
            return

        # y = 0 | 2 | 4 | 6... 
        if (is_even(y)):
            if (x == WS-1):
                move(North)
            else :
                move(East)
            return
        
        # y = 1 | 3 | 5 | 7...
        else :
            if (x == 0):
                move(North)
                return
            else:
                move(West)
            return
    
    def goto_next_simple()
        if (axis == "row"):
            if (x != WS-1):
                move(East)
            else :
                move(East)    
                move(North)
            return
                
        if (axis == "col"):
            if (y != WS-1):
                move(North)
            else :
                move(North)    
                move(East)
            return
        
    if (opti):
        goto_next_opti()
    else :
        goto_next_simple()

def goto_simple(target_x, target_y):
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

def goto_shortest(target_x, target_y):
    # The drone makes use of wraparound.
	# Args:
	#     target: Tuple of length 2
	# Returns:
	#     bool: Success state
	goto_x(x)
	goto_y(y)
	# return True # Commenting for now, may use it later

def goto_x(tx):
    # If the delta is negative, reverse the direction
	dx = shortest_delta(get_pos_x(), tx)
	if dx > 0:
		for _ in range(dx):
			move(East)
	elif dx < 0:
		for _ in range(-dx):
			move(West)
	# return True # Commenting for now, may use it later

def goto_y(ty):
    # If the delta is negative, reverse the direction
	dy = shortest_delta(get_pos_y(), ty)
	if dy > 0:
		for _ in range(dy):
			move(North)
	elif dy < 0:
		for _ in range(-dy):
			move(South)
	# return True # Commenting for now, may use it later

def goto(x,y, method=GOTO_METHOD):
    # Goto_method is define in globals.py and will be "shortest" or "simple"
    if (method == "shortest"):
        goto_shortest(x,y)
    else :
        goto_simple(x,y)
        
def reset_pos():
    goto(0,0)    

def do_flip(n):
    for i in range(n):
        do_a_flip()

        