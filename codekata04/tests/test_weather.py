from weather.weather import get_weather_data, smallest_tempreture_spread


def test_get_weather_data():
    """
    Parses into list of dicts
    Ignores '*'
    Parses float, int, str
    Parses None values
    """
    expected_data = [
        {
            'H1': 1,
            'H2': 2,
            'H3': None,
            'H4': 1.0,
            'H5': 'RF',
        },
        {
            'H1': 4,
            'H2': 5,
            'H3': 6,
            'H4': 12.0,
            'H5': 'F'
        },
    ]
    assert get_weather_data(
        source_data='tests/test_weather.dat'
    ) == expected_data


def test_smallest_tempreture_spread():
    test_data = [
        {
            'Dy': 1,
            'MxT': 10,
            'MnT': 5,
        },
        {
            'Dy': 2,
            'MxT': 20,
            'MnT': 5,
        }
    ]

    expected_data = 1

    assert smallest_tempreture_spread(test_data) == expected_data
