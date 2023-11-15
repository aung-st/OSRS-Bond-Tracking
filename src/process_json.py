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
    id+'-'+time_extracted (str): A string concatenation to be used as a primary key in a database
    """
    
    return id+'-'+time_extracted

def create_graph_key(
    id:str,
    timestamp:str,
) -> str:
    """
    Generate an n-character hash key + a timestamp in milliseconds seperated by a '-' character to be used as primary key
    for the graphs table.

    Parameters:
    id (str): Hash id of json file
    timestamp (str): timestamp in milliseconds since January 1st 1970

    Returns:
    id+'-'+ timestamp (str): A string concatenation to be used as a primary key in a database
    """
    
    return id+'-'+timestamp


def extract_row_tuple_details(
    data:dict,
    id:str
) -> tuple:
    """
    Extract all keys from a single dictionary entry and return it as a 17-tuple.

    Parameters:
    data (dict): A raw json file
    id (str): Hash id of raw json file in the first argument

    Returns:
    (
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
        day180_change
    ) (tuple): A 16-tuple to be used in bulk_process_json
    """

    # extract all keys from 1 dictionary entry
    item_id = data['item']['id']
    type = data['item']['type']
    name = data['item']['name']
    description = data['item']['description']
    current_trend = data['item']['current']['trend']
    current_price = data['item']['current']['price']
    today_trend = data['item']['today']['trend']
    today_price = data['item']['today']['price']
    members = data['item']['members']
    day30_trend = data['item']['day30']['trend']
    day30_change = data['item']['day30']['change']
    day90_trend = data['item']['day90']['trend']
    day90_change = data['item']['day90']['change']
    day180_trend = data['item']['day180']['trend']
    day180_change = data['item']['day180']['change']
    primary_key = create_detail_key(id)

    # return extracted keys
    return (
        primary_key,
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
        day180_change 
    )

def log_id(
    id:str,
) -> None:
   
   """
   Log each row insertion into database for debugging purposes.

   Parameters:
   id (str): Hash id of raw json file passed into bulk_process_json
   """
   
   # keep track of hash id in case of debugging needs
   logging.basicConfig(format="%(asctime)s - %(message)s",level=logging.INFO)
   logging.info(f'id: {id} inserted into details table')

def bulk_process_detail_json(
  database:str,
  raw_json:dict,
  id:str
) -> None:
    
    """
    Add a row json entries into a database 

    Parameters:
    database (str): Database name 
    raw_json (dict): Raw json response fetched from API call
    id (str): Hash id of raw json file
    """
  
    data = extract_row_tuple_details(raw_json,id)

    # add all values of a row into the details table
    bulk_add_details(data,database)

    log_id(data[0])
      
