from src.get_data import get_data_details,get_data_graph,get_data_five_minute_average

# API calls should return a dictionary if successful

def test_data_details_is_fetched():
    assert isinstance(get_data_details(),dict) 

def test_data_graph_is_fetched():
    assert isinstance(get_data_graph(),dict) 

def test_data_details_is_correct():
    assert len(get_data_details()) == 1
    assert len(get_data_details()['item']) == 13

def test_data_graph_is_correct():
    assert len(get_data_graph()) == 2
    assert len(get_data_graph()['daily']) == 180

def test_data_five_minute_average_is_correct():
    assert len(get_data_five_minute_average()['data']['13190']) == 4
    assert len(get_data_five_minute_average()) == 2