def get_football_data(source_data):
    with open(source_data) as f:
        file_data = f.read().splitlines()
    headers = file_data[0].split()
    start_pos = file_data[0].find(headers[0])

    rows = []
    for line in file_data[1:]:
        row = [convert_value(value) for value in line[start_pos:].split()]
        rows.append(row)

    data = [dict(zip(headers, row)) for row in rows]
    return data

def convert_value(value):
    if value.isalpha():
        return value
    if value.isdigit():
        return int(value)
    if _isfloat(value):
        return float(value)
