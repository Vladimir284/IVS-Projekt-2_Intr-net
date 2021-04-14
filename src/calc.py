# @file calc.py
# @brief Module with GUI
import tkinter as tk
import memory_operation
from main import Calculator as c
import subprocess

calc = tk.Tk()
calc.title("Calculator")
calc.minsize(400, 200)

tk.Grid.rowconfigure(calc, 0, weight=1)
for i in range(5):
    tk.Grid.columnconfigure(calc, i, weight=1)

display = tk.Entry(calc, width=30)
display.grid(row=0, column=0, columnspan=5, sticky="nesw")
display.config(justify="right")


def string_button_click(number):
    display.insert("insert", number)


def all_clear_click():
    display.delete(0, "end")
    # TODO: delete memory


def clear():
    display.delete(0, "end")


def calculate():
    if display.get() and display.get().isnumeric():
        c.value2 = float(display.get())
        display.delete(0, "end")
        display.insert("insert", c.executeOperation(c))
    else:
        clear()


def operation(x):
    if x == 1 and not display.get():
        display.insert("insert", '-')
    elif display.get() and display.get().isnumeric():
        c.value1 = float(display.get())
        c.ID_Operation = x
        if c.ID_Operation == 6 or c.ID_Operation == 7:
            clear()
            display.insert("insert", c.executeOperation(c))
        else:
            clear()
    else:
        clear()


def show_hint():
    # TODO call function from memory operations
    subprocess.run(['gedit', 'ahoj.txt'])


def key_operation(x):
    display.delete(len(display.get()) - 1)
    operation(x)


# TODO ANS
# TODO memory operation
# TODO input
# buttons def
num_0 = tk.Button(calc, text="0", command=lambda: string_button_click("0"))
num_1 = tk.Button(calc, text="1", command=lambda: string_button_click("1"))
num_2 = tk.Button(calc, text="2", command=lambda: string_button_click("2"))
num_3 = tk.Button(calc, text="3", command=lambda: string_button_click("3"))
num_4 = tk.Button(calc, text="4", command=lambda: string_button_click("4"))
num_5 = tk.Button(calc, text="5", command=lambda: string_button_click("5"))
num_6 = tk.Button(calc, text="6", command=lambda: string_button_click("6"))
num_7 = tk.Button(calc, text="7", command=lambda: string_button_click("7"))
num_8 = tk.Button(calc, text="8", command=lambda: string_button_click("8"))
num_9 = tk.Button(calc, text="9", command=lambda: string_button_click("9"))
n_root = tk.Button(calc, text="x^1/n", command=lambda: operation(5))
n_power = tk.Button(calc, text="x^n", command=lambda: operation(4))
absolute_value = tk.Button(calc, text="|x|", command=lambda: operation(6))
factorial = tk.Button(calc, text="x!", command=lambda: operation(7))
all_clear = tk.Button(calc, text="AC", command=lambda: all_clear_click())
C_clear = tk.Button(calc, text="C", command=lambda: clear())
hint = tk.Button(calc, text="HINT", command=lambda: show_hint())
plus = tk.Button(calc, text="+", command=lambda: operation(0))
minus = tk.Button(calc, text="-", command=lambda: operation(1))
times = tk.Button(calc, text="*", command=lambda: operation(3))
divide = tk.Button(calc, text="/", command=lambda: operation(2))
result = tk.Button(calc, text="=", command=lambda: calculate())
dot = tk.Button(calc, text=".", command=lambda: string_button_click("."))
ans = tk.Button(calc, text="ANS")

# buttons position using grid
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
