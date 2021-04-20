##
# @package math_lib
# @brief Module with implementation of basic math function
#
# @file math_lib.py
# @brief Implementation of basic mathematical functions
# import calc


##
# Absolute value, is a non-negative value of x without regard to its sign
# @note | number |
# @param number Number
# @return Absolute value of a number
def absolute_value(number):
    if number >= 0:
        return number
    else:
        return -number


##
# Factorial of a number is a product of an integer and all the integers below all the way to 1
# @note number!
# @param number Number
# @return Product of all positive integers less than or equal to number
# @exception ValueError if number is float or negative
def factorial(number):
    # Check if number isn't negative or float
    if number < 0 or number - round(number) != 0:
        show_error()
        raise ValueError

    # Main factorial algorithm
    if number <= 0:
        return 1
    else:
        return number * factorial(number - 1)


##
# N-th roots are treated as special cases of power, where the exponent is a fraction \f$ \frac{1}{root} \f$
# @note \f$ \sqrt[root]{base} \f$
# @param base Number that will be base of power
# @param root N-th root
# @return [float] N-th root of a number base
# @exception ValueError If base is negative integer and root is odd
def nth_root(root, base):
    # In case od even roots the base cannot be negative
    # Also 0th root is a invalid input
    if (root % 2 == 0 and base < 0) or root == 0:
        show_error()
    else:
        return base ** (1 / root)


##
# Basic addition
# @note summand1 + summand2
# @param summand1 Summand of the addition
# @param summand2 Summand of the addition
# @return Result of the addition
def summary(summand1, summand2):
    return summand1 + summand2


##
# Basic subtraction
# @note minuend - subtrahend
# @param minuend Minuend of the subtraction
# @param subtrahend Subtrahend of the subtraction
# @return Result of subtraction
def subtraction(minuend, subtrahend):
    return minuend - subtrahend


##
# Basic division
# @note \f$ dividend \div divisor \f$
# @param dividend Dividend of the division
# @param divisor Divisor of the divison
# @return [float] Result of a division
def division(dividend, divisor):
    if divisor == 0:
        show_error()
    else:
        return dividend / divisor


##
# Basic multiplication
# @note \f$ multiplicand \cdot multiplier \f$
# @param multiplicand Multiplicand of a multiplication
# @param multiplier Multiplier of a multiplication
# @return Result of a multiplication
def multiplication(multiplicand, multiplier):
    return multiplicand * multiplier


##
# When base is a positive integer, exponentiation corresponds to repeated multiplication of the base base times
# @note \f$ base^{exponent} \f$
# @param base Number that will be the base of a power
# @param exponent N-th power
# @return Base to the power of exponent
def nth_power(base, exponent):
    return base ** exponent


##
# Raises ValueError
# @exception ValueError
def show_error():
    raise ValueError
