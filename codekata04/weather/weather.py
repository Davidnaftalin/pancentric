def get_weather_data(source_data):
    with open(source_data) as f:
        file_data = f.read().splitlines()

    headers, header_index = get_header_index(file_data[0])
    rows = []
    for line in file_data[1:]:
        if line:
            row = []
            for start, finish in header_index:
                value = convert_value(line[start:finish].strip('*').strip())
                row.append(value)
            rows.append(row)

    data = [dict(zip(headers, row)) for row in rows]
    return data

def get_header_index(header_string):
    """
    Returns list of headers, list of tuples mapping last
    postion of each header to last position of next header

    get_header_index('  H1   H2   H3')
    >> (['H1', 'H2', 'H3'], [(0, 4), (4, 9), (9, 14)])
    """
    headers = header_string.split()
    hindex = [header_string.find(header) for header in headers]
    header_indexes = []
    for idx, header in enumerate(headers):
        end = hindex[idx] + len(header)

        # Make sure start is 0
        if idx == 0:
            start = 0
            header_index = (start, end)
        else:
            # start is last position of previous header in string
            start = header_indexes[-1][1]
            header_index = (start, end)
        header_indexes.append(header_index)
    return headers, header_indexes


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

