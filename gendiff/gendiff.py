import json


def transform_val(val):
    bl = {'True': 'true', 'False': 'false'}
    if isinstance(val, bool):
        return bl[str(val)]
    else:
        return val


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    tmp = '{\n'
    copy1 = sorted(file1.items())
    copy2 = sorted(file2.items())
    for key2, val2 in copy2:
        if key2 not in file1.keys():
            tmp += f'  + {key2}: {transform_val(val2)}\n'

        for key1, val1 in copy1:
            if key2 == key1 and val2 == val1:
                tmp += f'    {key2}: {transform_val(val2)}\n'
            elif key2 == key1 and val2 != val1:
                tmp += f'  - {key1}: {transform_val(val1)}\n'
                tmp += f'  + {key2}: {transform_val(val2)}\n'
            elif key1 not in file2.keys():
                unique_key1 = f'  - {key1}: {transform_val(val1)}\n'
                if unique_key1 not in tmp:
                    tmp += unique_key1
    tmp += '}'
    return tmp
