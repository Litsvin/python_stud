import json


class Reader:
    @staticmethod
    def read_json(path_to_file):
        with open(path_to_file, 'r') as f:
            return json.load(f)


