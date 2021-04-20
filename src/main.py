## @file main.py
# @brief declares class Calculator
import math_lib


## @class Calculator
# @brief Instance holds 3 values and her methods
#
#
# Values:
# 1. Last saved answer
# 2. Operand
# 3. ID of operation
#
# All of the varriables are initialised to zero
# Class also holds all its methods

class Calculator:
    ##
    # Number stored in memory
    __Last_saved_answer = 0

    ##
    # Next number that will be processed
    __Operand = 0

    ##
    # ID of next operation
    __ID_Operation = ""


    ## Gets Last saved answer
    # @return Last saved answer
    def getMemory(self):
        return Calculator.__Last_saved_answer
        pass

    ## Sets Last saved answer
    # @param value Number which is saved as Last saved answer

    def setMemory(self, value):
        Calculator.__Last_saved_answer = value
        pass

    ## Gets operand
    # @return Operand
    def getOperand(self):
        return Calculator.__Operand
        pass

    ## Sets Operand on value
    # @param value Value on which is operand set
    def setOperand(self, value):
        Calculator.__Operand = value
        pass

    ## Sets ID of operation
    # @param value Sets ID of opration on value
    def setID(self, value):
        Calculator.__ID_Operation = value
        pass

    ## Gets ID of operation
    def getID(self):
        return Calculator.__ID_Operation
        pass

    ## Executes mathematical operation based on ID
    def executeOperation(self):

        if self.__ID_Operation == 0:
            return math_lib.summary(self.__Last_saved_answer, self.__Operand)
        elif self.__ID_Operation == 1:
            return math_lib.substraction(self.__Last_saved_answer, self.__Operand)
        elif self.__ID_Operation == 2:
            return math_lib.division(self.__Last_saved_answer, self.__Operand)
        elif self.__ID_Operation == 3:
            return math_lib.multiplication(self.__Last_saved_answer, self.__Operand)
        elif self.__ID_Operation == 4:
            return math_lib.nth_power(self.__Last_saved_answer, self.__Operand)
        elif self.__ID_Operation == 5:
            return math_lib.nth_root(self.__Last_saved_answer, self.__Operand)
        elif self.__ID_Operation == 6:
            return math_lib.absolute_value(self.__Last_saved_answer)
        elif self.__ID_Operation == 7:
            return math_lib.factorial(self.__Last_saved_answer)


pass
