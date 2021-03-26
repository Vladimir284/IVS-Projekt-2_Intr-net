import math_lib
import pytest


@pytest.mark.parametrize("summand1, summand2, result", [
    (10, 10, 20),
    (-10, -10, -20),
    (-10, 10, 0),
    ((1 / 2), (1 / 2), (2 / 2))
])
def test_plus(summand1, summand2, result):
    assert math_lib.plus(summand1, summand2) == result


@pytest.mark.parametrize("root, base, result", [
    (3, 8, 2),
    (2, 1, 1),
])
def test_nth_root(root, base, result):
    assert math_lib.nth_root(root, base) == result
    with pytest.raises(ValueError):
        math_lib.nth_root(2, -10)
        math_lib.nth_root(0, 3)
    assert math_lib.nth_root(100, 1000) >= 1.07
    assert math_lib.nth_root(2, 20) == 2 * (math_lib.nth_root(2, 5))
