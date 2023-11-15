from database_utils import bulk_add_details
import datetime
import logging

def create_detail_key(
    id:str,
    time_extracted:str = datetime.datetime.now().strftime("%y%m%d%H%M")
) -> str:
    """
    Generate an n-character hash key + a timestamp in milliseconds seperated by a '-' character to be used as primary key
    for the details table.

    Parameters:
    id (str): Hash id of json file
    timestamp (str): datetime extraction of json contents in YYMMDDHHmm form

    Returns:
    id+'-'+country (str): A string concatenation to be used as a primary key in a database
    """
    
    return id+'-'+time_extracted

