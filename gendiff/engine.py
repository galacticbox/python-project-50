from gendiff.json_dif import jsn_open
from gendiff.yml_dif import yml_open


def transform_val(val):
    bl = {'True': 'true', 'False': 'false'}
    if isinstance(val, bool):
        return bl[str(val)]
    else:
        return val


def format_decoder(filepath):
    if filepath.endswith('yml') or filepath.endswith('yaml'):
        return yml_open(filepath)
    elif filepath.endswith('json'):
        return jsn_open(filepath)
    else:
        raise ValueError("the following format isn't supported")
