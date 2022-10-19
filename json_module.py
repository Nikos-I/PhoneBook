import json


def imp_json(filename):
    with open(f'{filename}.json', 'r') as f:
        buf_list = json.load(f)
        res_list = []
        for elem in buf_list:
            res_list.append(tuple(elem))
        return res_list


def exp_json(data, filename):
    with open(f'{filename}.json', 'w') as f:
        json.dump(data, f)
