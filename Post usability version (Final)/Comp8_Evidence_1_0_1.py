"""
    Author: Mason Waters
    Date: 21/11/20
    Desc: This provides evidence
    Version: 1.0.1 (Post usability)
    Improvements:
        Removed a couple of items which were too long
"""

# libraries and imports--------------------------------------------------------
from random import randint as rand  # rng
# end libraries and imports----------------------------------------------------

# function definitions---------------------------------------------------------


def observe(evidence, people_list):
    """
    This generates evidence
    Parameters:
        evidence: list: the evidence gathered up to this point
        people_list: list: the people
    Returns:
        evidence: list: the new evidence
    """
    item_kinds = [
        "vase",
        "goose",
        "gaggle of geese",
        "recording of goose noises",
        "honk honk buzzer",
        "bloodstain",
        "finely polished carving knife",
        "fingerprint",
        "half-eaten sandwich",
        "very sharp pencil",
        "weak magnet",
        "dog fur",
        "empty 1860s bullet casing",
        "hunting rifle",
        "half empty bottle of bleach",
        "martial arts uniform",
        "pointlessly long spoon",
        "very sharp fork",
        "steak with a bite mark",
        "rat poison",
        "sulfuric gases",
        "100% ethanol",
        "absurdly well trained alligator",
        "staple gun",
        "antique garrotte wire",
        "dynamite",
        "poisonous cactus",
        "absurd cheese",
        "fireworks",
        "broken carbon monoxide detector",
        "traditional guillotine"
        ]  # list of item names, inconsequential
    return [item_kinds[rand(0, len(item_kinds)-1)],
            people_list[rand(1, len(people_list)-1)][0], "physical"]  # return
    
    
    

# end function definitions-----------------------------------------------------

# testing routine--------------------------------------------------------------
if __name__ == "__main__":  # is this a real run? or is it just a test?
    emotional_states = ["angry", "neutral", "nervous"]
    people_list = [
    "",  # nobody, mr ghost
    ["Jim", False, emotional_states[rand(0, 2)]],
    ["Mary", False, emotional_states[rand(0, 2)]],
    ["Michael", False, emotional_states[rand(0, 2)]],
    ["Penny", False, emotional_states[rand(0, 2)]]
    ]
    evidence = [
        ["murder weapon", "???", "physical"]
    ]
    print(observe(evidence, people_list))  
# end testing routine----------------------------------------------------------
