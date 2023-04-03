import json


def read_json_file(json_path: str):
    """
    Open json file and return dict

    :param json_path:
    :return: dict from json
    """
    with open(json_path, "r") as json_file:
        data = json.load(json_file)

    return data


def save_data(json_path: str, data: dict):
    """
    Save dict to json file

    :param json_path: path to save the json file
    :param data: dict with saved data
    """
    with open(json_path, "w") as json_file:
        json.dump(data, json_file, indent=4)
