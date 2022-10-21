import json


def imp_json(filename):
    with open(f'./export/{filename}.json', 'r', encoding='utf-8') as f:
        buf_list = json.load(f)
        res_list = []
        for elem in buf_list:
            res_list.append(tuple(elem))
        return res_list


def exp_json(data, filename):
    with open(f'./export/{filename}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)
