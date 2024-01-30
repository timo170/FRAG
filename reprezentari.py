import turtle
from tkinter import ttk
import tkinter as tk
from tkhtmlview import HTMLLabel
from deschide_fisier import t_matrice, t_liste, t_incidenta
import config


def reprezentari(type):
    poz=config.poz + 1    # determinarea poziției pe ecran
    tip_graf=  config.graf[0][:len(config.graf[0])-1]
    space_poz= config.graf[1].find(' ')
    nr_varfuri = int(config.graf[1][:space_poz])
    nr_perechi  = int(config.graf[1][space_poz:])
    DY= turtle.window_height() / 2 - 10 -(nr_varfuri-2) * 30 * poz
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
        dx=10-turtle.window_width() / 2
        dy=DY- 15 - nr_varfuri*10
        t_matrice.penup()
        t_matrice.goto(dx,dy)
        t_matrice.pendown()
        t_matrice.write('A=', font=("Verdana",20, "normal"))
        dx=50-turtle.window_width() / 2
        dy=DY
        t_matrice.penup()
        t_matrice.goto(dx,dy)
        t_matrice.pendown()
        t_matrice.goto(dx,dy - nr_varfuri*20 + 10)
        for i in range(nr_varfuri):
            dx=55-turtle.window_width() / 2
            dy=DY -15 - i*20
            t_matrice.penup()
            t_matrice.goto(dx,dy)
            t_matrice.pendown()
            t_matrice.write(afisare[i], font=("Verdana",12, "normal"))
        dx=50-turtle.window_width() / 2 + 20*(nr_varfuri - 1 )
        dy=DY
        t_matrice.penup()
        t_matrice.goto(dx,dy)
        t_matrice.pendown()
        t_matrice.goto(dx,dy - nr_varfuri*20 + 10)

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
        dy=DY - 15 - 60
        t_liste.penup()
        t_liste.goto(dx,dy)
        t_liste.pendown()
        t_liste.write('L=', font=("Verdana",20, "normal"))
        dx=55 - turtle.window_width() / 2
        for i in range(1,nr_varfuri+1):
            dy = DY - 15 - (i-1)*20
            t_liste.penup()
            t_liste.goto(dx,dy)
            t_liste.pendown()
            t_liste.write(i, font=("Verdana",12, "normal"))
        dx=70-turtle.window_width() / 2 
        dy=DY
        t_liste.penup()
        t_liste.goto(dx,dy)
        t_liste.pendown()
        t_liste.goto(dx,dy - nr_varfuri*20 +10 )
        afisare = []
        for i in range(1,nr_varfuri+1):
            linie = ' '.join(str(e) for e in lista_ad[i])
            afisare.append(linie)
        for i in range(nr_varfuri):
            dx=75-turtle.window_width() / 2
            dy = DY - 15  - i*20
            t_liste.penup()
            t_liste.goto(dx,dy)
            t_liste.pendown()
            t_liste.write(afisare[i], font=("Verdana",12, "normal"))

    if type=="incidenta": 
        dx=10-turtle.window_width() / 2
        dy=DY- 15 + nr_varfuri*5 -120
        t_incidenta.penup()
        t_incidenta.goto(dx,dy)
        t_incidenta.pendown()
        t_incidenta.write('I=', font=("Verdana",20, "normal"))
        dx=50 -turtle.window_width() / 2 
        dy=DY
        t_incidenta.penup()
        t_incidenta.goto(dx,dy)
        t_incidenta.pendown()
        t_incidenta.goto(dx,dy - nr_varfuri*20 +10)
        
        matrice=[]
        for i in range(0,nr_varfuri+1):
            lista=[]
            for j in range(0,nr_perechi+1):
                lista.append(0)
            matrice.append(lista)
        if tip_graf=="neorientat":
            for j in range(2,nr_perechi +2):
                space_poz=config.graf[j].find(' ')
                v1=int(config.graf[j][:space_poz])
                v2=int(config.graf[j][space_poz:])
                matrice[v1][j-1]=1
                matrice[v2][j-1]=1
        else:
            for j in range(2,nr_perechi +2):
                space_poz=config.graf[j].find(' ')
                v1=int(config.graf[j][:space_poz])
                v2=int(config.graf[j][space_poz:])
                matrice[v1][j-1]=-1
                matrice[v2][j-1]=1

        lungime_linie=0
        afisare = []
        for i in range(0,nr_varfuri+1):
            linie=''
            for j in range(1,nr_perechi+1):
                e=matrice[i][j]
                if e==-1:
                    linie=linie+str(e)+' '
                else:
                    linie=linie+' '+str(e)+' '
            
            if len(linie)>lungime_linie:
                lungime_linie=len(linie)

            afisare.append(linie)
        for i in range(1,nr_varfuri+1):
            dx=55-turtle.window_width() / 2
            dy = DY- 15 - (i-1)*20
            t_incidenta.penup()
            t_incidenta.goto(dx,dy)
            t_incidenta.pendown()
            t_incidenta.write(afisare[i], font=("Verdana",12, "normal"))
        dx=55 -turtle.window_width() / 2 + 24*(nr_perechi-1)
        dy=DY
        t_incidenta.penup()
        t_incidenta.goto(dx,dy)
        t_incidenta.pendown()
        t_incidenta.goto(dx,dy - nr_varfuri*20 + 10)

    if type=="grade":
        dx=55-turtle.window_width() / 2 
        dy=DY
        t_liste.penup()
        t_liste.goto(dx,dy)
        t_liste.pendown()
        t_liste.goto(dx,dy - nr_varfuri*20 +10 )
        
        grade=[]
        grade = [[0,0] for i in range(nr_varfuri+1)]
        if tip_graf=="neorientat":
            for j in range(2,nr_perechi +2):
                space_poz=config.graf[j].find(' ')
                v1=int(config.graf[j][:space_poz])
                v2=int(config.graf[j][space_poz:])
                grade[v1][0]=grade[v1][0]+1
                grade[v2][1]=grade[v2][1]+1
        else:
            for j in range(2,nr_perechi +2):
                space_poz=config.graf[j].find(' ')
                v1=int(config.graf[j][:space_poz])
                v2=int(config.graf[j][space_poz:])
                grade[v1][0]=grade[v1][0]+1
                grade[v2][1]=grade[v2][1]+1
        print(grade)

        for i in range(1,nr_varfuri+1):
            dx=65-turtle.window_width() / 2
            dy = DY- 15- (i-1)*20
            t_liste.penup()
            t_liste.goto(dx,dy)
            t_liste.pendown()
            if tip_graf=="neorientat":
                t_liste.write("d("+str(i)+") = "+str(grade[i][0]+grade[i][1]), font=("Verdana",12, "normal"))
            else:
                t_liste.write("d\u207A("+str(i)+") = "+str(grade[i][0])+" , "+"d\u207B("+str(i)+") = "+str(grade[i][1]) , font=("Verdana",12, "normal"))
        

        
            
            