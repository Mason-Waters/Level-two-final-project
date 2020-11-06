"""
    Author: Mason Waters
    Date: 23/10/20
    Desc: Validation and safe user input
    Version: 0.0.3
    Improvements over previous trials:
        Well... it works?
    Disadvantages towards previous trials:
        It's all very inefficient and nigh unreadable. I wouldn't be surprised
        if there are a mass of bugs under the surface. There are default values
        that literally never occur, because above them there are higher level
        default values. The code isn't as well commented as I would like.
        The number check doesn't check for length. So on and so forth.
        Honestly, this code is just... bad.
"""

# libraries and imports--------------------------------------------------------
# end libraries and imports----------------------------------------------------

# function definitions---------------------------------------------------------


def type_check(input, desired_type, convert=False):
    """
    Ensures that the input string is of the desired type, or converts to the
    desired type.
    Parameters:
        input: dynamically typed: the stuff to be checked
        desired_type: keyword: the type desired (quick note. I will be assuming
        that desired_type is a safe and valid argument, as it is only used
        internally. This means that you (I) may encounter fatal exceptions when
        misusing desired_type.)
        convert: bool: True = yeah, convert type if possible, False = no, just
            check if the type matches desired_type
            defaults to: False
    Returns/Yields:
        If convert is True:
            input of type desired_type
            or
            False (meaning that input could not be casted)
        If convert is False
            True (the type of input matches desired_type)
            False (the type input does not match desired_type)
    """
    if convert:  # toggle casting stuff
        try:  # catch all the errors
            return desired_type(input)  # naming conventions are awwwesome
        except TypeError:  # should only happen when types dont convert as want
            return False  # we couldn't convert
        except ValueError:  # this one too
            return False  # we couldn't convert
        # could put a blanket except here, but I want to see all other errors
    return isinstance(input, desired_type)  # python handles this natively


def scope_check(input, max_length=99999999, min_length=1, num_min=-99999999,
                num_max=99999999, string_blacklist=[], string_whitelist=[]):
    """
    Manages scope. This is everything from length, to character set (no
    unicode EOF characters, thank you very much), to keyword management.
    Parameters:
        input: dynamically typed: the data to check
        max_length: the maximum length of the input as interpreted by len:
            defaults to: 99999999
        min_length: the minimum length of the input as interpreted by len
            defaults to: 1
        num_min: the minimum value of any number types (float, complex, int)
            defaults to: -99999999
        num_max: the maximum value of any number types (float, complex, int)
            defaults to: 99999999
        string_blacklist: list containing all the characters not allowed in the
            input
            defaults to: empty list
        string_whitelist: list containing all the characters allowed in the
            input
            defaults to: empty list
    Returns/Yields:
        0: Good value, the input passed all the checks
        1: The input was longer than the max length and is not numeric
        2: The input was shorter than the min length and is not numeric
        3: The input was lower than num_min and numeric in type
        4: The input was higher than num_max and numeric in type
        5: The input contained characters not in string_whitelist and was str
        6: The input contained characters in string_whitelist and was str
    """

    if isinstance(input, int) or isinstance(input, float):  # is num?
        if input < num_min:  # check against num_min
            return 3  # lower than num_min
        elif input > num_max:  # check against num_max
            return 4  # higher than num_max
    else:  # is not numeric
        if len(input) > max_length:  # check against max_length
            return 1  # longer than max length
        elif len(input) < min_length:  # check against min_length
            return 2  # shorter than min length
    if isinstance(input, str):  # is string?
        if string_whitelist != []:  # are they using the whitelist feature?
            for character in input:  # iterate through input
                if character not in string_whitelist:  # self-commenting
                    return 5  # failed whitelist check
        elif string_blacklist != []:  # are they using the blacklist feature?
            string_blacklist = string_blacklist + ["", "", "", "", "",
                                                   "", "", "    ", "", "",
                                                   "", "", "", "", "",
                                                   "", "", "", "", "",
                                                   "", "", "", "", "", ""
                                                   ]
            # oh? what's that? unicode control characters are dangerous and
            # shouldn't be used by people who don't understand them very well?
            # I completely agree, that's why my users won't be able to use them
            # What's that? I'm included in the group of people who shouldnt use
            # them? Sorry, what? I'm afraid I cant hear you. Our connection is
            # breaking up, we'll have to finish this another time. Ta-ta.
            for character in input:  # iterate through input
                if character in string_blacklist:  # self-commenting
                    return 6  # failed blacklist check
    return 0  # yay! this is the success exit code, where the input passed!


