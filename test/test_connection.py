from mysql.connector import connect
from src.database_utils import create_database
from os import getenv

# Ensure that database connections can be established 
def test_sample_db_connection_works():

    create_database("test_osrs_db")

    connection = connect(
        host='localhost',
        database='test_osrs_db',
        user="root",
        password=getenv("mysql_root")
        )
    
    assert connection.is_connected()

def test_main_db_connection_works():

    create_database("osrs_db")

    connection = connect(
        host='localhost',
        database='test_osrs_db',
        user="root",
        password=getenv("mysql_root")
        )
    
    assert connection.is_connected()
            
            

    