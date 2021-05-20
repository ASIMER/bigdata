import json
from os import fspath, getcwd, walk


def load_copy():
    # open output file for reading
    with open(fspath('BigDataProject/db_local_copy/db_local_data.txt'), 'r') as filehandle:
        dataList = json.load(filehandle)

    return dataList
