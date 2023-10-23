from src.dump_json import dump_json, create_filename 
from src.get_data import get_data_details, get_data_graph
import os 

def test_raw_json_is_dumped():
    json_path = "data/test_json_dump/details"
    raw_json = get_data_details()

    # dump json file
    filename,id = create_filename(json_path)

    dump_json(raw_json,filename)

    filepath = os.listdir(json_path)

    for f in filepath:
        if id in f:
            file = f
            break

    # check that a file exists with the hash id extracted above
    assert id in file