# This files handle variable that will be use in a lot of file
# Refrain from altering their value from inside the imported file or only for debug

# World Size and Execution Speed
# WS = get_world_size()
WS = 10
ES = 0

# Water Limit
WATER_LIMIT = 0

# Goto method preference - Shortest VS Simple (lessTick)
# GOTO_METHOD = "simple"
GOTO_METHOD = "shortest"

# Enhance goto_next function, if true, will not cross WS border except on last cell 
GOTO_NEXT_OPTI = False

# Axis for drone deplacement pattern, ONLY works when GOTO_NEXT_OPTI is False
AXIS = "row"
#AXIS = "col"