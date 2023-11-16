from database_utils import bulk_add_details,bulk_add_graphs,bulk_add_five_minute_averages
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

def create_five_minute_average_key(
    id:str,
    time_extracted:str = datetime.datetime.now().strftime("%y%m%d%H%M")
) -> str:
    """
    Generate an n-character hash key + a timestamp in milliseconds seperated by a '-' character to be used as primary key
    for the five minute averages table.

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

def extract_list_tuple_graphs(
    data:dict,
    id:str
) -> list:
    """
    Extract all keys and values from a graphs json as a list of 4-tuples.

    Parameters:
    data (dict): A raw json file
    id (str): Hash id of raw json file in the first argument

    Returns:
    graph_values (list): a list of 4-tuples containing the first sale price and 30 day average at a given timestamp
    in the order (primary key, timestamp, first sale price, 30 day average) for each tuple
    """

    # split data into daily and average keys to make extracting values easier
    daily = data['daily']
    average = data['average']
    
    # extract all timestamps by getting the keys of either daily or average
    # picking either is okay as the timestamps are in line with eachother
    timestamps = list(daily.keys())
    first_sale_prices = list(daily.values())
    average_30_days = list(average.values())

    graph_values = []

    # place all values into a list of tuples with the addition of a primary key 
    for timestamp in range(180):
        primary_key = create_graph_key(id,timestamps[timestamp])
        graph_values.append((primary_key,timestamps[timestamp],first_sale_prices[timestamp],average_30_days[timestamp]))
    
    # return extracted keys
    return graph_values

def extract_row_tuple_five_minute_average(
    data:dict,
    id:str
) -> tuple:
    """
    Extract all keys from a single dictionary entry and return it as a 5-tuple.

    Parameters:
    data (dict): A raw json file
    id (str): Hash id of raw json file in the first argument

    Returns:
    (
        primary_key,
        average_high_price,
        high_price_volume,
        average_low_price,
        low_price_volume
    ) (tuple): A 5-tuple to be used in bulk_process_json
    """
    
    # extract all values from json keys and generate primary key
    primary_key = create_five_minute_average_key(id)
    average_high_price = data['avgHighPrice']
    high_price_volume = data['highPriceVolume']
    average_low_price = data['avgLowPrice']
    low_price_volume = data['lowPriceVolume']

    # return 5-tuple for later insertion into database table
    return (
        primary_key,
        average_high_price,
        high_price_volume,
        average_low_price,
        low_price_volume
    )

def log_id(
    id:str,
    table:str
) -> None:
   
   """
   Log each row insertion into database for debugging purposes.

   Parameters:
   id (str): Hash id of raw json file passed into bulk_process_json
   table (str): Table name where json entries will be inserted
   """
   
   # keep track of hash id in case of debugging needs
   logging.basicConfig(format="%(asctime)s - %(message)s",level=logging.INFO)
   logging.info(f'id: {id} inserted into {table} table')

def bulk_process_detail_json(
  database:str,
  raw_json:dict,
  id:str
) -> None:
    
    """
    Add a row of json entries into a database 

    Parameters:
    database (str): Database name 
    raw_json (dict): Raw json response fetched from API call
    id (str): Hash id of raw json file
    """
  
    data = extract_row_tuple_details(raw_json,id)

    # add all values of a row into the details table
    bulk_add_details(data,database)

    log_id(data[0],"details")

def bulk_process_graph_json(
        database:str,
        raw_json:dict,
        id:str
) -> None:
    """
    Add 180 rows of json entries into a database 

    Parameters:
    database (str): Database name 
    raw_json (dict): Raw json response fetched from API call
    id (str): Hash id of raw json file
    """
    data = extract_list_tuple_graphs(raw_json,id)

    # add all values of a row into the details table
    
    for row in data:
        bulk_add_graphs(row,database)
        log_id(row,"graphs")

def bulk_process_five_minute_average_json(
        database:str,
        raw_json:dict,
        id:str
) -> None:
    """
    Add a rows of json entries into a database 

    Parameters:
    database (str): Database name 
    raw_json (dict): Raw json response fetched from API call
    id (str): Hash id of raw json file
    """
    data = extract_row_tuple_five_minute_average(raw_json,id)

    # add all values of a row into the details table
    bulk_add_five_minute_averages(data,database)
    log_id(data[0],"five minute averages")

