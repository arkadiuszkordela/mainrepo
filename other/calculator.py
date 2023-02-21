from tkinter import *

root = Tk()
root.title("Calculator")

resultField = Entry(root, width = 35, borderwidth = 5)
resultField.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def button_num(number):
    current = resultField.get()
    resultField.delete(0, END)
    resultField.insert(0, str(current) + str(number))

def button_plus():
    first_number = resultField.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    resultField.delete(0, END)

def button_minus():
    first_number = resultField.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    resultField.delete(0, END)

def button_multi():
    first_number = resultField.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    resultField.delete(0, END)

def button_div():
    first_number = resultField.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    resultField.delete(0, END)

def button_eq():
    second_number = resultField.get()
    resultField.delete(0, END)

    if math == "addition": 
        resultField.insert(0, f_num + int(second_number))

    if math == "subtraction": 
        resultField.insert(0, f_num - int(second_number))

    if math == "multiplication": 
        resultField.insert(0, f_num * int(second_number))

    if math == "division": 
        resultField.insert(0, f_num / int(second_number))

def button_clear():
    resultField.delete(0, END)

button1 = Button(root, text = "1", padx = 30, pady = 20, command = lambda: button_num(1))
button2 = Button(root, text = "2", padx = 30, pady = 20, command = lambda: button_num(2))
button3 = Button(root, text = "3", padx = 30, pady = 20, command = lambda: button_num(3))
button4 = Button(root, text = "4", padx = 30, pady = 20, command = lambda: button_num(4))
button5 = Button(root, text = "5", padx = 30, pady = 20, command = lambda: button_num(5))
button6 = Button(root, text = "6", padx = 30, pady = 20, command = lambda: button_num(6))
button7 = Button(root, text = "7", padx = 30, pady = 20, command = lambda: button_num(7))
button8 = Button(root, text = "8", padx = 30, pady = 20, command = lambda: button_num(8))
button9 = Button(root, text = "9", padx = 30, pady = 20, command = lambda: button_num(9))
button0 = Button(root, text = "0", padx = 30, pady = 20, command = lambda: button_num(0))
buttonPlus = Button(root, text = "+", padx = 29, pady = 19, command = button_plus)
buttonMinus = Button(root, text = "-", padx = 31, pady = 19, command = button_minus)
buttonMulti = Button(root, text = "*", padx = 31, pady = 19, command = button_multi)
buttonDiv = Button(root, text = "/", padx = 31, pady = 19, command = button_div)
buttonEq = Button(root, text = "=", padx = 29, pady = 19, command = button_eq)
buttonClear = Button(root, text = "Clear", padx = 100, pady = 20, command = button_clear)

button1.grid(row = 3, column = 0)
button2.grid(row = 3, column = 1)
button3.grid(row = 3, column = 2)
button4.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button6.grid(row = 2, column = 2)
button7.grid(row = 1, column = 0)
button8.grid(row = 1, column = 1)
button9.grid(row = 1, column = 2)
button0.grid(row = 4, column = 0)
buttonPlus.grid(row = 4, column = 1)
buttonMinus.grid(row = 4, column = 2)
buttonMulti.grid(row = 5, column = 1)
buttonDiv.grid(row = 5, column = 2)
buttonEq.grid(row = 5, column = 0)
buttonClear.grid(row = 6, column = 0, columnspan = 3)

root.mainloop()
