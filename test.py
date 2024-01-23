import pynliner
from tkinter import ttk
import tkinter as tk
from tkhtmlview import HTMLLabel
from PIL import Image,ImageTk
#https://stackoverflow.com/questions/35159861/multiple-lines-lable-in-tkinter
#https://pythonguides.com/python-tkinter-image/
popup = tk.Tk()
popup.geometry("600x700+500+70")
popup.wm_title("!")
title = "Reprezentarea prin matricea de adiacenta:"
p="Matricea de adiacenţă al unui graf de ordin n este o matrice pătratică de ordin n construita astfel:"
tk.Label(popup,text=title,fg='green',font=('Arial',20)).grid(row=0)
tk.Label(popup,text=p,font=('Arial',18),wraplength=600,justify=tk.LEFT).grid(row=1)
imag=ImageTk.PhotoImage(file="910839_orig.png")
tk.Label(popup,image=imag).grid(row=2) 
ttk.Button(popup, text="Okay", command = popup.destroy).grid(row=3)
    
popup.mainloop()