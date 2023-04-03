from task4.utils import read_json_file, save_data
from task4.worker import fix_updated_field


def fix_json(json_path: str, new_json_path: str):
    """
    Takes json file, find all "updated" fields and change the value to the current date and time in ISO 8601 format.

    :param json_path: input json file path
    :param new_json_path: path to save the corrected json file
    """
    data = read_json_file(json_path)
    fix_updated_field(data)
    save_data(new_json_path, data)
