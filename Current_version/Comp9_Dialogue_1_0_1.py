"""
    Author: Mason Waters
    Date: 6/11/20
    Desc: Dialogue component
    Version: 1.0.1
    Improvements:
        Bug-fixes, such as
        len("evidence") -> len(evidence) (stupidest issue ever)
"""

# libraries and imports--------------------------------------------------------
import Comp4_Validation_1_0_0 as four  # validation and safe user input
from random import randint as rand  # rng
# end libraries and imports----------------------------------------------------

# function definitions---------------------------------------------------------


def generate_response(person, evidence, dialogue_type, user="guest"):
    """
    Handles generation of dialogue
    Parameters:
        person: list: contains in the order shown:
            the person's name: str
            the person's murderous quality (are they the murderer?): boolean
            the person's personality: str (angry, neutral, nervous)
        evidence: list: contains every piece of evidence, each a list of form
            name: str: the name of the evidence piece
            owner: str: the name of the person this evidence relates to
            type: str: either physical or conversational, the kind of evidence
        dialogue_type: int or tuple: integers correspond as follows
            0: A farewell
            1: They're being confronted with physical evidence
            2: They're being confronted with conversational evidence
            (3, n): They're being asked a neutral question, where n is the
                    index number of the question in the neutral questions list.
                    Thank the gods for dynamic typing systems, as much as I
                    normally dislike them, they're working great for me here.
        user: str: the user's username: defaults to guest
    Returns:
        a dialogue string
    """
    personality_suffix = {"angry": "!",
                          "neutral": ".",
                          "nervous": "?"}  # suffix
    # boy do I wish this language had switch statements. Python. What the hell?
    if dialogue_type == 0:  # farewell stuff
        personality_farewell = {"angry": "I'm glad to see the back of you",
                                "neutral": "Goodbye",
                                "nervous": "B-bye"}  # farewell type
        return personality_farewell[person[2]] + \
            personality_suffix[person[2]]  # return a coherent farewell
    elif dialogue_type == 1:  # physical evidence confrontation
        if person[0] == evidence[1]:  # theyre linked to this evidence piece
            personality_affirmative_evidence_response = {
                "angry": "Well yes, of course I would. It's very prominent",
                "neutral": "Yes, I do",
                "nervous": "um, yes, um, yeah, actually"}  # responses
            return "  " + personality_affirmative_evidence_response[person[2]]\
                + personality_suffix[person[2]]  # combine them all together
        else:  # theyre not linked to this evidence piece
            personality_negative_evidence_response = {
                "angry": "No. What is this, what do you take me for",
                "neutral": "No",
                "nervous": "No, should I have? What's going on"}  # responses
            return personality_negative_evidence_response[person[2]] + \
                personality_suffix[person[2]]
    elif dialogue_type == 2:  # conversational evidence confrontation
        if person[1]:  # if they're the murderer
            return "Uh, ah, um, you're misremembering." + \
                "I would ah, never say anything like that."
        else:  # they not the murderer
            personality_response = {
                "angry": "What? How dare you imply that I would say such a" +
                         " thing. I made a mistake, that is all.",
                "neutral": "I mispoke. My apologies",
                "nervous": "ah, uh, um, whoops, I messed up my words. My bad."
                }  # every possible response
            return personality_response[person[2]]
    elif isinstance(dialogue_type, tuple):  # question bc is tuple
        if dialogue_type[1] == 0:  # where were you during the murder?
            if person[1]:  # theyre the murderer
                personality_response = {
                    "angry": "Well, uh, I was in the garden! Doing some" +
                             " midnight gardening! Yep!",
                    "neutral": "Um. I was properly in bed. Sleeping.",
                    "nervous": "um, um, uh, ah, um, I was on the loo. I " +
                               "have hemorrhoids?"
                    }  # all the responses that can be made
                evidence.append(["suspicious alibi",
                                 person[0],
                                 "conversational"])  # take note of that
            else:  # theyre not the murderer
                personality_response = {
                    "angry": "I was in bed! As any good person should have" +
                             " been!",
                    "neutral": "In bed.",
                    "nervous": "I was in bed, but I couldn't sleep, because" +
                               " I was having the, uh, the" +
                               " \*cheese dream\* again"
                    }  # all the responses that can be made
            return personality_response[person[2]], evidence
        elif dialogue_type[1] == 1:  # what time did the murder occur?
            if person[1]:  # theyre the murderer
                personality_response = {
                    "angry": "Around 11:20pm, shouldn't you know that?",
                    "neutral": "11:23pm.",
                    "nervous": "um, uh, the moon was high, so, uh, 11:15-ish?"
                    }  # all the responses that can be made
                evidence.append(["suspiciously specific knowledge of time",
                                 person[0],
                                 "conversational"])  # take note of that
            else:  # theyre not the murderer
                personality_response = {
                    "angry": "How the hell should I know!",
                    "neutral": "I'm afraid I have absolutely no idea." +
                               " Nighttime, presumably",
                    "nervous": "Well, uh, I don't actually know. Should I?" +
                               " Have I been left out of the loop?"
                    }  # all the responses that can be made
            return personality_response[person[2]], evidence
        elif dialogue_type[1] == 2:  # what is your favorite colour?
            personality_response = {
                "angry": "What? Red, I guess? What do you care!",
                "neutral": "Blue.",
                "nervous": "Green maybe?"
                }
            return personality_response[person[2]], evidence
        elif dialogue_type[1] == 3:  # how old are you?
            age = len(person[0])*len(user)  # this cant change when asked again
            if age < 18:  # I don't want to have to add a case for youth
                age = 21 + len(person[0]) + len(user)  # 18 would be suspicious
            personality_response = {
                "angry": "How dare you! I'm quite young, thank you very much!",
                "neutral": str(age) + " years old.",
                "nervous": "If I was born in, uh, February - wait, no March" +
                           " then I'm, ah, uh, um, " + str(age) + "?"
                }  # variations of answers
            return personality_response[person[2]], evidence  # select response
        elif dialogue_type[1] == 4:  # how long did you know the victim?
            consistent_random_number = (len(person[0])*len(user))//3  # names
            personality_response = {
                "angry": "I knew them for over " +
                         str(consistent_random_number) +
                         " years! I knew them better and longer than anyone!",
                "neutral": "Around " + str(consistent_random_number) +
                           " years I think. Yes, I was in London then.",
                "nervous": "It, um, well, it couldn't have been less than" +
                           ", uh, " + str(consistent_random_number) + " years?"
                }  # all the responses to the question
            return personality_response[person[2]], evidence  # select response
        elif dialogue_type[1] == 5:  # have you lost anything recently?
            evidence_choice = "None"
            for piece in evidence:  # looking for an item related to person
                if piece[2] == "physical":  # they cant lose a conversation
                    if piece[1] == person[0]:
                        if rand(0, 2):  # can't always be first item in array
                            continue  # ignore following code
                        evidence_choice = piece[0]  # save for later
                        nothing_flag = False
                        break  # we've found our evidence piece, stop the loop
            else:  # they haven't lost anything
                nothing_flag = True
            personality_response = {
                "angry": {True: "What? No, I'm not the sort to lose things.",
                          False: "What, have you been stalking me or" +
                                 " something? How did you know I lost my " +
                                 str(evidence_choice)},
                "neutral": {True: "Not to my knowledge",
                            False: "Yes, actually, I lost my " +
                                   str(evidence_choice)},
                "nervous": {True: "...um ...no? maybe? not that I can" +
                                  " remember",
                            False: "y-yes. Why? What does my " +
                                   str(evidence_choice) + " have to tell you?"}
                }  # all the possible responses to this particular question
            return personality_response[person[2]][nothing_flag], evidence


