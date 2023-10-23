from src.get_data import get_data_details,get_data_graph

# API calls should return a dictionary if successful

def test_data_details_is_fetched():
    assert isinstance(get_data_details(),dict) 

def test_data_graph_is_fetched():
    assert isinstance(get_data_graph(),dict) 

def test_data_details_is_correct():
    assert len(get_data_details()) == 1

def test_data_graph_is_correct():
    assert len(get_data_graph()) == 2