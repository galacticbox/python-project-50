import json


def jsn_open(file_path):
    file = json.load(open(file_path))
    return file