def display_dialogue(person, evidence, user):
    """
    Display of and interaction with dialogue
    Parameters:
        person: list: contains in the order shown:
            the persons name: str
            the persons murderous quality (are they the murderer?): boolean
            the persons personality: str (angry, neutral, nervous)
        evidence:
            a list containing all the evidence you can confront them with
        user: str: the users username
    Returns:
        None
    """
    dialogue_loop = True  # loop variable
    while dialogue_loop:  # dialogue loop
        print("What would you like to do in the conversation?")  # ui
        print(" [a] Leave")  # ui
        print(" [b] Confront with your evidence")  # ui
        print(" [c] Neutral question")  # ui
        choice = four.validate("", str, max_length=1, min_length=1,
                               string_whitelist=["a", "b", "c"])  # input
        if choice in ["a"]:  # leaving conversation
            print(user, ":", sep="")  # print username
            print("  Goodbye")  # illusion of conversation
            print(person[0], ":    ")  # print person's name
            print("  ", generate_response(person, None, 0))  # response
            dialogue_loop = False  # conversation is over
        elif choice in ["b"]:  # confrontation
            print("Which evidence piece would you like to confront them with?")
            for piece in range(len(evidence)):  # display the options
                print(" [", piece, "] ", evidence[piece][0], sep="")  # display
            evidence_choice = four.validate("", int, convert=True, num_min=0,
                                            num_max=len(evidence)-1)  # input
            evidence_choice = evidence[evidence_choice]  # not index, piece
            print(user, ":", sep="")  # print username
            if evidence_choice[2] == "physical":  # is this physical?
                print("  Do you recognise this ",
                      evidence_choice[0], "?", sep="")  # illusion of convo
                print(person[0], ":", sep="")  # person's name
                print("  ", generate_response(person, evidence_choice, 1))
            else:  # it's conversational in nature, this evidence
                print("  I have it on good authority that as a result of " +
                      "your words, something interesting has come to " +
                      "light regarding ", evidence_choice[0],
                      ". What do you think of this?", sep="")
                print(person[0], ":", sep="")  # person's name
                print("  ", generate_response(person, evidence_choice, 2))
        elif choice in ["c"]:
            print(user, ":", sep="")  # print username
            neutral_questions = ["Where were you during the murder?",
                                 "What time did the murder occur?",
                                 "What is your favorite colour?",
                                 "How old are you?",
                                 "How long did you know the victim?",
                                 "Have you lost anything recently?"]
            question_number = rand(0, len(neutral_questions)-1)  # index select
            print("  ", neutral_questions[question_number])  # illusion of talk
            print(person[0], ":", sep="")  # who's talking? person[0] is!
            response, evidence = generate_response(
                person,
                evidence,
                (3, question_number),
                user)  # get response
            print("  ", response)  # show response to user
        else:
            pass

# end function definitions-----------------------------------------------------

# main routine-----------------------------------------------------------------
if __name__ == "__main__":  # is this code being called directly?
    emotional_states = ["angry", "neutral", "nervous"]
    person = ["Jim", False, emotional_states[rand(0, 2)]]
    evidence = [["vase", "Jim", "physical"],
                ["bloodstain", "Jim", "physical"],
                ["bootprint", "Jim", "physical"],
                ["suspicious alibi", "Jim", "conversational"],
                ["cheese wheel", "Kate", "physical"]]
    user = "Mary"
    display_dialogue(person, evidence, user)

# end main routine-------------------------------------------------------------


