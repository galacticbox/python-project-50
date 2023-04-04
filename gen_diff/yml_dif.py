import yaml


def yml_open(file_path):
    file = yaml.safe_load(open(file_path))
    return file
