# @file calc.py
# @brief Module with GUI
import tkinter as tk
import memory_operation
from main import Calculator
import subprocess

## New instance of class object c
c = Calculator

#
## TO-DO Def
calc = tk.Tk()
calc.title("Calculator")
calc.minsize(400, 200)

#
## TO-DO Def
weight = 0

tk.Grid.rowconfigure(calc, 0, weight=1)
for i in range(5):
    tk.Grid.columnconfigure(calc, i, weight=1)

#
## TO-DO Def
display = tk.Entry(calc, width=30)
display.grid(row=0, column=0, columnspan=5, sticky="nesw")
display.config(justify="right")


## TO-DO Again, what function are we talking about and also
# @note TO-DO If you have something to add
# @param TO-DO After param, type name of parameter and after it what it represents, For each param youll have one line
# @return TO-DO What this function retuns
def string_button_click(number):
    display.insert("insert", number)


## TO-DO Again, what function are we talking about and also
# @note TO-DO If you have something to add
# @param TO-DO After @param, type name of parameter and after it what it represents, For each param youll have one line
# @return TO-DO What this function retuns
def all_clear_click():
    display.delete(0, "end")
    c.value1 = 0
    # TODO: delete memory


## TO-DO Again, what function are we talking about and also
# @note TO-DO If you have something to add
# @param TO-DO After @param, type name of parameter and after it what it represents, For each param youll have one line
# @return TO-DO What this function retuns
def clear():
    display.delete(0, "end")


## TO-DO Again, what function are we talking about and also
# @note TO-DO If you have something to add
# @param TO-DO After @param, type name of parameter and after it what it represents, For each param youll have one line
# @return TO-DO What this function returns
def calculate():
    if display.get() and display.get().replace('.', '', 1).isdigit():
        # c.value2 = float(display.get())
        c.setOperand(float(display.get()))


        c.setMemory(c, 10)

        c.


        display.delete(0, "end")
        display.insert("insert", c.executeOperation(c))
        c.value1 = c.executeOperation(c)
    else:
        clear()


## TO-DO Again, what function are we talking about and also
# @note TO-DO If you have something to add
# @param TO-DO After @param, type name of parameter and after it what it represents, For each param youll have one line
# @return TO-DO What this function returns
def operation(x):
    if x == 1 and not display.get():
        display.insert("insert", '-')
    elif display.get() and display.get().replace('.', '', 1).isdigit():
        c.value1 = float(display.get())
        c.ID_Operation = x
        if c.ID_Operation == 6 or c.ID_Operation == 7:
            clear()
            display.insert("insert", c.executeOperation(c))
        else:
            clear()
    else:
        clear()


## TO-DO Again, what function are we talking about and also
# @note TO-DO If you have something to add
# @param TO-DO After param, type name of parameter and after it what it represents, For each param youll have one line
# @return TO-DO What this function returns
def show_hint():
    # TODO call function from memory operations
    subprocess.run(['gedit', 'ahoj.txt'])


## TO-DO Again, what function are we talking about and also
# @note TO-DO If you have something to add
# @param TO-DO After @param, type name of parameter and after it what it represents, For each param youll have one line
# @return TO-DO What this function returns
def key_operation(x):
    display.delete(len(display.get()) - 1)
    operation(x)


# TODO ANS
# TODO memory operation
# TODO input


# buttons def
# TO-DO Definition of each button


#
## TO-DO Def
num_0 = tk.Button(calc, text="0", command=lambda: string_button_click("0"))

##
# TO-DO Def
num_1 = tk.Button(calc, text="1", command=lambda: string_button_click("1"))

##
# TO-DO Def
num_2 = tk.Button(calc, text="2", command=lambda: string_button_click("2"))

##
# TO-DO Def
num_3 = tk.Button(calc, text="3", command=lambda: string_button_click("3"))

##
# TO-DO Def
num_4 = tk.Button(calc, text="4", command=lambda: string_button_click("4"))

##
# TO-DO Def
num_5 = tk.Button(calc, text="5", command=lambda: string_button_click("5"))

##
# TO-DO Def
num_6 = tk.Button(calc, text="6", command=lambda: string_button_click("6"))

##
# TO-DO Def
num_7 = tk.Button(calc, text="7", command=lambda: string_button_click("7"))

##
# TO-DO Def
num_8 = tk.Button(calc, text="8", command=lambda: string_button_click("8"))

##
# TO-DO Def
num_9 = tk.Button(calc, text="9", command=lambda: string_button_click("9"))

##
# TO-DO Def
n_root = tk.Button(calc, text="x^1/n", command=lambda: operation(5))

##
# TO-DO Def
n_power = tk.Button(calc, text="x^n", command=lambda: operation(4))

##
# TO-DO Def
absolute_value = tk.Button(calc, text="|x|", command=lambda: operation(6))

##
# TO-DO Def
factorial = tk.Button(calc, text="x!", command=lambda: operation(7))

##
# TO-DO Def
all_clear = tk.Button(calc, text="AC", command=lambda: all_clear_click())

##
# TO-DO Def
C_clear = tk.Button(calc, text="C", command=lambda: clear())

##
# TO-DO Def
hint = tk.Button(calc, text="HINT", command=lambda: show_hint())

##
# TO-DO Def
plus = tk.Button(calc, text="+", command=lambda: operation(0))

##
# TO-DO Def
minus = tk.Button(calc, text="-", command=lambda: operation(1))

##
# TO-DO Def
times = tk.Button(calc, text="*", command=lambda: operation(3))

##
# TO-DO Def
divide = tk.Button(calc, text="/", command=lambda: operation(2))

##
# TO-DO Def
result = tk.Button(calc, text="=", command=lambda: calculate())

##
# TO-DO Def
dot = tk.Button(calc, text=".", command=lambda: string_button_click("."))

##
# TO-DO Def
ans = tk.Button(calc, text="ANS", command=lambda: string_button_click(c.value1))

##
# TO-DO Def
# buttons position using grid // You can do better
buttons_array = [hint, all_clear, C_clear, ans, divide, n_power, num_7, num_8, num_9, times, n_root, num_4, num_5,
                 num_6,
                 minus, factorial, num_1, num_2, num_3, plus, absolute_value, num_0, num_0, dot, result]
for i in range(1, 26):
    if i != 22 or i != 23:
        buttons_array[i - 1].grid(row=int(i / 5 if i % 5 == 0 else i / 5 + 1),
                                  column=int(i % 5 - 1 if i % 5 != 0 else 4),
                                  sticky="nesw")

num_0.grid(row=5, column=1, columnspan=2)

# keyboard events
calc.bind('<Return>', lambda e: calculate())
calc.bind('<KP_Enter>', lambda e: calculate())
calc.bind('<Escape>', lambda e: exit(0))

calc.bind('<KP_Add>', lambda e: key_operation(0))
calc.bind('<KP_Subtract>', lambda e: key_operation(1))
calc.bind('<KP_Multiply>', lambda e: key_operation(2))
calc.bind('<KP_Divide>', lambda e: key_operation(3))

calc.mainloop()
