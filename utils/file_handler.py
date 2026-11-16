from pathlib import Path
import json

def load_file(file_path):
    if not file_path.exists():
        return []
    with open(file_path, "r") as file:
        data = file.read()
        if not data:
            return []
        return json.loads(data)
    
def save_file(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)