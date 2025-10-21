from drone import *

count = 0

def reset_maze():
    clear()
    plant(Entities.Bush)
    goto_next()
    plant(Entities.Bush)
    use_item(Items.Weird_Substance,2)
    
def move_maze_drone():
    goto(0,0)
    while True:
        goto(0,1)
        test()
        goto(0,0)
        test()
        goto(1,0)
        test()
        goto(1,1)
        test()
        goto(1,0)
        test()
        goto(0,0)
        test()
        if (count > 305):
            break

def test():
    global count
    if (can_harvest() and get_entity_type() == Entities.Treasure):
        use_item(Items.Weird_Substance,2)
        count += 1
        quick_print(count)
    if (count > 305):
        if (can_harvest() and get_entity_type() == Entities.Treasure):
            harvest()
        
def main(): 
    clear()
    reset_maze()
    move_maze_drone()

if __name__ == "__main__":
    main()

        
#while True:
    #if(can_harvest()):
    #  harvest()
#    plant(Entities.Bush)
#    use_item(Items.Weird_Substance)
#    use_item(Items.Weird_Substance)