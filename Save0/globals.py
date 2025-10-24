# This files handle variable that will be use in a lot of file
# Refrain from altering their value from inside the imported file or only for debug

# World Size and Execution Speed
# WS = get_world_size()
WS = 6
ES = 0

# Water Limit
WATER_LIMIT = 0.3

# Goto method preference - Shortest VS Simple (lessTick)
# GOTO_METHOD = "simple"
GOTO_METHOD = "shortest"

# Enhance goto_next function, if true, will not cross WS border except on last cell 
GOTO_NEXT_OPTI = False

# ONLY works when GOTO_NEXT_OPTI is False, Axis for drone deplacement pattern, 
AXIS = "row"
#AXIS = "col"