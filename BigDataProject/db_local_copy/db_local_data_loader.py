import json
from os import fspath, getcwd, walk


def load_copy(fname):
    # open output file for reading
    with open(fspath(fname), 'r') as filehandle:
        dataList = json.load(filehandle)

    return dataList
