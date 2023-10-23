import json
import hashlib
import os 
import datetime

def dump_json():
    pass

def create_filename(
    path:str,
    id_length:int 
)-> str:
    """
    Construct a filename in the format YYMMDDHHmm_data_xxx where YY is year, MM is months DD is day, HH is hour, mm is minute and xxx is a 3 character unique hash id.
    In the case of hash id conflicts a new hash will be generated. The filename is then inserted into a specified json_dump directory from the data/ directory.
    It is recommended to keep the same id length for all json dump files.

    Parameters:
    path (str): A json_dump directory path 
    id_length (int): Length of hash id for files

    Returns:
    (filename,hash_id) (tuple): A 2-tuple with the filename and hash_id attached
    """

    # standardise file names 
    name = "data"  

    # time of json dump
    current_datetime = datetime.datetime.now().strftime("%y%m%d%H%M")


    hash_id = create_id(id_length)[:id_length]

    # construct the filename using the standardized format
    filename = f"{path}{current_datetime}_{name}_{hash_id}.json"

    # prevent conflicts in json dumps
    if os.path.exists(filename):
        print("Potential conflict detected")

        # reconstruct the filename with a different set of id_length hash characters
        hash_id = create_id(3)[:3]
        filename = f"{path}{hash_id}_{name}_{current_datetime}.json"

    # return filename to be used in dump json
    # return hash id for use in double check module
    return filename,hash_id

def create_id(length:str) -> str:
    
    """
    Create a hash id by encoding a string of random bytes of size length.

    Parameters:
    length (int): Size of random bytes

    Returns:
    A hash of length 40
    """

    # generate a hash object for a randomly generated string
    hash_object = hashlib.sha1()
    hash_object.update(str(os.urandom(length)).encode())
    hash_id = hash_object.hexdigest()

    return hash_id