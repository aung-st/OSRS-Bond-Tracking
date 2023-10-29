from mysql.connector import connect
from os import getenv

def get_password() -> str:
    """
    Gets the environment variable of the root password for mysql.

    Returns: 
    The MySQL root environment variable 
    """
    return getenv("mysql_root")

def create_database(name:str) -> None:
    """
    Creates a database with the name defined by the user.

    Parameters:
    name (str): Name of the database 
    """

    connection = connect(
        host="localhost",
        user="root",
        password=get_password()
    ) 

    connection.cursor().execute(f"CREATE database IF NOT EXISTS {name}")
    print("Execution Successful")
    


def list_databases() -> None:
    """
    list all created MySQL databases and print them.
    """

    connection = connect(
        host="localhost",
        user="root",
        password=get_password()
    ) 
    databases = connection.cursor()
    databases.execute("SHOW DATABASES")

    for database in databases:
        print(database) 

