# @package calc
# @brief Package with GUI
# @file calc.py
# @brief Module with GUI
import tkinter as tk
import memory_operation
from main import Calculator
from tkinter import *
import subprocess

##
# New instance of class object c
c = Calculator

##
# New instance of class tkinter???
calc = tk.Tk()

##
# Defining the title of the calculator
calc.title("Calculator")

##
# Defining the default size of the calculator
calc.minsize(720, 300)

##
# TO-DO Def
weight = 0

##
# TO-DO Def
row = 0

##
# TO-DO Def
column = 0

##
# TO-DO Def
columnspan = 0

tk.Grid.rowconfigure(calc, 0, weight=1)
for i in range(5):
    tk.Grid.columnconfigure(calc, i, weight=1)

##
# TO-DO Def
display = tk.Entry(calc, font="Calibri 20", width=30)
display.grid(row=0, column=0, columnspan=5, sticky="nesw")
display.config(justify="right")


##
# Inserts the number on the display
# @param number - Number, which is to be insert on the display
# @return void, inserts the number on the display
def string_button_click(number):
    display.insert("insert", number)


##
# Clears the display and the last saved answer
# @return void, deletes the memory and the display
def all_clear():
    c.setMemory(c, 0)
    c.setOperand(c, 0)
    clear()
    # TODO: delete memory


##
# Clears the display
# @note keeps the last saved answer
# @return void, clears the display
def clear():
    display.delete(0, "end")


##
# When the '=' is pressed, this will calculate the result
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


##
# Stores the display value into the variable and also stores the operation which will be made
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


##
# Shows the manual for the user
# @return void, shows the manual
def show_hint():
    # TODO call function from memory operations
    subprocess.run(['gedit', 'ahoj.txt'])


##
# Makes the keyboard buttons and operations work correctly
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
# Sets width of a button
width = 0

##
# Sets height of a button
height = 0

##
# Contains data about specified image which will be put on the button
image = PhotoImage(file="buttons_images/0.gif")

##
# Calculator button - Insert zero on the display
num_0 = tk.Button(calc, image=image, width=40, height=45, command=lambda: string_button_click("0"))

# Save the image so it won't be deleted by thrash cleaner
num_0.image = image

# Change image
image = PhotoImage(file="buttons_images/1.gif")

##
# Calculator button - Insert one on the display
num_1 = tk.Button(calc, image=image, width=30, height=45, command=lambda: string_button_click("1"))

# Save the image so it won't be deleted by thrash cleaner
num_1.image = image

# Change image
image = PhotoImage(file="buttons_images/2.gif")

##
# Calculator button - Insert two on the display
num_2 = tk.Button(calc, image=image, width=30, height=45, command=lambda: string_button_click("2"))

# Save the image so it won't be deleted by thrash cleaner
num_2.image = image

# Change image
image = PhotoImage(file="buttons_images/3.gif")

##
# Calculator button - Insert three on the display
num_3 = tk.Button(calc, image=image, width=30, height=45, command=lambda: string_button_click("3"))

# Save the image so it won't be deleted by thrash cleaner
num_3.image = image

# Change image
image = PhotoImage(file="buttons_images/4.gif")

##
# Calculator button - Insert four on the display
num_4 = tk.Button(calc, image=image, width=30, height=45, command=lambda: string_button_click("4"))

# Save the image so it won't be deleted by thrash cleaner
num_4.image = image

# Change image
image = PhotoImage(file="buttons_images/5.gif")

##
# Calculator button - Insert five on the display
num_5 = tk.Button(calc, image=image, width=30, height=45, command=lambda: string_button_click("5"))

# Save the image so it won't be deleted by thrash cleaner
num_5.image = image

# Change image
image = PhotoImage(file="buttons_images/6.gif")

##
# Calculator button - Insert six on the display
num_6 = tk.Button(calc, image=image, width=30, height=45, command=lambda: string_button_click("6"))

# Save the image so it won't be deleted by thrash cleaner
num_6.image = image

# Change image
image = PhotoImage(file="buttons_images/7.gif")

##
# Calculator button - Insert seven on the display
num_7 = tk.Button(calc, image=image, width=30, height=45, command=lambda: string_button_click("7"))

# Save the image so it won't be deleted by thrash cleaner
num_7.image = image

# Change image
image = PhotoImage(file="buttons_images/8.gif")

##
# Calculator button - Insert eight on the display
num_8 = tk.Button(calc, image=image, width=30, height=45, command=lambda: string_button_click("8"))

# Save the image so it won't be deleted by thrash cleaner
num_8.image = image

