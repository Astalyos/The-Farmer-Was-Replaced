# This files handle variable that will be use in a lot of file
# Refrain from altering their value from inside the imported file or only for debug

# World Size
# WS = get_world_size()
WS = 4 

# Water Limit
WATER_LIMIT = 0.76

# Axis for drone deplacement pattern
AXIS = "row"
# AXIS = "col"

# Goto method preference - Shortest VS Simple (lessTick)
# GOTO_MEHTOD = "simple"
GOTO_METHOD = "shortest"

# Enhance goto_next function, if true, will not cross WS border except on last cell 
GOTO_NEXT_OPTI = True