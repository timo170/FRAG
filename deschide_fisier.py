import turtle
import math
from tkinter import filedialog as fd
import os
import sys
import shutil
import tempfile
import canvasvg
import cairosvg
import config 

t_desen=turtle.Turtle()
t_matrice = turtle.Turtle()
t_liste = turtle.Turtle()
t_incidenta=turtle.Turtle()


def deschide():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    filename = fd.askopenfile(title='Deschide un fisier', initialdir='/',filetypes=filetypes)
    r = 20
    config.graf = filename.readlines()
    config.poz=-1
    print(config.graf)
    tip_graf=  config.graf[0][:len(config.graf[0])-1]
    space_poz= config.graf[1].find(' ')
    nr_varfuri = int(config.graf[1][:space_poz])
    nr_perechi  = int(config.graf[1][space_poz:])
    unghi=360/nr_varfuri
    coordonate={}
    raza = 0.8*turtle.window_height() / 2
    turtle.title("Grafuri {}e".format(tip_graf))
    t_desen.reset()
    t_liste.clear()
    t_matrice.clear()
    t_incidenta.clear()
    for i in range(1,nr_varfuri+1):
        x = raza*math.sin(math.radians(i*unghi))+350
        y = raza*math.cos(math.radians(i*unghi))
        coordonate[i] = (x,y+r)
        t_desen.speed(10)
        t_desen.penup()
        t_desen.goto(x, y)
        t_desen.pendown()
        t_desen.circle(r)
        t_desen.penup()
        t_desen.backward(10)
        t_desen.pendown()
        t_desen.write(i, move=False, font=("Verdana", 25, "normal"))
    for i in range(2, nr_perechi+2):
        space_poz= config.graf[i].find(' ')
        varf1 = int(config.graf[i][:space_poz])
        if i==nr_perechi+1:
            varf2  = int(config.graf[i][space_poz:len(config.graf[i])])
        else:
            varf2  = int(config.graf[i][space_poz:len(config.graf[i])-1])
        coord_vf1 = coordonate[varf1]
        coord_vf2 = coordonate[varf2]
        t_desen.up()
        t_desen.setposition(coord_vf1)
        t_desen.down()
        t_desen.setheading(0)
        ungh=t_desen.towards(coord_vf2)
        t_desen.left(ungh)
        t_desen.up()
        t_desen.forward(r)
        t_desen.down()
        distanta=t_desen.distance(coord_vf2)-r
        t_desen.forward(distanta)
        if tip_graf == 'orientat':
            x=t_desen.xcor()
            y=t_desen.ycor()
            t_desen.backward(10)
            t_desen.left(90)
            t_desen.fd(5)
            x1=t_desen.xcor()
            y1=t_desen.ycor()
            t_desen.goto(x,y)
            t_desen.goto(x1,y1)
            t_desen.backward(10)
            t_desen.goto(x,y)
    t_desen.hideturtle()
    
def salvare_pdf():
    name = turtle.textinput("Salvare ca PDF", "Dati numele fisierului :")
    nameSav = name + ".pdf"
    tmpdir = tempfile.mkdtemp()  # create a temporary directory
    tmpfile = os.path.join(tmpdir, 'tmp.svg')  # name of file to save SVG to
    ts = turtle.getscreen().getcanvas()
    canvasvg.saveall(tmpfile, ts)
    with open(tmpfile) as svg_input, open(nameSav, 'wb') as png_output:
        cairosvg.svg2pdf(bytestring=svg_input.read(),background_color="white", write_to=png_output)
    shutil.rmtree(tmpdir)  # clean up temp file(s)
               
def exitProgram():
    sys.exit('CORECT')