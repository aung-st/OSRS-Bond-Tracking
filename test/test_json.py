from src.dump_json import dump_json, create_filename, create_id
from src.get_data import get_data_details, get_data_graph
import os 

def test_id_is_created():

    # generate random id
    id = create_id(3)
    assert isinstance(id,str) and len(id) == 40

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