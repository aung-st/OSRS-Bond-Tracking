from src.get_data import get_data_details,get_data_graph,get_data_five_minute_average

# All API calls are initialised here to avoid excessive calls 
details = get_data_details()
graph = get_data_graph()
five_minute_averages = get_data_five_minute_average()

# API calls should return a dictionary if successful
def test_data_details_is_fetched():
    assert isinstance(details,dict) 

def test_data_graph_is_fetched():
    assert isinstance(graph,dict) 

def test_data_five_minute_average_is_fetched():
    assert isinstance(five_minute_averages,dict)

def test_data_details_is_correct():
    assert len(details) == 1
    assert len(details['item']) == 13

def test_data_graph_is_correct():
    assert len(graph) == 2
    assert len(graph['daily']) == 180
    assert len(graph['average']) == 180

def test_data_five_minute_average_is_correct():
    assert len(five_minute_averages['data']['13190']) == 4
    assert len(five_minute_averages) == 2