import json
import os
from jsonschema import Draft3Validator

json_list = os.listdir('task_folder/event/')

for json_file in json_list:
    json_data = open(f'task_folder/event/{json_file}')
    data = json.load(json_data)
    json_data.close()

    try:
        json_scheme = open(f'task_folder/schema/{data["event"]}.schema')
        schema = json.load(json_scheme)
        v = Draft3Validator(schema)
        for error in sorted(v.iter_errors(data), key=str):
            print(error.message)
        json_scheme.close()
    except KeyError:
        print(f"Add key 'event' to JSON file {json_file}")
    except TypeError:
        print(f'JSON file {json_file} is empty')
    except FileNotFoundError:
        print(f'JSON schema not found {data ["event"]}')
