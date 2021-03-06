"""
    Author: Mason Waters
    Date: 3/11/20
    Desc: Database backend
    Version: 1.0.0
    Note: This version is for integration with other components
    Improvements:
        Primary key autoincrement actually works now!
"""

# libraries and imports--------------------------------------------------------
import sqlite3  # database manipulation module
import hashlib  # secure hashing module
import Comp4_Validation_1_0_0 as four  # validation and safe user input
# end libraries and imports----------------------------------------------------

# function definitions---------------------------------------------------------


def connect_to_database():
    """
    Connection function, will create a database of given name if none exists of
    given name
    Parameters:
        None
    Returns/Yields:
        sqlite3 connection object
    """
    DB_NAME = "main_database.db"  # declare database name constant
    conn = sqlite3.connect(DB_NAME)  # create database or connect to it
    conn.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username DATATYPE VARCHAR(20),
password DATATYPE BLOB NOT NULL
)""")  # create users table
    conn.execute("""
CREATE TABLE IF NOT EXISTS scores(
score DATATYPE INTEGER,
owner DATATYPE INTEGER,
evidence DATATYPE BLOB
)""")  # create scores table
    return conn  # return database connection object


def login(conn):
    """
    Logs the user into the database.
    Parameters:
        conn: an sqlite3 connection object
    Returns/Yields:
        username: str: represents a username
    """
    login_flag = True  # login loop
    while login_flag:  # begin login loop (so as we can get failability)
        login_type_choice = four.validate("""Would you like to:
                            Login as a [g]uest,
                            [L]ogin to a pre-existing account,
                            Or create a [n]ew account?""", str,
                                          string_whitelist=["g", "l", "L", "G",
                                                            "n", "N"]
                                          ).lower()  # ui
        if login_type_choice in ["g", "guest"]:  # they want to play as guest
            print("Welcome, guest. We hope you enjoy yourself")  # ui
            return 0  # 0 = no account / guest account
            login_flag = False  # this should never run, but just in case :)
        elif login_type_choice in ["l", "login"]:  # pre-existing account
            username = four.validate(
                            "Please enter your username (not case-sensitive)",
                            str).lower()  # get username
            password = bytes(four.validate("Please enter your password " +
                                           "(case-sensitive)", str), "utf-8")
            password_hash = hashlib.sha224(password).hexdigest()  # hash it
            cursor = conn.cursor()  # for interacting with the database
            cursor.execute("""
            SELECT password
            FROM users
            WHERE username = ?
            """, (username,))  # get password hash at entered username
            correct_hash = cursor.fetchall()  # move results out of cursor
            if correct_hash != []:  # [] is the no results response from cursor
                correct_hash = correct_hash[0][0]  # removing boilerplate
            conn.commit()  # debind cursor results (more secure)
            if password_hash == correct_hash:  # this is the most important
                return username  # account is referred to by username
            elif correct_hash in [[], "", None]:  # many kinds of empty
                print("That user is not in our records, try again")  # ui
                continue  # give the user opportunity to correct typos
            else:
                print("Password does not match username, try again.")  # ui
                continue  # give the user opportunity to correct typos
        elif login_type_choice in ["n", "new"]:  # user creating new account
            username = four.validate("Enter your new username (not case sens" +
                                     "itive): ", str, max_length=12).lower()
            cursor = conn.cursor()  # need this to interact with database
            cursor.execute("""
            SELECT username
            FROM users
            WHERE username = ?
            """, (username,))  # this should be empty, if username isn't in db
            prior_usernames = cursor.fetchall()  # moving results out of cursor
            if prior_usernames != []:  # cursor returns [] if no results
                print("Sorry! That username has been taken")  # ui
                continue  # return to start of loop (give user another chance)
            check = four.validate("Please enter the username again, to avoid" +
                                  " typos and whatnot", str).lower()  # no typo
            if check != username:  # there was a typo somewhere
                print("Oops! Those don't match. Please try again")  # ui
                continue
            password = four.validate("Please enter your desired password:",
                                     str)  # reusing
            check = four.validate("Please reenter your desired password:",
                                  str)  # variables
            if password != check:  # these should match, else they've made typo
                print("Oops! Those do not match. Please try again")  # ui
                continue  # yeaaaaa. this sends them back to the top. bad.
            password = hashlib.sha224(bytes(password, "utf-8")).hexdigest()
            cursor.execute("""INSERT INTO users (username, password)
                              VALUES (?,?)""", (username, password))  # into db
            conn.commit()  # data persistence
            print("Your account has been created")  # ui
            return username  # log them into their new account
        else:  # we don't have a condition here
            print("That's not an option we have. Please try again")  # ui
            continue  # go to the top of the loop (in case program gets bigger)

"""
As it turns out, conn.close() does all the stuff I wanted. No point in having
a method that just wraps the conn.close(). Deprecated. Keeping for reference.
def close_database(conn, cap):
    \"""
    Close the database
    Parameters:
        conn: an sqlite3 connection object
        cap: int: the maximum number of times
    Returns/Yields:
        In case of successful close:
            None: NoneType
        In case of failure to close:
            False: bool
    \"""
    for i in cap:  # try and try and try again!
        if conn.close()
            pass
        # if the database connection is not closed
# close the database connection object with sqlite3's internal .close() method
        # if the database connection is closed
            # return None (so as to end the function)
# when the close loop has terminated naturally
(ie: the database has failed to close)
    # set conn to some arbitrary value so as to overwrite the connection object
    # return False (meaning that the function has failed to close the database)
"""

# end function definitions-----------------------------------------------------

# testing routine--------------------------------------------------------------
if __name__ == "__main__":  # is this code being called from here?
    conn = connect_to_database()
    test_data = [
        [0, 'jim', hashlib.sha224(b"password").hexdigest()],
        [1, 'bob', hashlib.sha224(b"pass").hexdigest()],
        [2, 'tim', hashlib.sha224(b"1234").hexdigest()],
        [3, 'mary', hashlib.sha224(b"donkey").hexdigest()]
        ]

    cursor = conn.cursor()
    #cursor.executemany("""
#INSERT INTO users VALUES (?,?,?)""", test_data)
    #conn.commit()  # saaaaaaaave teeeeeeest daaaaataaaaa
    cursor.execute("SELECT * FROM users")
    print("Database (users):\n ", cursor.fetchall())
    cursor.execute("SELECT * FROM scores")
    print("Database (scores):\n ", cursor.fetchall())
    account = login(conn)
    print(conn)
    conn.close()  # this replaces close_database
    print("Account: ", account)
    # MAX_CLOSE_DATABASE_ATTEMPTS = 7  # close db is deprecated
    # close_database(conn, MAX_CLOSE_DATABASE_ATTEMPTS)  # close db deprecated
# end testing routine----------------------------------------------------------