from tkinter import *
from tkinter import ttk

# Create a GUI window
window = Tk()
window.title("Unit Converter")
window.geometry("500x500")
window.configure(bg='skyblue')

#Method
def length_conversion():
    if inn.get() != int() or float():
        out.delete("0", END)
        out.insert(END,"Error!Input a number.")
    #Convert from Entry Unit to a Base Unit. Base unit will be meters(bu)
    if var1.get() == "Meters":
        bu = float(inn.get())

    elif var1.get() == "Centimeters":
        bu = float(inn.get())/100

    elif var1.get() == "Kilometers":
        bu = float(inn.get())*1000

    elif var1.get() == "Millimeters":
        bu = float(inn.get())/1000

    elif var1.get() == "Inches":
        bu = float(inn.get())/39.3701

    elif var1.get() == "Miles":
        bu = float(inn.get())*1609.34

    elif var1.get() == "Yards":
        bu = float(inn.get())/1.09361

    elif var1.get() == "Feet":
        bu = float(inn.get())/3.281

    #Convert Base unit to desired unit.
    if var2.get() == "Meters":
        ans = bu

    elif var2.get() == "Centimeters":
        ans = bu*100

    elif var2.get() == "Kilometers":
        ans = bu/1000

    elif var2.get() == "Millimeters":
        ans = bu*1000

    elif var2.get() == "Inches":
        ans = bu*39.3701

    elif var2.get() == "Miles":
        ans = bu/1609.34

    elif var2.get() == "Yards":
        ans = bu*1.09361

    elif var2.get() == "Feet":
        ans = bu*3.281

    out.delete("0",END)
    out.insert(END,ans)

#For weight base unit will be grams.
def weight_conversion():
    if inn1.get() != int() or float():
        out1.delete("0", END)
        out1.insert(END,"Error!Input a number.")
    #Entry to Base Unit
    if var3.get() == "Grams":
        bu = float(inn1.get())

    elif var3.get() == "Kilograms":
        bu = float(inn1.get())*1000

    elif var3.get() == "Ounce":
        bu = float(inn1.get())*28.3495

    elif var3.get() == "Pounds":
        bu = float(inn1.get())*453.592

    #Base unit to desired unit
    if var4.get() == "Grams":
        ans = bu

    elif var4.get() == "Kilograms":
        ans = bu/1000

    elif var4.get() == "Ounce":
        ans = bu/28.3495

    elif var4.get() == "Pounds":
        ans = bu/453.592

    out1.delete("0", END)
    out1.insert(END, ans)

#For Temps

def temp_conversion():
    if inn2.get() != int() or float():
        out2.delete("0", END)
        out2.insert(END,"Error!Input a number.")
    #Entry to Base Unit. Celsius will be the base unit
    if var5.get() == "Celsius":
        bu = float(inn2.get())

    elif var5.get() == "Fahrenheit":
        bu = (float(inn2.get())-32)*(5/9)

    elif var5.get() == "Kelvin":
        bu = float(inn2.get())-273.15

    #Base unit to desired unit
    if var6.get() == "Celsius":
        ans = bu, "°C"

    elif var6.get() == "Fahrenheit":
        ans = bu*(9/5)+32, "°F"

    elif var6.get() == "Kelvin":
        ans = bu+273.15, "K"

    out2.delete("0", END)
    out2.insert(END, ans)

# Create a tab
nb = ttk.Notebook(window)
tab1 = Frame(nb, bg="skyblue", padx=2)
tab2 = Frame(nb, bg="skyblue", padx=2)
tab3 = Frame(nb, bg="skyblue", padx=2)
nb.add(tab1, text="Length Converter")
nb.add(tab2, text="Weight Converter")
nb.add(tab3, text="Temperature Converter")
nb.pack(fill="both", expand=1)

