"""
    Author: Mason Waters
    Date: 10/9/20
    Desc: Database backend
    Version: 0.1 (Trial number one)
    Improvements over previous trials:
        There's code in it now, rather than just line by line decomposition
        with comments
        Now follows python Pep 8 conventions
        Program flow is now subtly better in places where hashing was happening
        too many times, and where the logic wasn't right
    Disadvantages over previous trials:
        Massive performance decreases. (Because there's code in it now, rather
        than just line by line decomposition)

"""

# libraries and imports--------------------------------------------------------
import sqlite3  # database manipulation module
import hashlib  # secure hashing module
from os import listdir
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

    if DB_NAME in listdir():  # db name exist in current directiory? (uses os)
        print("connecting to db (temp)")  # temp testing print
        conn = sqlite3.connect(DB_NAME)  # create database connection object
        return conn  # return database connection object
    elif DB_NAME not in listdir():  # db name not exist in this dir (uses os)
        print("creating db (temp)")  # temp
        conn = sqlite3.connect(DB_NAME)  # create database
        conn.execute("""
CREATE TABLE users(
id DATATYPE INTEGER PRIMARY KEY ASC,
username DATATYPE VARCHAR(20),
password DATATYPE BLOB NOT NULL
)""")  # create users table
        conn.execute("""
CREATE TABLE scores(
score DATATYPE INTEGER,
owner DATATYPE INTEGER,
evidence DATATYPE BLOB
)""")  # create scores table
        return conn  # return database connection object
    else:  # there is neither a database in the current directory, nor not. ?!
        raise Exception("There is neither not a database in the current " +
                        "directory, nor a database in the current " +
                        "directory. Huh? Huh? What? Huh?")  # raise an error.


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
        print("""Would you like to:
                            Login as a [g]uest,
                            [L]ogin to a pre-existing account,
                            Or create a [n]ew account?""")  # User interface
        login_type_choice = input().lower()  # which option does the user want
        if login_type_choice in ["g"]:  # they want to play as guest
            print("Welcome, guest. We hope you enjoy yourself")  # ui
            return 0  # 0 = no account / guest account
        elif login_type_choice in ["l"]:  # pre-existing account
            print("Please enter your username (not case-sensitive)")  # ui
            username = input().lower()  # get username
            print("Please enter your password (case-sensitive)")
            password = bytes(input(), "utf-8")  # get password
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
        elif login_type_choice in ["n"]:  # they're creating a new account
            username = input("Enter your new username (not case sensitive): ")\
                       .lower()
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
            check = input("Please enter the username again, to " +  # stop typo
                          "avoid typos and whatnot").lower()
            if check != username:  # there was a typo somewhere
                print("Oops! Those don't match. Please try again")  # ui
                continue
            password = input("Please enter your desired password:")  # reusing
            check = input("Please reenter your desired password:")  # variables
            if password != check:  # these should match, else they've made typo
                print("Oops! Those do not match. Please try again")  # ui
                continue  # yeaaaaa. this sends them back to the top. bad.
            password = hashlib.sha224(bytes(password, "utf-8")).hexdigest()
            cursor.execute("""INSERT INTO users (username, password) VALUES (?,?)
            """, (username, password))  # put it into the database (new record)
            conn.commit()  # data persistence
            print("Your account has been created")  # ui
            return username  # log them into their new account
        else:  # we don't have a condition here
            print("That's not an option we have. Please try again")  # ui
            continue  # go to the top of the loop (in case program gets bigger)

"""
As it turns out, conn.close() does all the stuff I wanted. No point in having
a method that just wraps the conn.close(). Deprecated.
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
    # cursor.executemany("""
# INSERT INTO users VALUES (?,?,?)""", test_data)
    cursor.execute("SELECT * FROM users")
    print("Database:\n ", cursor.fetchall())
    account = login(conn)
    print(conn)
    print()
    conn.close()  # this replaces close_database
    print("Account: ", account)
    # MAX_CLOSE_DATABASE_ATTEMPTS = 7  # close db is deprecated
    # close_database(conn, MAX_CLOSE_DATABASE_ATTEMPTS)  # close db deprecated
# end testing routine----------------------------------------------------------