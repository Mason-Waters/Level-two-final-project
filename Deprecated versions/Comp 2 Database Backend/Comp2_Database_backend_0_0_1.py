"""
    Author: Mason Waters
    Date: 10/9/20
    Desc: Database backend
    Version: 0.0 (Trial number one)
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
    Must be iterated over to get failability (wrong password, try again)
    Parameters:
        conn: an sqlite3 connection object
    Returns/Yields:
        username: str: represents a username
        or
        error_code: int: represents an issue raised inside the function
    """
    pass
    #tell the user what they can do (you can login as a guest, or create an account, or login like a normal person)
    #use a temporarary input statement to get what the user wants to do (in final version this will be a call to component 4, which handles this kind of thing)
    #if the user entered a value that means they want to play as guest
        #return a code representing the guest account
    #if the user entered a value that means they want to login to a pre-existing account
        #use a temporarary input statement to get what the user wants their username to be (in final version this will be a call to component 4, which handles this kind of thing)
        #use a temporarary input statement to get what the user wants their password to be (in final version this will be a call to component 4, which handles this kind of thing)
        #use a secure hashing algorithm to turn the password into a secure hash, store in [entered_hash]
        #get the password hash stored at the username given by the user, store in [correct_hash]
        #if the hash entered just now ([entered_hash]) equals the hash stored in the database ([correct_hash])
            #return the username the user entered
        #in the hash entered just now ([entered_hash]) does not equal the hash stored in the database ([correct_hash])
            #return an error code meaning the password hash was wrong
    #if the user wants to create an account
        #use a temporarary input statement to get what the user wants their username to be (in final version this will be a call to component 4, which handles this kind of thing)
        #if the entered username is already in the database
            #give the user feedback, that that username is already in the database
            #return an error code meaning that the username already exists
        #if the entered username is not in the database
            #use a temporarary input statement to get what the user wants their password to be (in final version this will be a call to component 4, which handles this kind of thing)
            #use a secure hashing algorithm to turn the password into a secure hash, store in [entered_hash]
            #use an sql "UPDATE" expression to add both the entered username and password to the database
            #give the user feedback saying that their account has been created
            #return the user's new username, effectively logging them into their new account

def close_database(conn):
    """
    Close the database
    Parameters:
        conn: an sqlite3 connection object
    Returns/Yields:
        None
    """
    pass

    #close the database connection object with sqlite3's internal .close() method


        
#end function definitions----------------------------------------------------------------

#testing routine----------------------------------------------------------------------------
if __name__ == "__main__": #is this code being called from somewhere else? if no, run it.
    connect_to_database() #this is just a function named main, for my main code, nothing to do with __main__
    login()
#end testing routine------------------------------------------------------------------------