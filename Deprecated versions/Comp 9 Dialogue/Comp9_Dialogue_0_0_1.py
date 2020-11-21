"""
    Author: Mason Waters
    Date: 15/10/20
    Desc: Dialogue component
    Version: 0.0.1
"""

# libraries and imports--------------------------------------------------------

# end libraries and imports----------------------------------------------------

# function definitions---------------------------------------------------------


def generate_response(person, dialogue_type):
    """
    Handles generation of dialogue
    Parameters:
        person: list: contains in the order shown:
            the person's name: str
            the person's murderous quality (are they the murderer?): boolean
            the person's personality: str (angry, neutral, nervous)
        dialogue_type: int: integers correspond as follows
            
    Returns:
        a dialogue string
    """

    from random import randint as rand
    if person[1]:  # they are the murderer
        answer_list = ["yes", "yeah", "uh-huh", "that's right"]
        personality_prefix = {"angry":"Shut up, ",
                              "neutral":"Sorry, um, ",
                              "nervous":"Um, ah, "}  # prefix
    else:  # they aren't the murderer
        answer_list = ["no", "nah", "nope", "that's wrong", "I don't recall"]
        personality_prefix = {"angry":"Well, ",
                              "neutral":"Sorry, ",
                              "nervous":"Um, ah, "}  # prefix

    dialogue = answer_list[rand(0, len(answer_list)-1)]

    personality_suffix = {"angry":"!",
                          "neutral":".",
                          "nervous":"?"}  # suffix
    return personality_prefix[person[2]] + dialogue +\
           personality_suffix[person[2]]  # combine into a coherent phrase

def display_dialogue(person, evidence):
    """
    Display of and interaction with dialogue
    Parameters:
        person: list: contains in the order shown:
            the person's name: str
            the person's murderous quality (are they the murderer?): boolean
            the person's personality: str (angry, neutral, nervous)
        evidence:
            a list containing all the evidence you can confront them with
    Returns:
        None
    """
    dialogue_loop = True  # loop variable
    while dialogue_loop:  # dialogue loop
        print("What would you like to do in the conversation?")  # ui
        print("[a] Leave")  # ui
        print("[b] Confront")
        print("[c] Neutral question")
        choice = input()  # input (later will be replaced by call to comp 4)
        if choice == ["a"]:
            print("")
        
        print(person[0], ":\n    ")
        print(generate_response(person))
# end function definitions-----------------------------------------------------

# main routine-----------------------------------------------------------------
if __name__ == "__main__":  # is this code being called directly?
    person = ["Jim", True, "nervous"]
    evidence = [["vase", "Jim"]]
    #print(generate_response(person))
    display_dialogue(person, 0)

# end main routine-------------------------------------------------------------
