from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
import os

path = "C:\\Users\ABC\PycharmProjects\grafuri\"
os.chdir(path)

drawing = svg2rlg("out.ps")
renderPM.drawToFile(drawing, "Pic.png")
