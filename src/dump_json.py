import json
import hashlib
import os 

def dump_json():
    pass

def create_filename() -> str:
    pass

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