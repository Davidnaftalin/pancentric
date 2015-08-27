def get_weather_data(source_data):
    with open(source_data) as f:
        file_data = f.read().splitlines()
    headers = file_data[0].split()
    rows = [
        [
        value.strip('*') for value in row.split()
        ] for row in file_data[1:] if row
    ]

    data = [dict(zip(headers, row)) for row in rows]
    return data
