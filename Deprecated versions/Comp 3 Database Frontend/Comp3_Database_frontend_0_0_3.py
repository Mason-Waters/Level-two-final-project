"""
    Author: Mason Waters
    Date: 30/10/20
    Desc: Database frontend, handles display and whatnot
    Version: 0.0.3
    Improvements over previous version:
        It works! It's nicely formated and everything! My god it works!
        Memory usage is 1/36 what it was before
        The code is far more readable
        It even gives purpose to the boilerplate!
    Disadvantages:
        None! It's faster AND more memory efficient!
    Note: I'm using stylistic commenting pep issues as reminders for myself
        in a couple of places here. Ie: var foo := "string"#reminder goes here and over the line
        It isn't just that I've missed them, they're delibrate

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
    user_options = {"sort": {"0": None,
                             "1": "score ASC",
                             "2": "score DESC",
                             "3": "owner ASC",
                             "4": "owner DESC"}[input("How do you want to" +
                                                      "sort the data?" +
                                                      "\n    0: No sorting," +
                                                      "just raw data.\n    1" +
                                                      ": By score, ascending" +
                                                      ".\n    2: By score," +
                                                      " descending.\n    3: " +
                                                      "By user, alphabetical" +
                                                      "ly, ascending.\n    4" +
                                                      ": By user, alphabetic" +
                                                      "ally, descending.")],
                    "duplicate": input("Do you want to allow duplicate data?" +
                                       "\n    0: Yes." +
                                       "\n    1: No."),
                    "filter": input("Is there anything you want to filter?" +
                                    "\n    0: Yes." +
                                    "\n    1: No.")}  # get user input (will be replaced by call to comp 4 later)
    if user_options["filter"] == "0":#remember to make "0" into 0
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
                           "\n    7: score <="
                           )
                     ], input("What do you want to compare to?")]#temp, will be comp 4 later. of which I am glad, because this is a hhhhaaaaaaaack. Oh, and don't forget to make "0" -> 0                                           
    query = "SELECT"
    if user_options["duplicate"] in ["0"]:  # they don't want duplicates
        query += " DISTINCT"  # the distinct clause ensures distinct records
    query += " * FROM scores"
    if filter is not None:  # sometimes we don't need a where clause
        query += " WHERE " + filter[0]  # sometimes we do need a where clause
    if user_options["sort"] is not None:  # sometimes we don't need an order by
        query += " ORDER BY " + user_options["sort"]  # sometimes we do

    cursor = conn.cursor()  # need cursor object to interact with db
    if filter is None:  # sometimes the execute doesn't need the extra arg
        cursor.execute(query)  # execute the query
    else:  # sometimes the execute needs the extra arg of filter
        cursor.execute(query, (filter[1],))  # execute the query
    results = cursor.fetchall()  # save results
    print("Score       Owner       Evidence Name       Evidence Owner       " +
          "Evidence Type")  # headings
    for row in results:  # iterate over results to extract one record at once
        output = "  "  # indentation
        output += str(row[0])  # score
        output += " "*(12-len(str(row[0])))  # column difference
        output += row[1][0].upper()+row[1][1:]  # name of user who owns score
        output += " "*(12-len(str(row[1])))  # column difference
        evidence_list = row[2].split("'")  # split the string
        for piece in range(1, len(evidence_list)-1):  # iterate over
            if evidence_list[piece] == ", ":  # builtin seperator! we can input
                output += " "*(20-len(evidence_list[piece-1]))  # whitespace!
            elif evidence_list[piece] == "], [":  # new evidence piece
                output += "\n"  # new line via newline
                output += " "*26  # move to correct column (and indent)
            else:  # we don't want our semantics
                output += evidence_list[piece]  # add it to output
        print(output)  # just print it out


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
    display(conn)

# end main routine-------------------------------------------------------------

