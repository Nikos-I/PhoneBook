import json


def imp_json(filename):
    with open(f'{filename}.json', 'r') as f:
        return json.load(f)


def exp_json(data, filename):
    with open(f'{filename}.json', 'w') as f:
        json.dump(data, f)
