import math_lib
import pytest


@pytest.mark.parametrize("summand1, summand2, result", [
    (10, 10, 20),
    (-10, -10, -20),
    (-10, 10, 0),
    ((1 / 2), (1 / 2), (2 / 2))
])
def test_summary(summand1, summand2, result):
    assert math_lib.summary(summand1, summand2) == result


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


@pytest.mark.parametrize("x , y , result", [
    (10, 2, 5),
    (15, -5, -3),
    (-15, 3, -5),
    (-15, 7, -2.142857142857143),
    (0, 5, 0),
])
def test_divide(x, y, result):
    with pytest.raises(Exception):
        assert math_lib.division(1, 0)
        assert math_lib.division(-50, 0)
    assert math_lib.division(x, y) == result


@pytest.mark.parametrize("x , result", [
    (5, 5),
    (-4, 4),
    (0, 0),
    (-123645789, 123645789),
    (-1.2548, 1.2548)
])
def test_absolute_value(x, result):
    assert math_lib.absolute_value(x) == result


@pytest.mark.parametrize("x, result", [
    (5, 120),
    (0, 1),
    (1, 1),
    (12, 479001600),
    (2, 2),
    (3, 6)
])
def test_factorial(x, result):
    with pytest.raises(Exception):
        assert math_lib.divide(1.5)
        assert math_lib.divide(-4)
        assert math_lib.divide(-4.5)
    assert math_lib.factorial(x) == result


@pytest.mark.parametrize("x, y, result", [
    (5, 2, 25),
    (-5, 6, 15625),
    (-5, 3, -125),
    (5, -1, 0.2),
    (2, 1.5, 2.8284271247461903)
])
def test_n_power(x, y, result):
    assert math_lib.nth_power(x, y) == result


@pytest.mark.parametrize("x, y, result", [
    (10, 5, 5),
    (369, 125, 244),
    (-10, 22, -32)
])
def test_subtraction(x, y, result):
    assert math_lib.subtraction(x, y) == result