"""
    Author: Mason Waters
    Date: 30/10/20 (Nice date, very satisfying)
    Desc: This component handles navigation
    Version: 0.0.1
    Note: This component seems almost disgustingly simple. This is due to time
        pressure. I ideally would have had this much more complex, and will
        if I have spare time.
"""

# libraries and imports--------------------------------------------------------

# end libraries and imports----------------------------------------------------

# function definitions---------------------------------------------------------


def navigation(map, room):
    """
    Navigation function
    Parameters:
        map: list: a list of rooms each of which has
            str: A name in first position (map[n][0])
            int: A series of connections, the rooms which are connected to it.
                 These are represented by the room's index in the map list
        room: int: The room the player is currently in, represented as the
            index of that room in the larger map list
    Returns:
        room: int: the new room number that the player is in
    """
    option_number = 0  # this is just for numbering - for the options
    print("You are currently in the", map[room][0])  # ui
    print("Where would you like to go?")  # ui
    for adjacent_room in map[room][1]:  # go through the connections in room
        print("  ", option_number, ": ", map[adjacent_room][0], sep="")  # ui
        option_number += 1  # distuinguish numbering for adjacent rooms
    user_choice = int(input())#this will be comp 4 later, right now it's very unsafe so it does very much need to be replaced
    room = map[room][1][user_choice]  # move the user
    print("You are now in the", map[room][0])  # ui
    return room


# end function definitions-----------------------------------------------------

# testing routine--------------------------------------------------------------
if __name__ == "__main__":  # testing routine
    test_map = [
        ["lounge", (1, 2, 4)],
        ["kitchen", (4, 0)],
        ["bedroom", (3, 0, 4)],
        ["cheese room", (2, 4)],
        ["hallway", (0, 1, 2, 3)]
        ]
    navigation(test_map, 1)

# end testing routine----------------------------------------------------------
