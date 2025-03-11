import json
import requests


def load_json_file(file_path, encoding='utf-8'):
    """
    Loads JSON data from a specified file and returns it as a Python object.
    """
    with open(file_path, 'r', encoding=encoding) as f:
        return json.load(f)


def save_json_file(data, file_path, encoding='utf-8', indent=4):
    """
    Saves a Python object as a JSON file.
    The data is usually a dict or list
    """
    with open(file_path, 'w', encoding=encoding) as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)


def validate_json(json_data):
    try:
        json.loads(json_data)
        return True
    except json.JSONDecodeError:
        return False


def load_url(url, params={}):
    """
    get json from url
    params is a dict.
    """
    try:
        response = requests.get(url, params)
        response.encoding = 'utf-8'
        return response.json()
    except Exception as e:
        return {'error': str(e)}
