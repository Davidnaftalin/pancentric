def get_weather_data(source_data):
    with open(source_data) as f:
        file_data = f.read().splitlines()

    headers = file_data[0].split()
    rows = []
    for line in file_data[1:]:
        if line:
            row = line.split()
            row = [convert_value(value.strip('*')) for value in row]
            rows.append(row)

    data = [dict(zip(headers, row)) for row in rows]
    return data

def _isfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def convert_value(value):
    if value.isalpha():
        return value
    if value.isdigit():
        return int(value)
    if _isfloat(value):
        return float(value)

