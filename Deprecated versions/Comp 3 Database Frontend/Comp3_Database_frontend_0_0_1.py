"""
    Author: Mason Waters
    Date: 27/10/20
    Desc: Database frontend, handles display and whatnot
    Version: 0.0.1
    Note: This is more or less an incomplete testing version. Some decisions
        were made in the display function that were questionable, but not game
        breaking, (notably in the filter section, with the use of dictionaries)
        that needed addressing.
"""

# libraries and imports--------------------------------------------------------
import sqlite3  # database management
import Comp2_Database_backend_0_1_1  # this is my utility funcs, only import while testing
# end libraries and imports----------------------------------------------------

# function definitions---------------------------------------------------------


def display(conn):
    """
    Function for getting data out of the database
    Please not that only data from the scores table is visible to the user,
    data from the users table is not avaliable. As such, the "FROM scores"
    section of the query is hard coded.
    Parameters:
        conn: sqlite3 connection object
    Returns/Yields:
    """
    #Ask the user how they want to sort or filter the data
    filter = None  # this would else only be init-ed conditionally
    user_options = {"sort": input("How do you want to sort the data?" +
                                  "\n    0: No sorting, just raw data." +
                                  "\n    1: By score, ascending." +
                                  "\n    2: By score, descending." +
                                  "\n    3: By user, alphabetically, ascending." +
                                  "\n    4: By user, alphabetically, descending."),
                    "duplicate": input("Do you want to allow duplicate data?" +
                                       "\n    0: Yes." +
                                       "\n    1: No."),
                    "filter": input("Is there anything you want to filter by?" +
                                    "\n    0: Yes." +
                                    "\n    1: No.")}  # get user input (will be replaced by call to comp 4 later)
    print("temporary input stuff, will be replaced with a better call to comp 4 later: ", user_options)#temp
    if user_options["filter"] == "0":#remember to make "0" into 0
        print("Filter is 0")#temp
        filter = {"0": "score",
                  "1": "owner",
                  "2": "evidence",
                  "3": input("Please enter your number"),
                  "4": input("Please enter your string")}[input("What is the first thing you want to compare?" +
                                                                "\n    0: score" +
                                                                "\n    1: owner" +
                                                                "\n    2: evidence" +
                                                                "\n    3: a number of your choice" +
                                                                "\n    4: a string of your choice")]#temp, will be comp 4 later. of which I am glad, because this is a hhhhaaaaaaaack. Oh, and don't forget to make "0" -> 0
        print(filter)#temp
        filter += {"0": " = ",
                   "1": " != ",
                   "2": " > ",
                   "3": " < ",
                   "4": " >= ",
                   "5": " <= "}[input("How do you want to compare the thing " +
                                    "you just entered to the thing you're " +
                                    "about to enter?" +
                                    "\n    0: First is = second" +
                                    "\n    1: First is not = second" +
                                    "\n    2: First is > second" +
                                    "\n    3: First is < second" +
                                    "\n    4: First is >= second" +
                                    "\n    5: First is <= second")]
        filter += {"0": "score",
                  "1": "owner",
                  "2": "evidence",
                  "3": input("Please enter your number"),
                  "4": input("Please enter your string")}[input("What is the first thing you want to compare?" +
                                                                "\n    0: score" +
                                                                "\n    1: owner" +
                                                                "\n    2: evidence" +
                                                                "\n    3: a number of your choice" +
                                                                "\n    4: a string of your choice")]#temp, will be comp 4 later. of which I am glad, because this is a hhhhaaaaaaaack. Oh, and don't forget to make "0" -> 0
    query = "SELECT"
    if user_options["duplicate"] in ["y", "yes"]:#temp, replace the stuff in the [] later
        print("in conditional")#temp
        query += " DISTINCT"  # the distinct clause ensures distinct records
    query += " * FROM scores "
    if filter is not False:  # sometimes we don't need a where clause
        query += "WHERE " + filter  # sometimes we do need a where clause
    print("query: ", query)#temp
    #Format a query string (begins with “SELECT”) based on that

    cursor = conn.cursor()  # need cursor object to interact with db
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
    #Query the database on that formatted query string, remembering to filter out any names but the current user’s
    #Display what the database returns based on that

def forgot_password():
    """
    This function handles the "oops, I forgot my password, let me change it"
    that seems so common on the modern web.
    Parameters:
    Returns/Yields:
    """
    #Safely get the user to enter their current username and password (4)
    #Encrypt their password using python’s hashlib library
    #If the password hash matches the password hash stored in the Users table of the database
    #Ask them what they would like to change their password to (4)
    #Encrypt the password via hashlib
    #Set the password field of the Users table at the record associated with the user’s username to the new password hash via the sqlite3 “UPDATE” command
    #Tell the user: “Your password has successfully been changed”


def data_into_database():
    """
    Function for putting data into the database
    Parameters:
    Returns/Yields:
    """
    pass

# end function definitions-----------------------------------------------------

# main routine-----------------------------------------------------------------
if __name__ == "__main__":  # testing routine
    conn = Comp2_Database_backend_0_1_1.connect_to_database()
    display(conn)

# end main routine-------------------------------------------------------------
