from datetime import datetime


def fix_updated_field(data):
    """
    Recursively bypasses the dictionary, find all "updated" fields and
    change the value to the current date and time in ISO 8601 format

    :param data: dict or list
    """
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "updated":
                data[key] = datetime.now().isoformat()
            else:
                fix_updated_field(value)
    if isinstance(data, list):
        for value in data:
            fix_updated_field(value)
