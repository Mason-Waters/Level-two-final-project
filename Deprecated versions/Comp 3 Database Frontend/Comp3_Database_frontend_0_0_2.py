"""
    Author: Mason Waters
    Date: 30/10/20
    Desc: Database frontend, handles display and whatnot
    Version: 0.0.2
    Improvements over previous version:
        The previous version was just too buggy to work with, and had support
        for sql injection. This implementation is better.
        Filter is consolodated into one dictionary, as opposed to three
        Added support for order by
        Progress toward display of data
    Disadvantages
        This works fine! If you have over a gigabyte of ram dedicated and are
        prepared to constantly restart your program. Which I do not, and am not
        It is also quite messy.
"""

# libraries and imports--------------------------------------------------------
import sqlite3  # database management
import Comp2_Database_backend_0_1_1  # this is my utility funcs, only import while testing, as will be imported from higher later
# end libraries and imports----------------------------------------------------

# function definitions---------------------------------------------------------


def display(conn):
    """
    Function for getting data out of the database
    Please note that only data from the scores table is visible to the user,
    data from the users table is not avaliable. As such, the "FROM scores"
    section of the query is hard coded.
    Parameters:
        conn: sqlite3 connection object
    Returns/Yields:
    """
    filter = None  # this would else only be init-ed conditionally
    #Ask the user how they want to sort or filter the data
    user_options = {"sort": {"0": None,
                             "1": "score ASC",
                             "2": "score DESC",
                             "3": "owner ASC",
                             "4": "owner DESC"}[input("How do you want to sort the data?" +
                                  "\n    0: No sorting, just raw data." +
                                  "\n    1: By score, ascending." +
                                  "\n    2: By score, descending." +
                                  "\n    3: By user, alphabetically, ascending." +
                                  "\n    4: By user, alphabetically, descending.")],
                    "duplicate": input("Do you want to allow duplicate data?" +
                                       "\n    0: Yes." +
                                       "\n    1: No."),
                    "filter": input("Is there anything you want to filter by?" +
                                    "\n    0: Yes." +
                                    "\n    1: No.")}  # get user input (will be replaced by call to comp 4 later)
    print("temporary input stuff, will be replaced with a better call to comp 4 later: ", user_options)#temp
    if user_options["filter"] == "0":#remember to make "0" into 0
        print("Filter is 0")#temp
        filter = [{"0": "score = ?",
                  "1": "owner = ?",
                  "2": "owner != ?",
                  "3": "score != ?",
                  "4": "score > ?",
                  "5": "score < ?",
                  "6": "score >= ?",
                  "7": "score <= ?",
                  }[input("Which comparison do you want?" +
                          "\n    0: score =" +
                          "\n    1: owner =" +
                          "\n    2: owner is not =" +
                          "\n    3: score is not =" +
                          "\n    4: score >" +
                          "\n    5: score <" +
                          "\n    6: score >=" +
                          "\n    7: score <=")], input("What do you want to compare to?")]#temp, will be comp 4 later. of which I am glad, because this is a hhhhaaaaaaaack. Oh, and don't forget to make "0" -> 0
        print("filter: ", filter)#temp                                             
    query = "SELECT"
    if user_options["duplicate"] in ["y", "yes"]:#temp, replace the stuff in the [] later
        print("in conditional")#temp
        query += " DISTINCT"  # the distinct clause ensures distinct records
    query += " * FROM scores"
    if filter is not None:  # sometimes we don't need a where clause
        query += " WHERE " + filter[0]  # sometimes we do need a where clause
    if user_options["sort"] is not None:  # sometimes we don't need an order by
        query += " ORDER BY " + user_options["sort"]  # sometimes we do
    print("query: ", query)#temp

    cursor = conn.cursor()  # need cursor object to interact with db
    if filter is None:  # sometimes the execute doesn't need the extra arg
        cursor.execute(query)  # execute the query
    else:  # sometimes the execute needs the extra arg of filter
        cursor.execute(query, (filter[1],))  # execute the query
    results = cursor.fetchall()  # save results
    print("Score       Owner       Evidence")
    for row in results:  # iterate over
        print("helphelphelphelphehhehehehehehhhhhhhhhh...")#temp
        print("row[2]: ", row[2])#temp
        evidence_list = row[2].split("[")#temp
        print("evidence_list pre-split: ", evidence_list)#temp
        for item in range(len(evidence_list)-1):
            print("item: ", evidence_list[item])#temp
            if evidence_list[item] == "":
                del evidence_list[item]
        evidence_list = [attribute.split(",") for attribute in evidence_list]
        print("evidence_list: ", evidence_list)#temp
        output = " " + " "*(3-len(str(row[0]))) + str(row[0]) + "         " + row[1] + "       "
        print("output: ", output)#temp
        
        for piece in range(len(evidence_list)):
            print("unfinished output: \n", output)
            output += evidence_list[piece]
            output += "\n"
            output += " "*(len(" " + " "*(3-len(str(row[0]))) + str(row[0]) + "         " + row[1] + "       ")-len(evidence_list[0]))
            
        print("finished output: \n", output)  # just print it out
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
    """#testdatainputcode
    test_data = [
        [56, 'jim', [["vase", "Jim", "physical"],
                     ["bloodstain", "Bob", "physical"],
                     ["bootprint", "Tim", "physical"],
                     ["suspicious alibi", "Jim", "conversational"],
                     ["cheese wheel", "Mary", "physical"]]],
        [72, 'bob', [["untied shoelace", "Jim", "physical"],
                     ["bloodstain", "Jim", "physical"],
                     ["vase", "Jim", "physical"],
                     ["suspicious alibi", "Jim", "conversational"],
                     ["cheese wheel", "Tim", "physical"]]],
        [804, 'tim', [["magic wand", "Jim", "physical"],
                      ["fence", "Jim", "physical"],
                      ["vase", "Mary", "physical"],
                      ["suspicious alibi", "Jim", "conversational"],
                      ["open fridge", "Tim", "physical"]]],
        [3, 'mary', [["vase", "Mary", "physical"]]]
        ]
    for i in test_data:
        i[2] = str(i[2])
    cursor = conn.cursor()
    cursor.executemany("""
#INSERT INTO scores VALUES (?,?,?)""", test_data)
    #conn.commit()  # saaaaaaaave teeeeeeest daaaaataaaaa
    c = conn.cursor()#temp
    c.execute("SELECT * FROM scores")
    r = c.fetchall()
    print("r: ", r)
    display(conn)

# end main routine-------------------------------------------------------------
