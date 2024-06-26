import json
from typing import Dict

class DataLoader:

    def load_json_file(name: str) -> Dict:
        with open(name, 'r') as file:
            return json.load(file)
        
        
    def load_string_array(file_path: str) -> list:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]