## @package calc
# @brief Package with GUI
## @file calc.py
# @brief Module with GUI
import tkinter as tk
import memory_operation
from main import Calculator
import subprocess

## New instance of class object c
c = Calculator

##
# New instance of class tkinter???
calc = tk.Tk()

##
# Defining the title of the calculator
calc.title("Calculator")

##
# Defining the default size of the calculator
calc.minsize(400, 200)

#
## TO-DO Def
weight = 0

#
## TO-DO Def
row = 0


#
## TO-DO Def
column = 0

#
## TO-DO Def
columnspan = 0


tk.Grid.rowconfigure(calc, 0, weight=1)
for i in range(5):
    tk.Grid.columnconfigure(calc, i, weight=1)

#
## TO-DO Def
display = tk.Entry(calc, width=30)
display.grid(row=0, column=0, columnspan=5, sticky="nesw")
display.config(justify="right")


## Inserts the number on the display
# @param number - Number, which is to be insert on the display
# @return void, inserts the number on the display
def string_button_click(number):
    display.insert("insert", number)


## Clears the display and the last saved answer
# @return void, deletes the memory and the display
def all_clear():
    c.setMemory(c, 0)
    c.setOperand(c, 0)
    clear()
    # TODO: delete memory


# Clears the display
# @note keeps the last saved answer
# @return void, clears the display
def clear():
    display.delete(0, "end")


## When the '=' is pressed, this will calculate the result
# @note Also checks for some not-a-number characters
# @return void, calls directly different functions
def calculate():
    if display.get() and display.get().replace('.', '', 1).isdigit():
        c.setOperand(c, float(display.get()))
        display.delete(0, "end")
        display.insert("insert", c.executeOperation(c))
        c.setMemory(c, c.executeOperation(c))
    else:
        all_clear()
        display.insert("insert", "SYNTAX ERROR")


## Stores the display value into the variable and also stores the operation which will be made
# @note also checks for the not-a-number characters
# @param id_op - ID of the operation
# @return void, calls directly different functions
def operation(id_op):
    if id_op == 1 and not display.get():
        display.insert("insert", '-')
    elif display.get() and display.get().replace('.', '', 1).isdigit():
        c.setMemory(c, float(display.get()))
        c.setID(c, id_op)
        if c.getID(c) == 6 or c.getID(c) == 7:
            clear()
            display.insert("insert", c.executeOperation(c))
        else:
            clear()
    else:
        all_clear()
        display.insert("insert", "SYNTAX ERROR")


## Shows the manual for the user
# @return void, shows the manual
def show_hint():
    # TODO call function from memory operations
    subprocess.run(['gedit', 'ahoj.txt'])


## Makes the keyboard buttons and operations work correctly
# @note Delete the character specific for the operation, so the string can be converted to the integer(float)
# @param x - the ID of the operation
# @return void, calls directly the function operation
def key_operation(x):
    display.delete(len(display.get()) - 1)
    operation(x)


# TODO memory operation


# buttons def
# TO-DO Definition of each button


##
# Calculator button - Insert zero on the display
num_0 = tk.Button(calc, text="0", command=lambda: string_button_click("0"))

##
# Calculator button - Insert one on the display
num_1 = tk.Button(calc, text="1", command=lambda: string_button_click("1"))

##
# Calculator button - Insert two on the display
num_2 = tk.Button(calc, text="2", command=lambda: string_button_click("2"))

##
# Calculator button - Insert three on the display
num_3 = tk.Button(calc, text="3", command=lambda: string_button_click("3"))

##
# Calculator button - Insert four on the display
num_4 = tk.Button(calc, text="4", command=lambda: string_button_click("4"))

##
# Calculator button - Insert five on the display
num_5 = tk.Button(calc, text="5", command=lambda: string_button_click("5"))

##
# Calculator button - Insert six on the display
num_6 = tk.Button(calc, text="6", command=lambda: string_button_click("6"))

##
# Calculator button - Insert seven on the display
num_7 = tk.Button(calc, text="7", command=lambda: string_button_click("7"))

##
# Calculator button - Insert eight on the display
num_8 = tk.Button(calc, text="8", command=lambda: string_button_click("8"))

##
# Calculator button - Insert nine on the display
num_9 = tk.Button(calc, text="9", command=lambda: string_button_click("9"))

##
# Calculator button - Makes the nth root of the given number
n_root = tk.Button(calc, text="x^1/n", command=lambda: operation(5))

##
# Calculator button - Makes the nth power of the given number
n_power = tk.Button(calc, text="x^n", command=lambda: operation(4))

##
# Calculator button - Makes the absolute value of the number
absolute_value = tk.Button(calc, text="|x|", command=lambda: operation(6))

##
# Calculator button - Makes the factorial of the given number
factorial = tk.Button(calc, text="x!", command=lambda: operation(7))

##
# Calculator button - Clears the display
All_clear = tk.Button(calc, text="AC", command=lambda: all_clear())

##
# Calculator button - Clears the display and the last saved answer
C_clear = tk.Button(calc, text="C", command=lambda: clear())

##
# Calculator button - Shows the manual for the user
hint = tk.Button(calc, text="HINT", command=lambda: show_hint())

##
# Calculator button - Makes the summary of the number on the display and the next given number
plus = tk.Button(calc, text="+", command=lambda: operation(0))

##
# Calculator button - Makes the distinction of the number on the display and the next given number
minus = tk.Button(calc, text="-", command=lambda: operation(1))

##
# Calculator button - Makes the multiplication of the number on the display and the next given number
times = tk.Button(calc, text="*", command=lambda: operation(3))

##
# Calculator button - Divide the number on the display and the next given number
divide = tk.Button(calc, text="/", command=lambda: operation(2))

##
# Calculator button - Shows the result
result = tk.Button(calc, text="=", command=lambda: calculate())

##
# Calculator button - Insert "." on the display
dot = tk.Button(calc, text=".", command=lambda: string_button_click("."))

##
# Calculator button - Shows the last saved answer
ans = tk.Button(calc, text="ANS", command=lambda: string_button_click(c.getMemory(c)))

##
# The array of the buttons which are in the calculator
# buttons position using grid // You can do better
buttons_array = [hint, All_clear, C_clear, ans, divide, n_power, num_7, num_8, num_9, times, n_root, num_4, num_5,
                 num_6,
                 minus, factorial, num_1, num_2, num_3, plus, absolute_value, num_0, num_0, dot, result]
for i in range(1, 26):
    if i != 22 or i != 23:
        buttons_array[i - 1].grid(row=int(i / 5 if i % 5 == 0 else i / 5 + 1),
                                  column=int(i % 5 - 1 if i % 5 != 0 else 4),
                                  sticky="nesw")

num_0.grid(row=5, column=1, columnspan=2)

##
# Keyboard buttons connected to their operations
calc.bind('<Return>', lambda e: calculate())
calc.bind('<KP_Enter>', lambda e: calculate())
calc.bind('<Escape>', lambda e: exit(0))

calc.bind('<KP_Add>', lambda e: key_operation(0))
calc.bind('<KP_Subtract>', lambda e: key_operation(1))
calc.bind('<KP_Multiply>', lambda e: key_operation(3))
calc.bind('<KP_Divide>', lambda e: key_operation(2))

calc.mainloop()
