import csv


def read_csv(file_name: str) -> [(float, float)]:
    values = []
    with open(file_name) as file:
        reader = csv.reader(file)
        for line in reader:
            try:
                values.append((float(line[0]), float(line[1])))
            except:
                pass
    return values
