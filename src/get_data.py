import requests

def get_data_graph() -> dict:
  """
  Get graph of old school bond sales on the Grand Exchange.

  Returns:
  A dictionary that shows the prices each day of a given item for the previous 180 days
  """
  
  url = "http://services.runescape.com/m=itemdb_oldschool/api/graph/13190.json"
  
  # make the API request
  response = requests.get(url)
  data = response.json()

  # return response data
  return data

def get_data_details() -> dict:
  """
  Get data on current price and price trends on old school bond sales on the Grand Exchange.

  Returns:
  A dictionary of current price and price trends information on tradeable items in the Grand Exchange, the category and item image link
  """
  url = "http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item=13190"
  
  # make the API request
  response = requests.get(url)
  data = response.json()

  # return response data
  return data

def get_data_five_minute_average() -> dict:
  """
  Get data on price averages and volume of sales of Grand Exchange items in the past 5 minutes of sales.
  
  Returns:
  A dictionary of 5 minute high and low average prices and volumes for all items on the Grand Exchange.
  """
  url = "https://prices.runescape.wiki/api/v1/osrs/5m"

  # make the API request
  response = requests.get(url)
  data = response.json()

  # return response data
  return data

