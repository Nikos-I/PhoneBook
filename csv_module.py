import csv


def exp_csv(data, filename):
    with open(f'{filename}.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def imp_csv(filename):
    with open(f'{filename}.csv', newline='') as f:
        reader = csv.reader(f)
        rows = []
        for row in reader:
            rows.append(row)

    return rows
