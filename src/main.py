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
        @return Last saved answr
        '''
        pass

    def setMemory(self):
        '''
        Set memory on current value
        '''
        pass

    def getOperand(self):
        '''
        Read from In.
        '''
        pass

    def setOperand(self):
        '''
        Set ID of next operation depending on opration entered
        '''
        pass

    def executeOpration(self, ID_Operation):
        '''
        @brief Executes operation depending on ID of operation
        @param ID_Operation:
        @return Result of operation
        '''
        pass
