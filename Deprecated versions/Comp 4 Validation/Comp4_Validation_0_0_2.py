"""
    Author: Mason Waters
    Date: 23/10/20
    Desc: Validation and safe user input
    Version: 0.0.2
    Improvements over previous trials:
        type_check is now more efficient
        type_check is now more pythonic (with usage of exceptions being
        integral to the python experience, even being raised internally on use
        of a for loop)
        type_check now knows how to catch errors
        null_cancel has been absorbed into scope_check (not that that means a
        whole lot, I haven't written either of them yet)
    Disadvantages towards previous trials:
        None.
        Well, if we're arguing semantics, I suppose that type_check is subtly
        less readable? Much cleaner though...
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
        # could put a blanket except here, but I want to see all other errors
    # if you're here, convert is False
    return isinstance(input, desired_type)  # python handles this natively


def scope_check():
    """
    Manages scope. This is everything from length, to character set (no
    unicode EOF characters, thank you very much), to keyword management.
    Parameters:
    Returns/Yields:
    """
    pass


def validate():
    """
    Main function that ties together all the different aspects of validation
    in a neat little bow. Also contains error catching.
    Parameters:
    Returns/Yields:
    """
    pass

# end function definitions-----------------------------------------------------

# main routine-----------------------------------------------------------------
if __name__ == "__main__":  # testing routine
    print(type_check(1, tuple, True))

# end main routine-------------------------------------------------------------
