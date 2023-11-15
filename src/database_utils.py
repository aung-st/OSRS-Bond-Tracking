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
    
def create_details_table(database: str) -> None:
    """
    Creates a table to store information from the json details.

    Parameters:
    database (str): Name of database where the table is inserted
    """
    connection = connect(
        host="localhost",
        user="root",
        password=get_password(),
        database=database
        ) 

    connection.cursor().execute(f"""
                                CREATE TABLE IF NOT EXISTS details (
                                uuid varchar(255) PRIMARY KEY,
                                type varchar(255),
                                item_id int,
                                name varchar(255),
                                description varchar(255),
                                members varchar(255),
                                current_trend varchar(255),
                                current_price varchar(255),
                                today_trend varchar(255),
                                today_price varchar(255),
                                day30_trend varchar(255),
                                day30_change varchar(255),
                                day90_trend varchar(255),
                                day90_change varchar(255),
                                day180_trend varchar(255),
                                day180_change varchar(255)
                                );
                                """)
    
def bulk_add_details(
    data:tuple,
    database:str
) -> None:
        """
        Adds entries from a raw json file into the details table of a database specified in the parameters. 

        Parameters:
        data (tuple): json file content collated into a tuple to be inserted into details table
        database (str): Name of database that will be used to insert into the details table
        """
        connection = connect(
        host="localhost",
        user="root",
        password=get_password(),
        database=database
        ) 

        # sqlite query to be inserted into the execution sequence
        connection.cursor().execute(f"""
            INSERT INTO details(
            uuid,
            type,
            item_id,
            name,
            description,
            members,
            current_trend,
            current_price,
            today_trend,
            today_price,
            day30_trend,
            day30_change,
            day90_trend,
            day90_change,
            day180_trend,
            day180_change)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ;""",data)
        
        connection.commit()

def create_graphs_table(database:str) -> None:
    """
    Creates a table to store information from the json graphs.

    Parameters:
    database (str): Name of database where the table is inserted
    """
    connection = connect(
        host="localhost",
        user="root",
        password=get_password(),
        database=database
        ) 

    connection.cursor().execute(f"""
                                CREATE TABLE IF NOT EXISTS details (
                                uuid varchar(255) PRIMARY KEY,
                                timestamp varchar(255),
                                first_sale_price int,
                                30_day_average int
                                );
                                """)

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