#Create a unit list
options1 = [
    "Meters",
    "Centimeters",
    "Kilometers",
    "Millimeters",
    "Inches",
    "Feet",
    "Miles",
    "Yards",
]
options2 = [
    "Grams",
    "Kilograms",
    "Pounds",
    "Ounce"
]
options3 = [
    "Celsius",
    "Fahrenheit",
    "Kelvin"
]
#//////////////////////////////////////////////////////////////////////////////////////////
#Create a frame for input unit
CU= LabelFrame(tab1, text = "From", font=('Verdana', 20)) #CU = Current unit
CU.pack(pady = 20)

inn = Entry(CU,font=("verdana", 16)) # in = entry number
inn.grid(row=1, column=0)

var1 = StringVar()
var1.set(options1[0])
ud1 = OptionMenu(CU, var1, *options1)
ud1.config(anchor=W,font=("verdana", 16), width= 10)
ud1.grid(row=1, column=1, pady=10)


#Creat a frame for output unit
CoU = LabelFrame(tab1, text= "To", font=("verdana", 20)) #CoU = converted unit
CoU.pack(pady=20)

out = Entry(CoU,font=("verdana", 16), bg="#f0f0f0")
out.grid(row=1, column=0)

var2 = StringVar()
var2.set(options1[1])
ud2 = OptionMenu(CoU, var2, *options1)
ud2.config(anchor=W,font=("verdana", 16), width= 10)
ud2.grid(row=1, column=1, pady= 10)

#Convert Button
CB = Button(tab1, text="Convert", command=length_conversion, font=('verdana', 20))
CB.place(anchor="center", relx=.5, y=350)
#/////////////////////////////////////////////////////////////////////////////////////////////////
#Weight Converter Tab
#/////////////////////////////////////////////////////////////////////////////////////////////////
CU= LabelFrame(tab2, text = "From", font=('Verdana', 20)) #CU = Current unit
CU.pack(pady = 20)

inn1 = Entry(CU,font=("verdana", 16)) # in = entry number
inn1.grid(row=1, column=0)

var3 = StringVar()
var3.set(options2[0])
ud1 = OptionMenu(CU, var3, *options2)
ud1.config(anchor=W,font=("verdana", 16), width= 10)
ud1.grid(row=1, column=1, pady=10)


#Creat a frame for output unit
CoU = LabelFrame(tab2, text= "To", font=("verdana", 20)) #CoU = converted unit
CoU.pack(pady=20)

out1 = Entry(CoU,font=("verdana", 16), bg="#f0f0f0")
out1.grid(row=1, column=0)

var4 = StringVar()
var4.set(options2[1])
ud2 = OptionMenu(CoU, var4, *options2)
ud2.config(anchor=W,font=("verdana", 16), width= 10)
ud2.grid(row=1, column=1, pady= 10)

CB = Button(tab2, text="Convert", command=weight_conversion, font=('verdana', 20))
CB.place(anchor="center", relx=.5, y=350)
#///////////////////////////////////////////////////////////////////////////
#Temperature
#/////////////////////////////////////////////////////////////////////////////
CU= LabelFrame(tab3, text = "From", font=('Verdana', 20)) #CU = Current unit
CU.pack(pady = 20)

inn2 = Entry(CU, font=("verdana", 16)) # in = entry number
inn2.grid(row=1, column=0)

var5 = StringVar()
var5.set(options3[0])
ud1 = OptionMenu(CU, var5, *options3)
ud1.config(anchor=W,font=("verdana", 16), width= 10)
ud1.grid(row=1, column=1, pady=10)


#Creat a frame for output unit
CoU = LabelFrame(tab3, text= "To", font=("verdana", 20)) #CoU = converted unit
CoU.pack(pady=20)

out2 = Entry(CoU,font=("verdana", 16), bg="#f0f0f0")
out2.grid(row=1, column=0)

var6 = StringVar()
var6.set(options3[1])
ud2 = OptionMenu(CoU, var6, *options3)
ud2.config(anchor=W,font=("verdana", 16), width= 10)
ud2.grid(row=1, column=1, pady= 10)

CB = Button(tab3, text="Convert", command=temp_conversion, font=('verdana', 20))
CB.place(anchor="center", relx=.5, y=350)

window.mainloop()