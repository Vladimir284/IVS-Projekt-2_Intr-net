import math_lib
import memory_operation


class Calculator:
    '''
    Stores values of memory and contains operands methods
    '''

    def __init__(self):
        '''
        Constructor
        Every parameter will be set to zero
        '''
        _Operand = 0.0
        _ID_operation = 0
        _Last_answer = 0

    def getMemory(self):
        '''
        Return values currently stored on memory
        :return:
        '''
        pass

    def setMemory(self):
        '''
        Set memory on current value
        :return:
        '''
        pass

    def getOperand(self):
        '''
        Read from In.
        :return:
        '''
        pass

    def setOperand(self):
        '''
        Set ID of next operation depending on opration entered
        :return:
        '''
        pass

    def executeOpration(self, ID_Operation):
        '''
        Executes operation depending on param.
        :param ID_Operation:
        :return:
        '''
        pass


# TODO
# Depends on memory_operation implements
# Implementation might be needed in module memory_operation - Discuss
Operations = ["absolute_value", "factorial", "nth_root", "summary", "substraction", "division", "multiplication",
              "nth_power", "memory_recall", "display_clear", "ans", "memory_clear", "hint"]
