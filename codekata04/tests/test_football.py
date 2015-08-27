from football.football import get_football_data, min_for_against_diff


def test_get_football_data():
    """
    Parses into list of dicts
    Parses float, int, str
    Ignores numbering
    Ignores dash
    Ignores invalid line
    """
    expected_data = [
        {
            'Team': 'Arsenal',
            'P': 38,
            'W': 26,
            'L': 9,
            'A': 35,
        },
        {
            'Team': 'Liverpool',
            'P': 38,
            'W': 24,
            'L': 8,
            'A': 38,
        },
    ]
    assert get_football_data(
        source_data='tests/test_football.dat'
    ) == expected_data


def test_for_against_diff():
    test_data = [
        {
            'Team': 'Arsenal',
            'P': 38,
            'W': 26,
            'F': 79,
            'A': 36,
        },
        {
            'Team': 'Liverpool',
            'P': 38,
            'W': 24,
            'F': 67,
            'A': 30,
        },
    ]

    assert min_for_against_diff(test_data) == 'Liverpool'

