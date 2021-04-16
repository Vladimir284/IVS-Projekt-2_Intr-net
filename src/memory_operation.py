## @file memory_operation.py
# @brief Module with implementation of operations with memory
#
# All of the functions are void and don't take any paramater

import calc


## Clears the display
## TO-DO Again, what function are we talking about and also
# @note TO-DO If you have something to add
# @param TO-DO After @param, type name of parameter and after it what it represents, For each param youll have one line
# @return TO-DO What this function retuns
def display_clear():
    calc.clear()
    pass


## Clears the display and the last saved answer (ANS)
## TO-DO Again, what function are we talking about and also
# @note TO-DO If you have something to add
# @param TO-DO After @param, type name of parameter and after it what it represents, For each param youll have one line
# @return TO-DO What this function retuns
def memory_clear():
    calc.c.setMemory(calc.c, 0)
    pass


## Opens manual for the user
## TO-DO Again, what function are we talking about and also
# @note TO-DO If you have something to add
# @param TO-DO After @param, type name of parameter and after it what it represents, For each param youll have one line
# @return TO-DO What this function retuns
def hint_show_man():
    # TO-DO write manual
    pass
