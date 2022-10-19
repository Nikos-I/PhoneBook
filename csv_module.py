import csv


def exp_csv(data, filename):
    with open(f'{filename}.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def imp_csv(filename):
    with open(f'{filename}.csv', newline='') as f:
        reader = csv.reader(f)
        rows = []
        rows_result = []
        for row in reader:
            rows.append(row)

        for i in range(len(rows)):
            for j in range(len(rows[i])):
                if rows[i][j].isdigit():
                    rows[i][j] = int(rows[i][j])
        for elem in rows:
            rows_result.append(tuple(elem))
    return rows_result
