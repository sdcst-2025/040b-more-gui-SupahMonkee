import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title('tk')
window.geometry('385x80')

prinlbl = tk.Label(window, text='Principal')
intlbl = tk.Label(window, text='Interest Rate')
yearslbl = tk.Label(window, text='Years')
dashlbl = tk.Label(window, text='-')
prinent = tk.Entry(window)
intent = tk.Entry(window)
yearscom = ttk.Combobox(window)
amntlbl = tk.Label(window, text='Amount')
amntent = tk.Entry(window)


prinlbl.place(x=35,y=0)
prinent.place(x=0,y=20)
intlbl.place(x=150,y=0)
intent.place(x=120,y=20)
yearslbl.place(x=298,y=0)
yearscom.place(x=243,y=20)
dashlbl.place(x=53,y=40)
amntlbl.place(x=70,y=60)
amntent.place(x=120,y=60)

window.mainloop()
#done