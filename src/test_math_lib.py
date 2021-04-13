## @package test_math_lib
# @brief Tests for mathemathical library
import math_lib
import pytest


@pytest.mark.parametrize("summand1, summand2, result", [
    (10, 10, 20),
    (-10, -10, -20),
    (-10, 10, 0),
    ((1 / 2), (1 / 2), (2 / 2))
])
## Addition tests
# @param summand1 Summand
# @param summand2 Summand
# @param result Expected value
# @test summand1 + summand2 = result
def test_summary(summand1, summand2, result):
    assert math_lib.summary(summand1, summand2) == result


@pytest.mark.parametrize("root, base, result", [
    (3, 8, 2),
    (2, 1, 1),
])
## N-th root tests
# @param root Root of term
# @param base Base of term
# @param result Expected value of finding root
# @test \f$ \sqrt[root]{base} = result \f$
# @test ValueError ecxceptions
def test_nth_root(root, base, result):
    assert math_lib.nth_root(root, base) == result
    with pytest.raises(ValueError):
        math_lib.nth_root(2, -10)
        math_lib.nth_root(0, 3)
    assert math_lib.nth_root(100, 1000) >= 1.07
    assert math_lib.nth_root(2, 20) == 2 * (math_lib.nth_root(2, 5))


@pytest.mark.parametrize("dividend , substrahend, result", [
    (10, 2, 5),
    (15, -5, -3),
    (-15, 3, -5),
    (-15, 7, -2.142857142857143),
    (0, 5, 0),
])
## Division tests
# @param divisor Divisor of divison
# @param dividend Dividend of division
# @param result Expected value of division
# @test \f$ divisor \div dividend = result \f$
# @test Value Error exception
def test_divide(dividend, substrahend, result):
    with pytest.raises(ValueError):
        assert math_lib.division(1, 0)
        assert math_lib.division(-50, 0)
    assert math_lib.division(dividend, substrahend) == result


@pytest.mark.parametrize("number , result", [
    (5, 5),
    (-4, 4),
    (0, 0),
    (-123645789, 123645789),
    (-1.2548, 1.2548)
])
## Absolute value tests
# @param number Number of term
# @param result Expected value from term
# @test \f$ number \geq 0 \Rightarrow |number| = number \f$
# @test \f$ number < 0 \Rightarrow |number| = number \f$
def test_absolute_value(number, result):
    assert math_lib.absolute_value(number) == result


@pytest.mark.parametrize("number, result", [
    (5, 120),
    (0, 1),
    (1, 1),
    (12, 479001600),
    (2, 2),
    (3, 6)
])
## Factorial tests
# @param number number
# @param result Expected value
# @test number! = result
# @test Value Error exceptions
def test_factorial(number, result):
    with pytest.raises(ValueError):
        assert math_lib.factorial(1.5)
        assert math_lib.factorial(-4)
        assert math_lib.factorial(-4.5)
    assert math_lib.factorial(number) == result


@pytest.mark.parametrize("base, power, result", [
    (5, 2, 25),
    (-5, 6, 15625),
    (-5, 3, -125),
    (5, -1, 0.2),
    (2, 1.5, 2.8284271247461903)
])
## N-th power tests
# @param base Base of power
# @param exponent Exponent of power
# @param result Excpected value of power
# @test \f$  base^{exponent} = result \f$
def test_n_power(base, power, result):
    assert math_lib.nth_power(base, power) == result


@pytest.mark.parametrize("minuend, substrahend, result", [
    (10, 5, 5),
    (369, 125, 244),
    (-10, 22, -32)
])
## Substraction tests
# @param minuend Minuend of subsaction
# @param substrahend Substrahend of operation
# @param result Expected value of substraction
# @test minuend - subtrahen = result
def test_subtraction(minuend, substrahend, result):
    assert math_lib.subtraction(minuend, substrahend) == result
