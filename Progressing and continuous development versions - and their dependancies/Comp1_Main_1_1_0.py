"""
    Author: Mason Waters
    Date: 6/11/20
    Desc: This is the main
    Version: 1.1.0
    Improvements:
        Using the observe a room functionality now works.
    Disadvantages:
        Connection close is slightly less guarranteed.
"""

# libraries and imports--------------------------------------------------------
# is there a better way to do this? yes. absolutely. shhhhhhhhhhhhhhhhhhhhhhhhh
import Comp2_Database_backend_1_0_0 as two
import Comp3_Database_frontend_1_0_0 as three
import Comp4_Validation_1_0_0 as four
# import Comp5_Generate_Map_0_0_2 as five
# import Comp6_Options_0_0_0
import Comp7_Navigation_1_0_0 as seven
import Comp8_Evidence_1_0_0 as eight
import Comp9_Dialogue_1_0_1 as nine
import Comp10_Arrest_1_0_0 as ten

from random import randint as rand  # rng
import time  # time
# end libraries and imports----------------------------------------------------

# function definitions---------------------------------------------------------


def main():
    """
    Main function
    Parameters:
        None
    Returns:
        arrest: int:
            0: they were wrong
            1: they correctly identified the murderer
        user: str: the username of the user
        evidence: list: the evidence list that is happening
    """

    try:  # just for the connection close, doesn't catch anything
        connection = two.connect_to_database()  # connect to the database
        user = two.login(connection)  # log the user in
        if user is 0:  # neutrality response is baaaaaad
            user = "Guest"  # make good for ui later
        emotional_states = ["angry", "neutral", "nervous"]  # used for people
        people_list = [
            "",  # nobody, mr ghost
            ["Jim", False, emotional_states[rand(0, 2)]],
            ["Mary", False, emotional_states[rand(0, 2)]],
            ["Michael", False, emotional_states[rand(0, 2)]],
            ["Penny", False, emotional_states[rand(0, 2)]]
            ]  # generate people
        people_list[rand(1, len(people_list)-1)][1] = True  # make a murderer
        # map = five.generate_map()  # generate map.
        map = [
            ["lounge", (1, 2, 4), 1],
            ["kitchen", (4, 0), 0],
            ["bedroom", (3, 0, 4), 0],
            ["cheese room", (2, 4, 5), 2],
            ["hallway", (0, 1, 2, 3), 3],
            ["empty elevator shaft", (3), 4]
            ]  # so it turns out map generation is hard the way I wanted
# to do it? here's a hard-coded map. I'll fix it if I have time.
        room = 1  # which room are they in?
        evidence = [
            ["murder weapon", "???", "physical"]
            ]  # there's no evidence
        print("You are in the", map[room][0])  # ui
        gameplay_flag = True  # hmm. multiple turns. what are those?
        while gameplay_flag:  # without these two lines, no idea!
            """
            options = {0: nine.display_dialogue(),
                       1: seven.navigation(map, 0)}[four.validate("", int)]
            """
            prompt = "What do you want to do?\n 0: Go to another room" + \
                     "\n 1: Observe the room\n 2: Make an arrest"  # for option
            if map[room][2] != 0:  # if there's a person in the room
                prompt += "\n 3: Talk to the person in the room"  # talk?
                decision = four.validate(prompt, int, num_min=0,
                                         num_max=3)  # get what they want to do
            else:  # there's nobody in the room
                decision = four.validate(prompt, int, num_min=0,
                                         num_max=2)  # get what they want to do
            if decision == 3 and map[room] != 0:  # they want to talk
                nine.display_dialogue(people_list[map[room][2]],
                                      evidence, user)  # talk
            elif decision == 0:  # they want to move
                room = seven.navigation(map, room)  # navigate
            elif decision == 1:  # they want to observe the room
                evidence.append(eight.observe(evidence, people_list))  # append
                print(f"You look around the room and find: {evidence[-1][0]}")
            elif decision == 2:
                arrest = ten.arrest(people_list)  # make an arrest
                if arrest is not None:  # they went through with the arrest
                    return arrest, user, evidence  # exit function
            else:  # four.validate() shouldn't allow this to happen
                print("hmm. this shouldn't happen. this shouldn't happen. th-")
    finally:  # close the connection, even if an error occurs
        try:  # if there's an error too quickly, connection might be undefined
            connection.close()  # close the connection
        except:
            print("An error occured.")  # well, it did

# end function definitions-----------------------------------------------------

# main routine-----------------------------------------------------------------
if __name__ == "__main__":  # is this code being called directly?
    start_time = time.time()  # start timer
    success, user, evidence = main()  # just function named main, not __main__
    connection = two.connect_to_database()  # connect to db
    if user != "Guest":  # guests dont get their score in the db
        score = int((999 - (time.time() - start_time)) * success)  # score calc
        evidence = str(evidence)  # to put into db later
        user = connection.cursor().execute("SELECT id FROM users WHERE use" +
                                           "rname = ?", (user,)).fetchone()[0]
# get id of user for foreign key
        three.data_into_database([score, user, evidence], "scores", connection)
    end_view_flag = True  # while True is bad, apparently
    while end_view_flag:  # this handles the score view at the end
        three.display(connection)
        if four.validate("Do you want to view the scores again?", str).lower()\
           in ["n", "no"]:  # stop
            break  # stop
    print("Thanks for playing!")  # ui
    connection.close()  # close the database
    # conn = two.connect_to_database()
    # three.display(conn)

# end main routine-------------------------------------------------------------
