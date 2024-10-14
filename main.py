import tkinter
from tkinter import *

m = tkinter.Tk()
m.geometry("800x800") # window size


x = 4
text = tkinter.Text(height=2, width=30)
text.insert(tkinter.END, x)
text.place(x=100, y=20)

# button1 = Button(text="Click me!")
# button1.place(x=100, y=20)



m.mainloop()