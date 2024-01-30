from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk

def adiacenta():
    popup = tk.Tk()
    popup.geometry("500x200+500+70")
    popup.wm_title("Matricea de adiacență")
    title = "Reprezentarea prin matricea de adiacenta:"
    p="Matricea de adiacenţă a unui graf de ordin n este o matrice pătratică de ordin n construita astfel:"
    tk.Label(popup,text=title,fg='green',font=('Arial',18)).grid(row=0)
    tk.Label(popup,text=p,font=('Arial',15),wraplength=500,justify=tk.LEFT).grid(row=1)
    imag=ImageTk.PhotoImage(file="adiacenta.png",master=popup)
    tk.Label(master=popup,image=imag).grid(row=2) 
    ttk.Button(popup, text="Okay", command = popup.destroy).grid(row=3)
    popup.mainloop()

def lista():
    popup = tk.Tk()
    popup.geometry("500x150+500+70")
    popup.wm_title("Lista de adiacență")
    title = "Reprezentarea prin lista de adiacență                       (a vecinilor):"
    p="Pentru fiecare vârf x al grafului se memorează lista vârfurilor y adiacente cu acesta."
    tk.Label(popup,text=title,fg='green',font=('Arial',18),wraplength=500,justify=tk.LEFT).grid(row=0)
    tk.Label(popup,text=p,font=('Arial',15),wraplength=500,justify=tk.LEFT).grid(row=1)
    ttk.Button(popup, text="Okay", command = popup.destroy).grid(row=3)
    popup.mainloop()

def incidenta():
    popup = tk.Tk()
    popup.geometry("500x200+500+70")
    popup.wm_title("Matricea de incidență")
    title = "Reprezentarea prin matricea de incidență:"
    p="Matricea de incidenţă a unui graf de ordin n este o matrice de n linii și m coloane construită astfel:"
    tk.Label(popup,text=title,fg='green',font=('Arial',18)).grid(row=0)
    tk.Label(popup,text=p,font=('Arial',15),wraplength=500,justify=tk.LEFT).grid(row=1)
    imag=ImageTk.PhotoImage(file="incidenta.png",master=popup)
    tk.Label(popup,image=imag).grid(row=2) 
    ttk.Button(popup, text="Okay", command = popup.destroy).grid(row=3)
    popup.mainloop()

def grade():
    popup = tk.Tk()
    popup.geometry("500x150+500+70")
    popup.wm_title("Gradele vârfurilor")
    title = "Gradele vârfurilor se calculează astfel:"
    p="Pentru fiecare vârf x al grafului se numără lista vârfurilor y adiacente cu acesta (sau numărul de muchii incidente cu acesta)."
    tk.Label(popup,text=title,fg='green',font=('Arial',18),wraplength=500,justify=tk.LEFT).grid(row=0)
    tk.Label(popup,text=p,font=('Arial',15),wraplength=500,justify=tk.LEFT).grid(row=1)
    ttk.Button(popup, text="Okay", command = popup.destroy).grid(row=3)
    popup.mainloop()
