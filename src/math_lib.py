## @package math_lib
# Implementation of basic matematic function


def absolute_value(number):
    ## Absolulte value of a number  \f$ \mid x \mid \f$
    # @note \f$ \mid x \mid \f$
    # @param number from which will be absolute value calculated
    # @return absolute value of a number
    if number >= 0:
        return number
    else:
        return -number


def factorial(number):
    ## Factorial of a non-negative integer number
    # @note number!
    # @param number
    # @return factorial of a number
    # @return If number is float return None
    # @return If number < 0 return None

    # Check if number isnt negative or float
    if number < 0 or number - round(number) != 0:
        show_error()
        raise ValueError
        return None

    # Main factorial algorythm
    if number <= 0:
        return 1
    else:
        return number * factorial(number - 1)


def nth_root(root, base):
    ## N-th roots are treated as special cases of exponentiation, where the exponent is a fraction \f$ \frac{1}{root} \f$
    # @note \f$ \sqrt[n]{root} \f$
    # @param a Number that will be root
    # @param n N-th root, default is 2
    # @return[float] N-th root of number base
    # @return If base is negative integer and base is odd return None

    # In case od even roots the base cannot be negative
    # Also 0th root is a invalid input
    if base % 2 == 0 and root < 0 or root == 0:
        show_error()
        raise ValueError
    else:
        return base ** (1 / root)


def summary(summmand1, summand2):
    ## Basic summary
    # @param summand1
    # @param summand2
    # @return summand1 + summand2

    return summmand1 + summand2


def subtraction(minuend, subtrahend):
    ## Basic substraction
    # @param minuend
    # @param subtrahend
    # @return minuend - subtrahend

    return minuend - subtrahend


def division(dividend, divisor):
    ## Basic division
    # @param dividend
    # @param divisor
    # @return If divisor is 0 return Non
    # @return \f$ dividend \div divisor \f$

    if divisor == 0:
        show_error()
        raise ValueError
        return None
    else:
        return dividend / divisor


def multiplication(multiplicand, multiplier):
    ## Basic multiplication
    # @param multiplicand
    # @param multiplier
    # @return multilicand * multiplier

    return multiplicand * multiplier


def nth_power(base, exponent):
    ## When base is a positive integer, exponentiation corresponds to repeated multiplication of the base n times
    # @note \f$ a^n \f$
    # @param a Number that will be power
    # @param n N-th power
    # @return a to the power of n

    return base ** exponent


def show_error():
    ## Whenever error occurs, MATH_Error is printed just like in standard table calculator

    print("MATH ERROR")