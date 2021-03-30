import tkinter as tk

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


def clear_click():
    display.delete(0, "end")


def calculate():
    display.delete(0, "end")
    display.insert("insert", "random")


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
n_root = tk.Button(calc, text="x^1/n")
n_power = tk.Button(calc, text="x^n")
absolute_value = tk.Button(calc, text="|x|")
factorial = tk.Button(calc, text="x!")
all_clear = tk.Button(calc, text="AC", command=lambda: all_clear_click())
clear = tk.Button(calc, text="C", command=lambda: clear_click())
l_bracket = tk.Button(calc, text="(", command=lambda: string_button_click("("))
r_bracket = tk.Button(calc, text=")", command=lambda: string_button_click(")"))
plus = tk.Button(calc, text="+", command=lambda: string_button_click("+"))
minus = tk.Button(calc, text="-", command=lambda: string_button_click("-"))
times = tk.Button(calc, text="*", command=lambda: string_button_click("*"))
divide = tk.Button(calc, text="/", command=lambda: string_button_click("/"))
result = tk.Button(calc, text="=", command=lambda: calculate())
dot = tk.Button(calc, text=".", command=lambda: string_button_click("."))
ans = tk.Button(calc, text="ANS")

# buttons position using grid
buttons_array = [l_bracket, r_bracket, n_power, n_root, all_clear, num_7, num_8, num_9, divide, clear, num_4, num_5,
                 num_6, times, factorial, num_1, num_2, num_3, minus, absolute_value, num_0, dot, result, plus, ans]
for i in range(1, 26):
    buttons_array[i - 1].grid(row=int(i / 5 if i % 5 == 0 else i / 5 + 1), column=int(i % 5 - 1 if i % 5 != 0 else 4),
                              sticky="nesw")

# keyboard events
calc.bind('<Return>', lambda e: calculate())
calc.bind('<Escape>', lambda e: exit(0))
# TODO: help(f1) and more

calc.mainloop()
