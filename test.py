
from tkinter import ttk
import tkinter as tk

from PIL import ImageTk

popup = tk.Tk()
popup.geometry("600x250+500+70")
popup.wm_title("!")
title = "Reprezentarea prin matricea de adiacenta:"
p="Matricea de adiacenţă al unui graf de ordin n este o matrice pătratică de ordin n construita astfel:"
tk.Label(popup,text=title,fg='green',font=('Arial',20)).grid(row=0)
tk.Label(popup,text=p,font=('Arial',18),wraplength=600,justify=tk.LEFT).grid(row=1)
imag=ImageTk.PhotoImage(file="adiacenta.png")
tk.Label(popup,image=imag).grid(row=2) 
ttk.Button(popup, text="Okay", command = popup.destroy).grid(row=3)
    
popup.mainloop()