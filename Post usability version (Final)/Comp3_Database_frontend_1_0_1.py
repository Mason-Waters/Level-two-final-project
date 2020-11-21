"""
    Author: Mason Waters
    Date: 21/11/20
    Desc: Database frontend, handles display and whatnot
    Version: 1.0.1
    Improvements:
        All numeric selections raised one :(
        Fixed the score indent as well
"""

# libraries and imports--------------------------------------------------------
import sqlite3  # database management
import Comp4_Validation_1_0_0 as four  # validation and safe user input
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
        None
    """
    filter = None  # this would else only be init-ed conditionally
    user_options = {"sort": {1: None,
                             2: "score ASC",
                             3: "score DESC",
                             4: "owner ASC",
                             5: "owner DESC"}[four.validate("How do you want to"
                                                            + " sort the sco" +
                                                      "res?\n    1: No sorti" +
                                                      "ng, just raw data.\n " +
                                                      "   2: By score, ascen" +
                                                      "ding.\n    3: By scor" +
                                                      "e, descending.\n    4" +
                                                      ": By user, alphabetic" +
                                                      "ally, ascending.\n   " +
                                                      " 5: By user, alphabet" +
                                                      "ically, descending.",
                                                      int, convert=True,
                                                      num_min=1, num_max=5)],
                    "duplicate": four.validate("Do you want to allow duplica" +
                                       "te data?\n    1: Yes." +
                                       "\n    2: No.", int, convert=True,
                                               num_min=1, num_max=2)-1,
                    "filter": four.validate("Is there anything you want to " +
                                    "filter?\n    1: Yes." +
                                    "\n    2: No.", int, convert=True,
                                    num_min=1, num_max=2)-1}  # get user input
    if user_options["filter"] == 0:#remember to make "0" into 0
        filter = [{1: "score = ?",
                   2: "owner = ?",
                   3: "owner != ?",
                   4: "score != ?",
                   5: "score > ?",
                   6: "score < ?",
                   7: "score >= ?",
                   8: "score <= ?",
                   }[four.validate("Which comparison do you want?" +
                           "\n    1: score =" +
                           "\n    2: owner =" +
                           "\n    3: owner is not =" +
                           "\n    4: score is not =" +
                           "\n    5: score >" +
                           "\n    6: score <" +
                           "\n    7: score >=" +
                           "\n    8: score <="
                           , int, convert=True, num_min=1, num_max=8)
                     ], four.validate("What do you want to compare to?", str,
                                      string_blacklist=["~"])]#temp, will be comp 4 later. of which I am glad, because this is a hhhhaaaaaaaack. Oh, and don't forget to make "0" -> 0                                           
    query = "SELECT"
    if user_options["duplicate"] in [0]:  # they don't want duplicates
        query += " DISTINCT"  # the distinct clause ensures distinct records
    query += (" scores.score, users.username, scores.evidence " +
              "FROM scores INNER JOIN users ON users.id = scores.owner")
    if filter is not None:  # sometimes we don't need a where clause
        query += " WHERE " + filter[0]  # sometimes we do need a where clause
    if user_options["sort"] is not None:  # sometimes we don't need an order by
        query += " ORDER BY " + str(user_options["sort"])  # sometimes we do
    cursor = conn.cursor()  # need cursor object to interact with db
    if filter is None:  # sometimes the execute doesn't need the extra arg
        cursor.execute(query)  # execute the query
    else:  # sometimes the execute needs the extra arg of filter
        cursor.execute(query, (filter[1],))  # execute the query
    results = cursor.fetchall()  # save results
    print("Score       Owner        Evidence Name                          Evidence Owner       " +
          "                    Evidence Type")  # headings
    for row in results:  # iterate over results to extract one record at once
        output = "  "  # indentation
        output += str(row[0])  # score
        output += " "*(12-len(str(row[0])))  # column difference
        output += row[1][0].upper()+row[1][1:]  # name of user who owns score
        output += " "*(13-len(str(row[1])))  # column difference
        evidence_list = row[2].split("'")  # split the string
        for piece in range(1, len(evidence_list)-1):  # iterate over
            if evidence_list[piece] == ", ":  # builtin seperator! we can input
                output += " "*(40-len(evidence_list[piece-1]))  # whitespace!
            elif evidence_list[piece] == "], [":  # new evidence piece
                output += "\n"  # new line via newline
                output += " "*27  # move to correct column (and indent)
            else:  # we don't want our semantics
                output += evidence_list[piece]  # add it to output
        print(output)  # just print it out


"""
Due to time constraints, func: forgot_password will not be a part of the final
product. This decision has been made after considerable thought, and is the
only way to get a final product out. I apologise for the issue.
"""


def data_into_database(data, table, conn):
    """
    Function for putting data into the database
    More or less a wrapper for an insert expression
    Parameters:
        data: list: the data to put in. CSV for column differentiation please
        table: str: the table the data is going into
        conn: sqlite3 connection object: sqlite3 connection object
    Returns/Yields:
        None
    """
    query = f"INSERT INTO {table} VALUES (?,?,?);"  # basic query template
    cursor = conn.cursor()  # need this to interact with the database
    cursor.execute(query, (data[0], data[1], data[2]))  # put it in
    conn.commit()  # lock it in
    # ------------what follows is for testing and should be commented out later
    # cursor.execute(f"SELECT * FROM {table}")
    # results = cursor.fetchall()
    # for i in results:
        # print(i)
    return conn

# end function definitions-----------------------------------------------------

# main routine-----------------------------------------------------------------
if __name__ == "__main__":  # testing routine
    conn = Comp2_Database_backend_0_1_1.connect_to_database()
    """#testdatainputcode
    test_data = [
        [56, 0, [["vase", "Jim", "physical"],
                     ["bloodstain", "Bob", "physical"],
                     ["bootprint", "Tim", "physical"],
                     ["suspicious alibi", "Jim", "conversational"],
                     ["cheese wheel", "Mary", "physical"]]],
        [72, 1, [["untied shoelace", "Jim", "physical"],
                     ["bloodstain", "Jim", "physical"],
                     ["vase", "Jim", "physical"],
                     ["suspicious alibi", "Jim", "conversational"],
                     ["cheese wheel", "Tim", "physical"]]],
        [804, 2, [["magic wand", "Jim", "physical"],
                      ["fence", "Jim", "physical"],
                      ["vase", "Mary", "physical"],
                      ["suspicious alibi", "Jim", "conversational"],
                      ["open fridge", "Tim", "physical"]]],
        [3, 3, [["vase", "Mary", "physical"]]]
        ]
    for i in test_data:
        i[2] = str(i[2])
    cursor = conn.cursor()
    cursor.executemany("""
#INSERT INTO scores VALUES (?,?,?)""", test_data)
    #conn.commit()  # saaaaaaaave teeeeeeest daaaaataaaaa
    #display(conn)
    conn = data_into_database([57.5, 2,
                               "[['orange', 'Kathelin', 'physical'], " +
                               "['pear', 'Kathelin', 'physical']]"], "scores",
                              conn)
    display(conn)

# end main routine-------------------------------------------------------------