def validate(prompt, desired_type, **kwargs):
    """
    Main function that ties together all the different aspects of validation
    in a neat little bow. Also contains true, blanket exception catching.
    Parameters:
        prompt: str: the prompt to display when asking for user input
        desired_type: keyword: the desired_type of the input
        **kwargs: accepts:
            convert: bool: True = yeah, convert type if possible, False = no,
                just check if the type matches desired_type
                defaults to: False
            max_length: the maximum length of the input as interpreted by len:
                defaults to: 99999999
            min_length: the minimum length of the input as interpreted by len
                defaults to: 1
            num_min: the minimum value of any number types (float, complex,
                int)
                defaults to: -99999999
            num_max: the maximum value of any number types (float, complex,
                int)
                defaults to: 99999999
            string_blacklist: list containing all the characters not allowed in
                the input
                defaults to: empty list
            string_whitelist: list containing all the characters allowed in the
                input
                defaults to: empty list
    Returns/Yields:
        Valid input of type desired_type
    """

    for argument in kwargs.keys():  # this loop ensures kwargs are acceptable
        if argument not in ["convert",
                            "max_length",
                            "min_length",
                            "num_min",
                            "num_max",
                            "string_blacklist",
                            "string_whitelist"]:  # list of acceptable kwargs
            raise Exception("Function validate() has no place to put keyword" +
                            "argument: " + argument)  # raise keyword exception
    defaults = {"convert": True,
                "max_length": 99999999,
                "min_length": 1,
                "num_min": -99999999,
                "num_max": 99999999,
                "string_blacklist": [],
                "string_whitelist": []}  # these are the default values
    for requirement in ["convert",
                        "max_length",
                        "min_length",
                        "num_min",
                        "num_max",
                        "string_blacklist",
                        "string_whitelist"]:  # yes this is a hack. shush.
        if requirement not in kwargs.keys():  # is the req in provided kwargs?
            kwargs[requirement] = defaults[requirement]  # like append
    input_flag = True  # flag for loop for retry after failed input
    while input_flag:  # try doesn't retry, this loop facilitates retry on fail
        try:  # important errors that shouldn't be caught? what are those?
            user_input = input(prompt)  # just get the input, yet unsafe
            type_check_result = type_check(user_input, desired_type,
                                           convert=kwargs["convert"])  # call
            if type_check_result is False:  # if valid type
                raise TypeError("Ooops! Sorry, " + user_input + " is not a" +
                                " valid input, because it should be of type " +
                                str(desired_type) + ". Please try again.")
            elif kwargs["convert"] is True:  # if it doesn't behave as a test
                user_input = type_check_result  # save it, for scope check
            scope_check_result = scope_check(user_input,
                                             max_length=kwargs["max_length"],
                                             min_length=kwargs["min_length"],
                                             num_min=kwargs["num_min"],
                                             num_max=kwargs["num_max"],
                                             string_blacklist=kwargs[
                                                 "string_blacklist"],
                                             string_whitelist=kwargs[
                                                 "string_whitelist"])  # call

            scope_fail_response = {
                1: "Oops! That input was too long. Shorter than " +
                   str(kwargs["max_length"]) + " characters please.",
                2: "Oops! That input was too short. Longer than " +
                   str(kwargs["min_length"]) + " characters please.",
                3: "Oops! That input was too low. At least " +
                   str(kwargs["num_min"]) + " please",
                4: "Oops! That input was too high. The highest input should" +
                   "be " + str(kwargs["num_max"]) + " please",
                5: "Oops! That input contained characters you aren't allowed" +
                   "to use. Please only use the following characters: ",
                6: "Oops! That input contained characters you aren't allowed" +
                   "to use. Please do not use the following characters: "
                }
            for character in kwargs["string_blacklist"]:  # add blacklist
                scope_fail_response[6] += character  # add to response
            for character in kwargs["string_whitelist"]:  # add whitelist
                scope_fail_response[5] += character  # add to response
            if scope_check_result != 0:  # don't need to respond if success
                print(scope_fail_response[scope_check_result])  # fail response
            else:  # scope_check had success
                return user_input  # so we send out our input!
        except TypeError as error:  # handle TypeErrors
            print("Error:  ", error)  # look, this except is literally just so
            # that the code keeps running, I don't care if the user sees errors
            continue  # does nothing, just a precaution
# end function definitions-----------------------------------------------------

# main routine-----------------------------------------------------------------
if __name__ == "__main__":  # testing routine
    #print(type_check(1, tuple, True))
    #print(scope_check("abstraction", string_blacklist=["q"]))
    print(validate("prompt goes here: ", int, convert=True))

# end main routine-------------------------------------------------------------
