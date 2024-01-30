import config
from tkinter import filedialog as fd

def deschide():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    filename = fd.askopenfile(title='Deschide un fisier', initialdir='/',filetypes=filetypes)
    config.graf = filename.readlines()
    tip_graf=  config.graf[0][:len(config.graf[0])-1]
    tip_graf=tip_graf.replace(' ','')
    print(tip_graf)
    if tip_graf.isnumeric() == False:
        print("e scris sub forma listei de muchii")
    else:
        print("e o reprezentare")
        matrice=[]
        linie=config.graf[0][:len(config.graf[0])-1].replace(' ','')
        m=len(linie)
        n=1
        ok=1#aici am ramas
        while True:
            linie=config.graf[n][:len(config.graf[n])-1].replace(' ','')
            n=n+1
            if len(linie)!=m:
                ok=0
            line=list(linie)
            matrice.append(line)
    
        for i in range(n):
            for j in range(m):
                print(matrice[i][j],end=" ")
            print()
        
        
            


deschide()