"""
    Author: Mason Waters
    Date: 10/9/20
    Desc: Database backend
    Version: 0.0 (Trial number three)
    Improvements over previous trials:
        Close method is MUCH safer.
    Disadvantages over previous trials:
        Close method must be checked for failure (False)

"""

#libraries and imports-------------------------------------------------------------------
#database manipulation module
#file path manipulation module
#secure hashing module
#end libraries and imports---------------------------------------------------------------

#function definitions--------------------------------------------------------------------
def connect_to_database():
    """
    Connection function, will create a database of given name if none exists of given name
    Parameters:
        None
    Returns/Yields:
        sqlite3 connection object
    """
    pass
    #declare database name constant

    #if database name constant exists in the current directiory (use os module)
        #create database connection object
        #return database connection object
    #else if database name constant does not exist in the current directory (use os module)
        #create database as according to the specifications in the creation document
        #create database connection object
        #return database connection object
    #else
        #raise an error, this should never happen

def login(conn):
    """
    Logs the user into the database.
    Parameters:
        conn: an sqlite3 connection object
    Returns/Yields:
        username: str: represents a username
    """
    pass
    #begin login loop (so as we can get failability)
        #tell the user what they can do (you can login as a guest, or create an account, or login like a normal person)
        #use a temporarary input statement to get what the user wants to do (in final version this will be a call to component 4, which handles this kind of thing)
    #if the user entered a value that means they want to play as guest
        #return a code representing the guest account
    #if the user entered a value that means they want to login to a pre-existing account
        #use a temporarary input statement to get what the user wants their username to be (in final version this will be a call to component 4, which handles this kind of thing)
        #use a temporarary input statement to get what the user wants their password to be (in final version this will be a call to component 4, which handles this kind of thing)
        #use a secure hashing algorithm (hashlib) to turn the password into a secure hash, store in [entered_hash]
        #get the password hash stored at the username given by the user, store in [correct_hash]
        #if [correct_hash] is not in the database
            #give the user feedback meaning "that username isn't in our records, please try again"
            #jump back up to the top of the loop with a jump statement (continue)
        #if the hash entered just now ([entered_hash]) equals the hash stored in the database ([correct_hash])
            #return the username the user entered
        #in the hash entered just now ([entered_hash]) does not equal the hash stored in the database ([correct_hash])
            #give the user feedback meaning "that password is wrong, please try again"
            #jump back up to the top of the loop with a jump statement (continue)
    #if the user wants to create an account
        #use a temporarary input statement to get what the user wants their username to be (in final version this will be a call to component 4, which handles this kind of thing)
        #if the entered username is already in the database
            #give the user feedback, that that username is already in the database
            #use a jump statement (continue) to restart the loop
        #if the entered username is not in the database
            #use a temporarary input statement to get what the user wants their username to be again (in final version this will be a call to component 4, which handles this kind of thing)
            #if the second username entry does not enter the first username
                #give the user feedback meaning that their usernames did not match
                #use a jump statement (continue) to restart the loop
            #use a temporarary input statement to get what the user wants their password to be (in final version this will be a call to component 4, which handles this kind of thing)
            #use a temporarary input statement to get what the user wants their password to be again (in final version this will be a call to component 4, which handles this kind of thing)            #use a secure hashing algorithm to turn the password into a secure hash, store in [entered_hash]
            #if the second password entry and the first password entry do not match
                #restart the loop with a jump statement
            #use a secure hashing algorithm (hashlib) to turn the password into a secure hash, store in [entered_hash]
            #use an sql "UPDATE" expression to add both the entered username and password to the database
            #give the user feedback saying that their account has been created
            #return the user's new username, effectively logging them into their new account
    #if the user entered something that isn't one of our options
        #give the user feedback telling them that they scewed up, try again
        #put a continue here in case we want to add more cases later. actually semantically useless right now, but it allows for program growth

def close_database(conn, cap):
    """
    Close the database
    Parameters:
        conn: an sqlite3 connection object
        cap: int: the maximum number of times
    Returns/Yields:
        In case of successful close:
            None: NoneType
        In case of failure to close:
            False: bool
    """
    pass
    #begin close loop (iterate over the code in the loop until it's been run [cap] times)
        #if the database connection is not closed
            #close the database connection object with sqlite3's internal .close() method
        #if the database connection is closed
            #return None (so as to end the function)
    #when the close loop has terminated naturally (ie: the database has failed to close)
        #set conn to some arbitrary value so as to overwrite the connection object
        #return False (meaning that the function has failed to close the database)

        
#end function definitions----------------------------------------------------------------

#testing routine----------------------------------------------------------------------------
if __name__ == "__main__": #is this code being called from somewhere else? if no, run it.
    connect_to_database() 
    login()
    close_database()
#end testing routine------------------------------------------------------------------------