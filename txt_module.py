def exp_txt(data, filename):
    with open(f'{filename}.txt', 'w', encoding='utf-8') as f:
        f.writelines([f"{line}**" for line in data])


def imp_txt(filename):
    with open(f'{filename}.txt', 'r', encoding='utf-8') as f:
        buf_str = f.read().strip('**')
        buf_list = buf_str.split('**')
        for elem in range(len(buf_list)):
            buf_list[elem] = buf_list[elem].replace(')', '').replace('(', '')

        buf_list2 = []
        for el in range(len(buf_list)):
            buf_list2.append(buf_list[el].replace("'", "").split(', '))

        for i in range(len(buf_list2)):
            for j in range(len(buf_list2[i])):
                if buf_list2[i][j].isdigit():
                    buf_list2[i][j] = int(buf_list2[i][j])

        row_result = []
        for elem in buf_list2:
            row_result.append(tuple(elem))

        return row_result
        # print(row_result)
