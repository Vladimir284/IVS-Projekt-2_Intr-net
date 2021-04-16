## @package memory_operation
# @brief Package with implementation of operations with memory
#
# All of the functions are void and don't take any paramater
#
# @file memory_operation.py
# @brief Module with implementation of operations with memory
#

import calc


## Clears the display
# @note Does not clear the memory
def display_clear():
    calc.clear()
    pass


## Clears the display and the last saved answer (ANS)
def memory_clear():
    calc.c.setMemory(calc.c, 0)
    pass


## Opens manual for the user
# @note opens manual.pdf
def hint_show_man():
    # TO-DO write manual
    pass
