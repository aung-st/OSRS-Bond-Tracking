from src.dump_json import dump_json, create_filename, create_id
from src.get_data import get_data_details, get_data_graph, get_data_five_minute_average
import os 

def test_id_is_created():

    # generate random id
    id = create_id(4)
    assert isinstance(id,str) and len(id) == 40

def test_details_filename_is_created():

    json_path = "data/test_json_dump/details"
    id_length = 4

    filename,id = create_filename(json_path,id_length)
    
    assert isinstance(create_filename(json_path,id_length),tuple) and isinstance(filename,str) and isinstance(id,str) 

def test_graphs_filename_is_created():

    json_path = "data/test_json_dump/graphs"
    id_length = 4

    filename,id = create_filename(json_path,id_length)
    
    assert isinstance(create_filename(json_path,id_length),tuple) and isinstance(filename,str) and isinstance(id,str)

def test_five_minute_average_filename_is_created():

    json_path = "data/test_json_dump/five_minute_averages"
    id_length = 4

    filename,id = create_filename(json_path,id_length)
    
    assert isinstance(create_filename(json_path,id_length),tuple) and isinstance(filename,str) and isinstance(id,str)

def test_detail_json_is_dumped():

    # test file path for json details
    json_path = "data/test_json_dump/details/"
    raw_json = get_data_details()

    id_length = 4

    # create filename and fetch id 
    filename,id = create_filename(json_path,id_length)

    # dump json file
    dump_json(raw_json,filename)

    filepath = os.listdir(json_path)

    for f in filepath:
        if id in f:
            file = f
            break

    # check that a file exists with the hash id extracted above
    assert id in file

def test_graph_json_is_dumped():

    # test file path for json graph
    json_path = "data/test_json_dump/graphs/"
    raw_json = get_data_graph()

    id_length = 4

    # create filename and fetch id 
    filename,id = create_filename(json_path,id_length)

    # dump json file
    dump_json(raw_json,filename)

    filepath = os.listdir(json_path)

    for f in filepath:
        if id in f:
            file = f
            break

    # check that a file exists with the hash id extracted above
    assert id in file

def test_five_minute_average_json_is_dumped():

    # test file path for json five minute average
    json_path = "data/test_json_dump/five_minute_averages/"
    raw_json = get_data_five_minute_average()

    id_length = 4

    # create filename and fetch id 
    filename,id = create_filename(json_path,id_length)

    # dump json file
    dump_json(raw_json,filename)

    filepath = os.listdir(json_path)

    for f in filepath:
        if id in f:
            file = f
            break

    # check that a file exists with the hash id extracted above
    assert id in file