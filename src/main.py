## @file main.py
# @brief TO-DO
import math_lib
import memory_operation


# fixme Finish the comments

#  TO-DO write here what class are we talking about
# @note TO-DO If you have something to add type it here, might not be needed
# @brief TO-DO Surely type here briefly about calculator, what id does#
#
# TO-DO If needed, detailed description will be here

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

    ## TO-DO Again, what function are we talking about and also
    # @note TO-DO If you have something to add
    # @param TO-DO After @param, type name of parameter and after it what it represents, For each param youll have one line
    # @return TO-DO What this function retuns
    def getMemory(self):
        return Calculator.__Last_saved_answer
        pass

    ## TO-DO Again, what function are we talking about and also
    # @note TO-DO If you have something to add
    # @param TO-DO After @param, type name of parameter and after it what it represents, For each param youll have one line
    # @return TO-DO What this function retuns
    def setMemory(self, value):
        Calculator.__Last_saved_answer = value
        pass

    ## TO-DO Again, what function are we talking about and also
    # @note TO-DO If you have something to add
    # @param TO-DO After @param, type name of parameter and after it what it represents, For each param youll have one line
    # @return TO-DO What this function retuns
    def getOperand(self):
        return Calculator.__ID_Operation
        pass

    ## TO-DO Again, what function are we talking about and also
    # @note TO-DO If you have something to add
    # @param TO-DO After @param, type name of parameter and after it what it represents, For each param youll have one line
    # @return TO-DO What this function retuns
    def setOperand(self, ID_Operation):
        Calculator.__ID_Operation = ID_Operation
        pass

    ## TO-DO Again, what function are we talking about and also
    # @note TO-DO If you have something to add
    # @param TO-DO After @param, type name of parameter and after it what it represents, For each param youll have one line
    # @return TO-DO What this function retuns
    def executeOperation(self):

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