# Change image
image = PhotoImage(file="buttons_images/9.gif")

##
# Calculator button - Insert nine on the display
num_9 = tk.Button(calc, image=image, width=30, height=45, command=lambda: string_button_click("9"))

# Save the image so it won't be deleted by thrash cleaner
num_9.image = image

# Change image
image = PhotoImage(file="buttons_images/n-th_root.gif")

##
# Calculator button - Makes the nth root of the given number
n_root = tk.Button(calc, image=image, width=30, height=45, command=lambda: operation(5))

# Save the image so it won't be deleted by thrash cleaner
n_root.image = image

# Change image
image = PhotoImage(file="buttons_images/n-th_power.gif")

##
# Calculator button - Makes the nth power of the given number
n_power = tk.Button(calc, image=image, width=30, height=45, command=lambda: operation(4))

# Save the image so it won't be deleted by thrash cleaner
n_power.image = image

# Change image
image = PhotoImage(file="buttons_images/abs.gif")

##
# Calculator button - Makes the absolute value of the number
absolute_value = tk.Button(calc, image=image, width=30, height=45, command=lambda: operation(6))

# Save the image so it won't be deleted by thrash cleaner
absolute_value.image = image

# Change image
image = PhotoImage(file="buttons_images/factorial.gif")

##
# Calculator button - Makes the factorial of the given number
factorial = tk.Button(calc, image=image, width=30, height=45, command=lambda: operation(7))

# Save the image so it won't be deleted by thrash cleaner
factorial.image = image

# Change image
image = PhotoImage(file="buttons_images/clear_memory.gif")

##
# Calculator button - Clears the display Code review Code-review
All_clear = tk.Button(calc, image=image, width=30, height=45, command=lambda: all_clear())

# Save the image so it won't be deleted by thrash cleaner
All_clear.image = image

# Change image
image = PhotoImage(file="buttons_images/clear_display.gif")

##
# Calculator button - Clears the display and the last saved answer  Code-review
C_clear = tk.Button(calc, image=image, width=30, height=45, command=lambda: clear())

# Save the image so it won't be deleted by thrash cleaner
C_clear.image = image

# Change image
image = PhotoImage(file="buttons_images/hint.gif")

##
# Calculator button - Shows the manual for the user
hint = tk.Button(calc, image=image, width=30, height=45, command=lambda: show_hint())

# Save the image so it won't be deleted by thrash cleaner
hint.image = image

# Change image
image = PhotoImage(file="buttons_images/plus.gif")

##
# Calculator button - Makes the summary of the number on the display and the next given number
plus = tk.Button(calc, image=image, width=30, height=45, command=lambda: operation(0))

# Save the image so it won't be deleted by thrash cleaner
plus.image = image

# Change image
image = PhotoImage(file="buttons_images/minus.gif")

##
# Calculator button - Makes the distinction of the number on the display and the next given number
minus = tk.Button(calc, image=image, width=30, height=45, command=lambda: operation(1))

# Save the image so it won't be deleted by thrash cleaner
minus.image = image

# Change image
image = PhotoImage(file="buttons_images/multiply.gif")

##
# Calculator button - Makes the multiplication of the number on the display and the next given number
times = tk.Button(calc, image=image, width=30, height=45, command=lambda: operation(3))

# Save the image so it won't be deleted by thrash cleaner
times.image = image

# Change image
image = PhotoImage(file="buttons_images/divide.gif")
##

# Calculator button - Divide the number on the display and the next given number
divide = tk.Button(calc, image=image, width=30, height=45, command=lambda: operation(2))

# Save the image so it won't be deleted by thrash cleaner
divide.image = image

# Change image
image = PhotoImage(file="buttons_images/equals.gif")

##
# Calculator button - Shows the result
result = tk.Button(calc, image=image, width=30, height=45, command=lambda: calculate())

# Save the image so it won't be deleted by thrash cleaner
result.image = image

# Change image
image = PhotoImage(file="buttons_images/colon.gif")

##
# Calculator button - Insert "." on the display
dot = tk.Button(calc, image=image, width=30, height=45, command=lambda: string_button_click("."))

# Save the image so it won't be deleted by thrash cleaner
dot.image = image

# Change image
image = PhotoImage(file="buttons_images/ans.gif")

##
# Calculator button - Shows the last saved answer
ans = tk.Button(calc, image=image, width=30, height=45, command=lambda: string_button_click(c.getMemory(c)))

# Save the image so it won't be deleted by thrash cleaner
ans.image = image

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
