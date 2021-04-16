## @file math_lib.py
# @brief Module with implementation of basic matematic function

## Absolute value, is a non-negative value of x without regard to its sign
# @note | number |
# @param number Number
# @return Absolute value of a number
def absolute_value(number):
    if number >= 0:
        return number
    else:
        return -number


## Factorial of a non-negative integer number, denoted by number!, is the product of all positive integers less than or equal to the number
# @note number!
# @param number Number
# @return Product of all positive integers less than or equal to number
# @exception ValueError if number is float or negative
def factorial(number):
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


## N-th roots are treated as special cases of exponentation, where the exponent is a fraction \f$ \frac{1}{root} \f$
# @note \f$ \sqrt[root]{base} \f$
# @param base Number that will be base of exponentation
# @param root N-th root
# @return [float] N-th root of a number base
# @exception ValueError If base is negative integer and root is odd
def nth_root(root, base):
    # In case od even roots the base cannot be negative
    # Also 0th root is a invalid input
    if base % 2 == 0 and root < 0 or root == 0:
        show_error()
    else:
        return base ** (1 / root)

## Basic addition
# @note summand1 + summand2
# @param summand1 Summand of the addition
# @param summand2 Summand of the addition
# @return Result of the addition
def summary(summmand1, summand2):
    return summmand1 + summand2

## Basic substraction
# @note minuend - subtrahend
# @param minuend Minuend of the substraction
# @param subtrahend Substrahnd of the substraction
# @return Result of substraction
def subtraction(minuend, subtrahend):
    return minuend - subtrahend

## Basic division
# @note \f$ dividend \div divisor \f$
# @param dividend Dividend of the division
# @param divisor Divisor of the divison
# @return [float] Result of a division
def division(dividend, divisor):
    if divisor == 0:
        show_error()
    else:
        return dividend / divisor

## Basic multiplication
# @note \f$ multiplicand \cdot multiplier \f$
# @param multiplicand Multiplicand of a multiplication
# @param multiplier Multiplier of a multiplication
# @return Result of a multiplication
def multiplication(multiplicand, multiplier):
    return multiplicand * multiplier

## When base is a positive integer, exponentiation corresponds to repeated multiplication of the base base times
# @note \f$ base^{exponent} \f$
# @param base Number that will be the base of a power
# @param exponent N-th power
# @return Base to the power of exponent
def nth_power(base, exponent):
    return base ** exponent

## Prints on the calculator screen MATH ERROR
# @exception ValueError
def show_error():
    raise ValueError
    print("MATH ERROR") # TO-DO Print to the GUI
