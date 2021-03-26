'''
    @package

    Contains all mathematic operations
'''


def plus(summmand1, summand2):
    '''
    Addition
    :param self:
    :param summmand1:
    :param summand2:
    :return summand1 + summand2:
    '''
    return summmand1 + summand2


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


def show_error():
    '''
    Whenever error occurs, show error will print on stdout the error
    '''
    print("MATH ERROR")
