"""
    Author: Mason Waters
    Date: 13/10/20
    Desc: Generate the map
    Version:
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
    world_size = MAX_ROOM_COUNT*MAX_ROOM_SIZE  # world size
    grid = [[world_size]]*world_size  # empty space as large as need
    print(grid)#temp
    room_count = rand(MIN_ROOM_COUNT, MAX_ROOM_COUNT)  # room num for this map
    room_list = []  # stores a list of the rooms
    for i in range(room_count):  # each iteration of this loop makes a new room
        length = rand(MIN_ROOM_SIZE, MAX_ROOM_SIZE)  # x_size of the new room
        #height = rand(MIN_ROOM_SIZE, MAX_ROOM_SIZE)  # y_size of the new room
        height = length#temptemptemp
        print("room count high loop: ", i)#temp
        if room_list == []:  # is this the first room?
            room_list.append([rand(0, world_size-length),
                             rand(0, world_size-height),
                             length, height])  # store the thing
            print(room_list)#temp
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
                    room_list[0][0]-1,  # space before room
                    True,  # wall
                    length-2,  # space in room
                    True,  # wall
                    world_size-length-room_list[0][0]]  # space after room
            grid[room_list[0][1]+height] = [  # top of the room into grid
                room_list[0][0]-1,  # space before room
                [True] * length,  # waaaaaaalllll
                world_size-length-room_list[0][0]]  # space after room
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
    MIN_ROOM_SIZE = 2
    MAX_ROOM_SIZE = 5
    MIN_ROOM_COUNT = 3
    MAX_ROOM_COUNT = 3
    map_generate(MIN_ROOM_SIZE, MAX_ROOM_SIZE, MIN_ROOM_COUNT, MAX_ROOM_COUNT)

# end main routine-------------------------------------------------------------
