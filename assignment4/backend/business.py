# import json
# def get_data():

#     with open("names.json", "r") as f:
#         names = json.load(f)

#         # names = dict(names)
#         print(names)
#         return names
# def set_data(data:dict):

#     with open("names.json", "w") as f:
#         f.write(str(data))

import json
from typing import Dict, Any

# FILE_PATH = "names.json"

def get_data() -> Any:
    """Read and return JSON data from names.json"""
    try:
        with open("names.json", "r") as f:
            names = json.load(f)
            print(names)
            return names
    except FileNotFoundError:
        print(f"names.json not found, returning empty list")
        return []
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return []

def set_data(data: Dict) -> None:
    """Write dictionary data to names.json as valid JSON"""
    with open("names.json", "w") as f:
        json.dump(data, f, indent=4)
