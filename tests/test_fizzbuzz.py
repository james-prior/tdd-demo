import pytest

from fizzbuzz import fizzbuzz

number_to_expected_output = {
    1: 1,
    2: 2,
    3: 'fizz',
    4: 4,
}
@pytest.mark.parametrize('number, expected_output', number_to_expected_output.items())
def test_known_number_returns_expected(number, expected_output):
    assert expected_output == fizzbuzz(number)
