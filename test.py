import pynliner
from tkinter import ttk
import tkinter as tk
from tkhtmlview import HTMLLabel
#https://www.tutorialspoint.com/python/tk_text.htm
popup = tk.Toplevel()
popup.geometry("500x500+250+70")
popup.wm_title("!")
    
    # Add label 
html = '''<style> h5,p{ color:#ffcc00;}</style>
            <b><h5 >Reprezentarea prin matricea de adiacenţă:</h5></b>
            <p>Matricea de adiacenţă al unui graf de ordin n este o matrice pătratică de ordin n,</p>
        
            <img src="910839_orig.png">
            '''
p=pynliner.Pynliner().from_string(html).run()
titlu=tk.Text(popup,str="Reprezentarea prin matricea de adiacenţă:",)    
my_label = HTMLLabel(popup, html=p)
my_label.pack(side="top", fill="x")
B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
B1.pack(side='top',anchor="center")
    
popup.mainloop()