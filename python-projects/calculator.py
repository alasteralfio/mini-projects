# Calculator
# 10/6/2023

from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, borderwidth=5, width=40)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def button_ac():
    e.delete(0, END)

def button_add():
    first = e.get()
    global f_num, math 
    math = "add"

    f_num = float(first)
    e.delete(0, END)

def button_subf():
    first = e.get()
    global f_num, math 
    math = "sub"

    f_num = float(first)
    e.delete(0, END)


def button_mulf():
    first = e.get()
    global f_num, math 
    math = "mul"

    f_num = float(first)
    e.delete(0, END)


def button_divf():
    first = e.get()
    global f_num, math 
    math = "div"

    f_num = float(first)
    e.delete(0, END)


def button_equalf():
    second = e.get()
    e.delete(0, END)

    if math == "add":
        e.insert(0, f_num + float(second))
    if math == "sub":
        e.insert(0, f_num - float(second))
    if math == "mul":
        e.insert(0, f_num * float(second))
    if math == "div":
        e.insert(0, f_num / float(second))


# Define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_plus = Button(root, text="+", padx=39, pady=20, command=lambda: button_add())
button_equal = Button(root, text="=", padx=86, pady=20, command=button_equalf)
button_clear = Button(root, text="Clear", padx=77, pady=20, command=button_ac)

button_sub = Button(root, text="-", padx=40, pady=20, command=lambda: button_subf())
button_div = Button(root, text="/", padx=40, pady=20, command=lambda: button_divf())
button_mul = Button(root, text="*", padx=40, pady=20, command=lambda: button_mulf())

# Place buttons on screen
button_1.grid(row=3, column=0, sticky="nsew")
button_2.grid(row=3, column=1, sticky="nsew")
button_3.grid(row=3, column=2, sticky="nsew")

button_4.grid(row=2, column=0, sticky="nsew")
button_5.grid(row=2, column=1, sticky="nsew")
button_6.grid(row=2, column=2, sticky="nsew")

button_7.grid(row=1, column=0, sticky="nsew")
button_8.grid(row=1, column=1, sticky="nsew")
button_9.grid(row=1, column=2, sticky="nsew")

button_0.grid(row=4, column=0, sticky="nsew")
button_clear.grid(row=4, column=1, columnspan=2, sticky="nsew")

button_plus.grid(row=5, column=0, sticky="nsew")
button_equal.grid(row=5, column=1, columnspan=2, sticky="nsew")

button_sub.grid(row=6, column=0, sticky="nsew")
button_mul.grid(row=6, column=1, sticky="nsew")
button_div.grid(row=6, column=2, sticky="nsew")

root.mainloop() 