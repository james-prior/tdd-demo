import pytest

from largest_factor import largest_factor

number_to_largest_prime_factor = {
    2: 2,
    3: 3,
    5: 5,
    2**2 * 13: 13,
    2**3 * 3**2: 3,
    5*7*11: 11,
    5*7*11*11: 11,
    2**100: 2,
}
@pytest.mark.parametrize('number, expected_largest_prime_factor', number_to_largest_prime_factor.items())
def test_known_number_returns_expected(number, expected_largest_prime_factor):
    assert expected_largest_prime_factor == largest_factor(number) 

