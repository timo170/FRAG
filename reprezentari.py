import turtle
from tkinter import ttk
import tkinter as tk
from tkhtmlview import HTMLLabel
from deschide_fisier import t_matrice, t_liste
import config

def popupmsg_adiacenta():
    popup = tk.Tk()
    popup.wm_title("!")
    msg='adia'
    # Add label
    my_label = HTMLLabel(popup, html="""
            <b><h1>Reprezentarea prin matricea de adiacenţă:</h1></b>
            <p>Matricea de adiacenţă al unui graf de ordin n este o matrice pătratică de ordin n,</p>
            <img src="910839_orig.png">
            <ul>
                <li><a href='https://www.geeksforgeeks.org/python-programming-language/'>Python</a></li>
                <li><a href='https://www.geeksforgeeks.org/c-plus-plus/'>C++</a></li>
                <li><a href='https://www.geeksforgeeks.org/java/'>Java</a></li>
            </ul>
        """)
    # label = ttk.Label(popup, text=msg, font=("Verdana",10, "normal"))
    my_label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
    
def popupmsg_liste():
    popup = tk.Tk()
    popup.wm_title("!")
    msg='liste'
    label = ttk.Label(popup, text=msg, font=("Verdana",10, "normal"))
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
    
def reprezentari(type):
    tip_graf=  config.graf[0][:len(config.graf[0])-1]
    space_poz= config.graf[1].find(' ')
    nr_varfuri = int(config.graf[1][:space_poz])
    nr_perechi  = int(config.graf[1][space_poz:])
    if type == 'matrice':
        matrice = []
        for i in range(nr_varfuri+1):
            linie = [0 for _ in range(nr_varfuri+1)]
            matrice.append(linie)
        for i in range(2, nr_perechi+2):
            space_poz= config.graf[i].find(' ')
            varf1 = int(config.graf[i][:space_poz])
            if i==nr_perechi+1:
                varf2  = int(config.graf[i][space_poz:len(config.graf[i])])
            else:
                varf2  = int(config.graf[i][space_poz:len(config.graf[i])-1])
            matrice[varf1][varf2] = 1
            if tip_graf == "neorientat":
                matrice[varf2][varf1]  = 1
        afisare = []
        for i in range(1,nr_varfuri+1):
            linie = ' '.join(str(e) for e in matrice[i])
            afisare.append(linie[1:])
        
        print(turtle.window_width(),turtle.window_height())

        dx=10-turtle.window_width() / 2
        print(dx)
        dy=turtle.window_height() / 2-25 - nr_varfuri*10
        print(dy)
        t_matrice.penup()
        t_matrice.goto(dx,dy)
        t_matrice.pendown()
        t_matrice.write('A=', font=("Verdana",20, "normal"))
        dx=50-turtle.window_width() / 2
        dy=turtle.window_height() / 2 - 10
        t_matrice.penup()
        t_matrice.goto(dx,dy)
        t_matrice.pendown()
        t_matrice.goto(dx,dy - nr_varfuri*20 + 10)
        for i in range(nr_varfuri):
            dx=55-turtle.window_width() / 2
            dy=turtle.window_height() / 2-25 - i*20
            t_matrice.penup()
            t_matrice.goto(dx,dy)
            t_matrice.pendown()
            t_matrice.write(afisare[i], font=("Verdana",12, "normal"))
        dx=50-turtle.window_width() / 2 + 20*(nr_varfuri - 1 )
        dy=turtle.window_height() / 2 - 10
        t_matrice.penup()
        t_matrice.goto(dx,dy)
        t_matrice.pendown()
        t_matrice.goto(dx,dy - nr_varfuri*20 + 10)
        popupmsg_adiacenta()
    if type == 'liste':
        lista_ad = [[] for i in range(nr_varfuri+1)]
        for i in range(2, nr_perechi+2):
            space_poz= config.graf[i].find(' ')
            varf1 = int(config.graf[i][:space_poz])
            if i==nr_perechi+1:
                varf2  = int(config.graf[i][space_poz:len(config.graf[i])])
            else:
                varf2  = int(config.graf[i][space_poz:len(config.graf[i])-1])
            lista_ad[varf1].append(varf2)
            if tip_graf == "neorientat":
                lista_ad[varf2].append(varf1)
        print(lista_ad)
        dx=10-turtle.window_width() / 2
        dy=turtle.window_height() / 2-25 - nr_varfuri*30
        t_liste.penup()
        t_liste.goto(dx,dy)
        t_liste.pendown()
        t_liste.write('L=', font=("Verdana",20, "normal"))
        dx=55 - turtle.window_width() / 2
        for i in range(1,nr_varfuri+1):
            dy = turtle.window_height() / 2-25 - nr_varfuri*20 - i*20
            t_liste.penup()
            t_liste.goto(dx,dy)
            t_liste.pendown()
            t_liste.write(i, font=("Verdana",12, "normal"))
        dx=70-turtle.window_width() / 2 
        dy=turtle.window_height() / 2 - 25 - nr_varfuri*20
        t_liste.penup()
        t_liste.goto(dx,dy)
        t_liste.pendown()
        t_liste.goto(dx,dy - nr_varfuri*20 )
        afisare = []
        for i in range(1,nr_varfuri+1):
            linie = ' '.join(str(e) for e in lista_ad[i])
            afisare.append(linie)
        for i in range(nr_varfuri):
            dx=75-turtle.window_width() / 2
            dy=turtle.window_height() / 2-45 - nr_varfuri*20 - i*20
            t_liste.penup()
            t_liste.goto(dx,dy)
            t_liste.pendown()
            t_liste.write(afisare[i], font=("Verdana",12, "normal"))
        popupmsg_liste()

        if type=="incidenta":
            matrice=[]
            for i in range(0,nr_varfuri+1):
                lista=[]
                for j in range(0,nr_perechi+1):
                    lista.append(0)
                matrice.append(lista)

            for j in range(2,nr_perechi +1):
                space_poz=config.graf[j].find(' ')
                v1=int(config.graf[j][space_poz:])
                v2=int(config.graf[j][:space_poz])
                matrice[v1][j-1]=1
                matrice[v2][j-1]=1

            for i in range(1,nr_varfuri+1):
                for j in range(1,nr_perechi+1):
                    print(matrice[i][j],end=" ")
                print()