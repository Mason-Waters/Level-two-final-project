"""
    Author: Mason Waters
    Date: 22/10/20
    Desc: Validation and safe user input
    Version: 0.0.1
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
        desired_type: keyword: the type desired
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
    print("input:", input,
          "\ndesired_type:", desired_type,
          "\nconvert:", convert)#temp
    if convert:  # toggle casting stuff
        cases = {
            (bool, bool): input,
            (bool, int): int(input),
            (bool, float): False,
            (bool, str): str(input),
            (int, bool): bool(input),  # will always be True
            (int, int): input,
            (int, float): float(input),
            (int, str): str(input),
            (float, bool): bool(input),  # will always be True
            (float, int): int(input),  # this truncates the decimal component
            (float, float): input,
            (float, str): str(input),
            (str, bool): bool(input),  # will always be True
            (str, int): False,  # while there are cases where this is fine,
                                # there are far more where it is not
            (str, float): False,  # see str -> int
            (str, str): input
            }  # this contains every combination of input type and desired type
        return cases[(type(input), desired_type)]  # select the correct one
        #return desired_type(input)  # naming conventions are awwwesome
    return isinstance(input, desired_type)  # python handles this perfectly

def scope_check():
    """
    Manages scope. This is everything from length, to character set (no
    unicode EOF characters, thank you very much), to keyword management.
    Parameters:
    Returns/Yields:
    """
    pass

def null_cancel():
    """
    Neatly handles null values. There are enough ways to write nothing that
    this warrants its own function.
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
    print(type_check("sdf", bool, True))

# end main routine-------------------------------------------------------------
