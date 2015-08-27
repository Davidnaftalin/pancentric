from weather.weather import get_weather_data


def test_get_weather_data():
    '''
    Parses into list of dicts
    '''
    expected_data = [
        {
        'H1': '1',
        'H2': '2',
        'H3': '3',
        },
        {
        'H1': '4',
        'H2': '5',
        'H3': '6',
        },
    ]
    assert get_weather_data(source_data='tests/test_weather.dat') == expected_data

