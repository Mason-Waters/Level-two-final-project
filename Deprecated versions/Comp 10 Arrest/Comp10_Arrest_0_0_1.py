"""
    Author: Mason Waters
    Date: 30/10/20
    Desc: This component handles the arrest, ending the gameplay
    Version: 0.0.1
"""

# libraries and imports--------------------------------------------------------

# end libraries and imports----------------------------------------------------

# function definitions---------------------------------------------------------


def arrest(people_list):
    """
    Arrest function
    Parameters:
        people_list: list: contains all of the people
    Returns:
        None: NoneType: Means that the user went to arrest, and then decided
            against it. Continue as if this function was not called
        0: Means that the user guessed wrong. Give score of 0
        1: Means that the user guessed correctly. Give a score above 0
    """
    certainty = input("Are you sure that you are ready to make an arrest? This will end the game.")  # verify (will be call to comp 4 later)
    if certainty in ["n", "no"]:#be sure to change this condition once comp 4 is happen
        return None  # the user decided not to make an arrest just yet
    print("You gather everyone in the yard. There is a heavy police presence" +
          ", in case the culprit tries to escape. The mood is tense. You" +
          " raise your arm, point, and say:\n\"It\'s you! You committed " +
          "the crime!\"")  # worldbuilding and user interaction (ui)
    prompt = "Who were you pointing at?"  # initialisation
    for person in range(len(people_list)):  # this handles people
        prompt += "\n" + str(person) + ": " + people_list[person][0]  # add

    accused = people_list[int(input(prompt))]#this will be a call to comp 4 later also.
    if accused[1]:  # they were the murderer, user was right
        print("A fine days work from the best detective in the world. Anothe" +
              "r criminal behind bars. You have earned your salary.")  # ui
        return 1
    else:  # they arent the murderer, user was wrong
        print("Ooo. That's going to leave a mark when they are found innoc" +
              "ent in court. You might even go to jail yourself for malpract" +
              "ice. People won't trust you as much anymore, as an innocent" +
              " is going on trial due to you.")  # ui
        return 0
# end function definitions-----------------------------------------------------

# testing routine--------------------------------------------------------------
if __name__ == "__main__":  # is this code being called directly?
    arrest([["Jim", True, "angry"], ["Mary", False, "nervous"]])

# end testing routine----------------------------------------------------------
