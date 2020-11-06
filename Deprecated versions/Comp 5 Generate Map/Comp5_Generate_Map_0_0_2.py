"""
    Author: Mason Waters
    Date: 13/10/20
    Desc: Generate the map
    Version: 0.0.2
    Improvements over previous trials:
        I just wanted to back up the incomplete code in the last version
    Disadvantages over previous trials:
        I just wanted to back up the incomplete code in the last version
"""

# libraries and imports--------------------------------------------------------

# end libraries and imports----------------------------------------------------

# function definitions---------------------------------------------------------


def map_generate(MIN_ROOM_SIZE, MAX_ROOM_SIZE, MIN_ROOM_COUNT, MAX_ROOM_COUNT):
    """
    This function generates the map
    It should only be run once.
    Parameters:
        MIN_ROOM_SIZE: the minimum size of a room
        MAX_ROOM_SIZE: the maximum size of a room
        MIN_ROOM_COUNT: the minimum number of rooms
        MAX_ROOM_COUNT: the maximum number of rooms
    Returns/Yields:
        grid: A map of the rooms, organised into lines of x. True represents a
              wall, a number represents that number of empty spaces. The grid
              is square.
    """
    from random import randint as rand  # random number generator
    ROOM_COUNT = rand(MIN_ROOM_COUNT, MAX_ROOM_COUNT)  # room num for this map
    world_size = ROOM_COUNT*MAX_ROOM_SIZE  # world size
    grid = [[world_size]]*world_size  # empty space as large as need
    room_list = []  # stores a list of the rooms
    print("ROOM_COUNT: ", ROOM_COUNT, "\nworld_size: ", world_size)
    for i in range(ROOM_COUNT):  # each iteration of this loop makes a new room
        length = rand(MIN_ROOM_SIZE, MAX_ROOM_SIZE)  # x_size of the new room
        height = rand(MIN_ROOM_SIZE, MAX_ROOM_SIZE)  # y_size of the new room
        print("room count high loop: ", i)#temp
        if room_list == []:  # is this the first room?
            room_list.append([rand(0, world_size-length),
                             rand(0, world_size-height),
                             length, height])  # store the thing
            print("room_list: ", room_list)#temp
        else:  # this is not the first room
            # this block finds an open face to place the block onto
            room_list.append([rand(0, world_size-length),#screeeeeeeeeeeeeeeeeeeeeeam
                             rand(0, world_size-height),
                             length, height])  # store the thing
            print("room_list: ", room_list)#temp
        
        #this block puts the room into the grid. the for stuff is just move up
        for x_strip in range(room_list[i][1], room_list[i][1] + height):
            print("x_strip: ", x_strip)#temp
            print("grid[x_strip]: ", grid[x_strip])#temp
            """
            remaining_space = world_size  # this will store space to the right
            for space in grid[x_strip]:  # for "thing" in x_strip
                if type(space) == type([]):  # rooms are stored as list
                    for boolean in space:  # iterate over items in room desc
                        remaining_space -= boolean  # subtract each (True = 1!)
                    continue  # remaining_space -= space will throw an error
                remaining_space -= space  # subtract item from remaining space
                print("Remaining space: ", remaining_space, "\nSpace: ", space)#temp
        
            """
            print("grid[x_strip][-1]: ", grid[x_strip][-1])#temp
            grid[x_strip][-1] -= room_list[i][0]  # create space to the right
            print("grid[x_strip][-1]: ", grid[x_strip][-1])#temp
            grid[x_strip].append([True, length-2, True])  # add the room slice
            #grid[x_strip].append(remaining_space)  # add the remaining space
            #grid[x_strip] = [room_list[i][1], [True, length-2,True], world_size-length-room_list[i][1]]
            
            """
            print([  # bottom of the room into grid
                room_list[0][0]-1,  # space before room
                [True] * length,  # waaaaaaalllll
                world_size-length-room_list[0][0]] )#temp
            grid[room_list[0][1]] = [  # bottom of the room into grid
                room_list[0][0],  # space before room
                [True] * length,  # waaaaaaalllll
                world_size-length-room_list[0][0]]  # space after room
            for l in range(1, height):  # iterate over y-values of interior
                grid[room_list[0][1]+l] = [  # one horizontal crosssection of room
                    room_list[0][0],  # space before room
                    [True],  # wall
                    length-2,  # space in room
                    [True],  # wall
                    world_size-length-room_list[0][0]]  # space after room
            grid[room_list[0][1]+height] = [  # top of the room into grid
                room_list[0][0],  # space before room
                [True] * length,  # waaaaaaalllll
                world_size-length-room_list[0][0]]  # space after room
            """
            
        #this next section tries to find an open face of the building
        #that happens in order of placement, so the first room to be placed gets high priority
        for r in room_list:  # this loop glances at each room to find space
            if grid[r[1]] == True:
                pass
        #after that, we make sure that there's enough space to place the thing
        #and place it in, bindings (room adjacencies) and all
        #then we place items into it
    else:  #heyo, we're done with construction (or something's happened !!! )
        print(world_size, "\n", room_list, "\n", grid)#temp, debug
    for q in range(len(grid)):
        print("Test grid number {0}: ".format(q), grid[q])
            
        

# end function definitions-----------------------------------------------------

# main routine-----------------------------------------------------------------
if __name__ == "__main__":  # is this code being called directly?
    MIN_ROOM_SIZE = 3
    MAX_ROOM_SIZE = 5
    MIN_ROOM_COUNT = 1
    MAX_ROOM_COUNT = 1
    map_generate(MIN_ROOM_SIZE, MAX_ROOM_SIZE, MIN_ROOM_COUNT, MAX_ROOM_COUNT)

# end main routine-------------------------------------------------------------
