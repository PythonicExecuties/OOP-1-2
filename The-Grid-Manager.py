from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("280x220")

#text variable to store the data in entry field.
text = StringVar()
calculation = ""

def click(numbers): #function click with a parameter numbers
    global calculation #to access the data of multiple functions
    calculation = calculation + str(numbers) #concatenation of string
    text.set(calculation)

def clear():
    global calculation
    calculation = ""
    text.set("")

def equal():
        global calculation
        add = str(eval(calculation))
        text.set(add)
        calculation = ""



text_display = Entry(window, font=('Verdana', 24), justify='right', textvariable=text, width=13, border=8)
text_display.grid(columnspan=4)

btn7 = Button(window, text="7", font=('Verdana', 14), width=5, command=lambda:click("7"))
btn7.grid(row=1, column=0)
btn8 = Button(window, text="8", font=('Verdana', 14), width=5, command=lambda:click("8"))
btn8.grid(row=1, column=1)
btn9 = Button(window, text="9", font=('Verdana', 14), width=5, command=lambda:click("9"))
btn9.grid(row=1, column=2)
btn4 = Button(window, text="4", font=('Verdana', 14), width=5, command=lambda:click("4"))
btn4.grid(row=2, column=0)
btn5 = Button(window, text="5", font=('Verdana', 14), width=5, command=lambda:click("5"))
btn5.grid(row=2, column=1)
btn6 = Button(window, text="6", font=('Verdana', 14), width=5, command=lambda:click("6"))
btn6.grid(row=2, column=2)
btn1 = Button(window, text="1", font=('Verdana', 14), width=5, command=lambda:click("1"))
btn1.grid(row=3, column=0)
btn2 = Button(window, text="2", font=('Verdana', 14), width=5, command=lambda:click("2"))
btn2.grid(row=3, column=1)
btn3 = Button(window, text="3", font=('Verdana', 14), width=5, command=lambda:click("3"))
btn3.grid(row=3, column=2)
btn0 = Button(window, text="0", font=('Verdana', 14), width=5, command=lambda:click("0"))
btn0.grid(row=4, column=0)
btn_plus = Button(window, text="+", font=('Verdana', 14), width=5, command=lambda:click("+"))
btn_plus.grid(row=1, column=3)
btn_minus = Button(window, text="-", font=('Verdana', 14), width=5, command=lambda:click("-"))
btn_minus.grid(row=2, column=3)
btn_multiplication = Button(window, text="*", font=('Verdana', 14), width=5, command=lambda:click("*"))
btn_multiplication.grid(row=3, column=3)
btn_divide = Button(window, text="/", font=('Verdana', 14), width=5, command=lambda:click("/"))
btn_divide.grid(row=4, column=3)
btn_clear = Button(window, text="C", font=('Verdana', 14), width=5, command=clear)
btn_clear.grid(row=4, column=1)
btn_equals = Button(window, text="=", font=('Verdana', 14), width=5, command=equal)
btn_equals.grid(row=4, column=2)


window.mainloop()