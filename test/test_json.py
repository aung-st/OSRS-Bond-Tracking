from src.dump_json import dump_json, create_filename, create_id
from src.get_data import get_data_details, get_data_graph
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

def test_detail_json_is_dumped():

    # test file path for json details
    json_path = "data/test_json_dump/details"
    raw_json = get_data_details()

    # create filename and fetch id 
    filename,id = create_filename(json_path)

    # dump json file
    dump_json(raw_json,filename)

    filepath = os.listdir(json_path)

    for f in filepath:
        if id in f:
            file = f
            break

    # check that a file exists with the hash id extracted above
    assert id in file