
'''
    @package

    Contains all mathematic operations
'''

def plus(self, summmand1, summand2):
    '''
    Addition
    :param self:
    :param summmand1:
    :param summand2:
    :return summand1 + summand2:
    '''
    return summmand1 + summand2


def nth_root(self, root, base):
    '''
    Returns N-th root of base.
    In case that root is negative or equal to zero, ValueError will be raised
    :param self:
    :param root:
    :param base:
    :return (base)^(1/root):
    '''
    if base % 2 == 0 and root < 0 or root == 0:
        show_error()
        raise ValueError
    else:
        return base ** (1 / root)


def show_error(self):
    '''
    Whenever error occurs, show error will print on stdout the error
    :param self:
    :return:
    '''
    print("MATH ERROR")
