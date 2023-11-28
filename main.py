# https://realpython.com/python-use-global-variable-in-function/
# https://www.geeksforgeeks.org/how-to-pass-arguments-to-tkinter-button-command/
# https://www.geeksforgeeks.org/python-match-case-statement/
# https://www.geeksforgeeks.org/python-turtle-clear/
# https://www.guru99.com/learning-python-strings-replace-join-split-reverse.html
# https://www.geeksforgeeks.org/python-turtle-pencolor-method/
# https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python#:~:text=To%20convert%20a%20list%20to%20a%20string%2C%20use%20Python%20List,and%20return%20it%20as%20output
# https://www.eg.bucknell.edu/~hyde/Python3/TurtleDirections.html
# http://grafurisite.weebly.com/reprezentare-351i-implementare.html
# https://pythonprogramming.net/tkinter-popup-message-window/
# https://pythonguides.com/python-turtle-input/
# https://stackoverflow.com/questions/35526668/how-to-print-a-turtle-window
# https://stackoverflow.com/questions/25050156/save-turtle-output-as-jpeg
# https://cairosvg.org
# https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer
# https://www.youtube.com/watch?v=p2Lws5CyioQ
# https://www.geeksforgeeks.org/how-to-use-html-in-tkinter-python/

import tkinter as tk
import turtle
from turtle import Screen
import deschide_fisier as df
import reprezentari as rep


def program_start():
    screen = Screen()
    screen.setup(width=1.0, height=0.88, startx=0, starty=0)
    canvas = screen.getcanvas()
    meniu  = tk.Menu(canvas.master)
    fileMenu = tk.Menu(meniu)
    fileMenu.add_command(label="Deschide", command=df.deschide)
    fileMenu.add_command(label="Salvare ca PDF", command=df.salvare_pdf)
    fileMenu.add_command(label="Iesire", command=df.exitProgram)
    meniu.add_cascade(label="Fisier", menu=fileMenu)
    reprezMenu=tk.Menu(meniu)
    reprezMenu.add_command(label="Matrice adiacenta", command= lambda :rep.reprezentari('matrice') )
    reprezMenu.add_command(label="Liste adiacenta", command= lambda :rep.reprezentari('liste'))
    meniu.add_cascade(label="Reprezentari", menu=reprezMenu)
    canvas.master["menu"] = meniu
    turtle.mainloop()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    program_start()
