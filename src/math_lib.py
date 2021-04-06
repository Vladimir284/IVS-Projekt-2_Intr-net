'''
    @package

    Contains all mathematic operations
'''


def absolute_value(value):
    '''
    Returns absolute value of value.
    :param self:
    :param value:
    '''
    if value >= 0:
        return value
    else:
        return -value


def factorial():
    # TODO
    # Since I needed to enumerate the functions, function base is prepared
    # Please implement it
    pass


def nth_root(root, base):
    '''
    Returns N-th root of base.
    In case that root is negative or equal to zero, ValueError will be raised
    :param self:
    :param root:
    :param base:
    :return (base)^(1/root):
    '''

    # In case od even roots the base cannot be negative
    # Also 0th root is a invalid input
    if base % 2 == 0 and root < 0 or root == 0:
        show_error()
        raise ValueError
    else:
        return base ** (1 / root)


def summary(summmand1, summand2):
    '''
    Addition
    :param self:
    :param summmand1:
    :param summand2:
    :return summand1 + summand2:
    '''
    return summmand1 + summand2


def subtraction(minuend, subtrahend):
    '''
    :param minuend:
    :param subtrahend:
    :return: minuend - subtrahend
    '''
    return minuend - subtrahend


def division(dividend, divisor):
    '''
    Return divident divided by divisor.
    If divisor is equal to zero, Value error is raised
    :param self:
    :param dividend:
    :param divisor:
    '''
    if divisor == 0:
        show_error()
        raise ValueError
    else:
        return dividend / divisor


def multiplication(multiplicand, multiplier):
    '''
    Return multiplicand * multiplier
    :param multiplicand:
    :param multiplier:
    :return:
    '''
    return multiplicand * multiplier


def nth_power(base, exponent):
    '''
    :param self:
    :param base: 
    :param exponent: 
    :return: round((base ** exponent), 2)
    '''
    return base ** exponent


def show_error():
    '''
    Whenever error occurs, show error will print on stdout the error
    '''
    print("MATH ERROR")
