import os
import ctypes.util
path = ctypes.util.find_library('libcairo-2')
print(path)
gtkbin = r'C:\Program Files\GTK3-Runtime Win64\bin'
add_dll_dir = getattr(os, 'add_dll_directory', None)
if callable(add_dll_dir):
    add_dll_dir(gtkbin)
else:
    os.environ['PATH'] = os.pathsep.join((gtkbin, os.environ['PATH']))
import shutil
import tempfile
import turtle
import canvasvg
import cairosvg


def draw_spiral():
    turtle.fillcolor('blue')
    turtle.begin_fill()
    for i in range(20):
        d = 50 + i*i*1.5
        turtle.pencolor(0, 0.05*i, 0)
        turtle.width(i)
        turtle.forward(d)
        turtle.right(144)
    turtle.end_fill()




name = input("What would you like to name it? \n")
nameSav = name + ".png"
tmpdir = tempfile.mkdtemp()  # create a temporary directory
tmpfile = os.path.join(tmpdir, 'tmp.svg')  # name of file to save SVG to
draw_spiral()
ts = turtle.getscreen().getcanvas()
canvasvg.saveall(tmpfile, ts)
with open(tmpfile) as svg_input, open(nameSav, 'wb') as png_output:
    cairosvg.svg2png(bytestring=svg_input.read(), write_to=png_output)
shutil.rmtree(tmpdir)  # clean up temp file(s)
