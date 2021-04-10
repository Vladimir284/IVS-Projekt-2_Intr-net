import math_lib
import memory_operation


class Calculator:
    '''
    Stores values of memory and contains operands methods
    '''
    value1 = 0
    value2 = 0
    ID_Operation = ""

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

    def executeOperation(self):
        '''
        @brief Executes operation depending on ID of operation
        @param ID_Operation:
        @return Result of operation
        '''

        if self.ID_Operation == 0:
            return math_lib.summary(self.value1, self.value2)
        elif self.ID_Operation == 1:
            return math_lib.subtraction(self.value1, self.value2)
        elif self.ID_Operation == 2:
            return math_lib.division(self.value1, self.value2)
        elif self.ID_Operation == 3:
            return math_lib.multiplication(self.value1, self.value2)
        elif self.ID_Operation == 4:
            return math_lib.nth_power(self.value1, self.value2)
        elif self.ID_Operation == 5:
            return math_lib.nth_root(self.value1, self.value2)
        elif self.ID_Operation == 6:
            return math_lib.absolute_value(self.value1)
        elif self.ID_Operation == 7:
            return math_lib.factorial(self.value1)


pass