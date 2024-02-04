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
        n=len(config.graf)
        print(n)

        linie=config.graf[0][:config.graf[0].find('\n')].replace(' ','') #tratam primul rand
        line=list(linie)
        matrice.append(line)
        ok=1
        for i in range(1,n-1):  #tratam randurile din mijloc
            linie=config.graf[i][:config.graf[i].find('\n')].replace(' ','')
            line=list(linie)
            matrice.append(line)
        linie=config.graf[n-1].replace(' ','') #tratam ultimul rand care nu are \n la sfarsit
        line=list(linie)
        matrice.append(line)
        m=len(matrice[0])    
        for i in range(n):
            matrice[i]=list(map(int,matrice[i])) #convertesc toate elementele matricei din str in int
            if len(matrice[i])>m:
                m=len(matrice[i])
                ok=0
            for j in range(len(matrice[i])):
                print(matrice[i][j],end=" ")
            print()
        
        if ok==1:
            print('este matrice')
            if n == m:
                print('posibil matrice de adiacenta')
                k=1
                for i in range(n):
                    S=0
                    if matrice[i][i]!=0:
                        k=0
                        break
                    for j in range(n):
                        if matrice[i][j]!=matrice[j][i]:
                            k=0
                            break
                        
                        if matrice[i][j]!=0 and matrice[i][j]!=1:
                            k=0
                            break
                        S=S+matrice[i][j]
                    if S > n-1:
                        k=0
                        break

                if k==1:
                    print("este matrice de adiacenta")
                else:
                    print("nu este matrice de adiacenta")
                
            else:
                print("posibil matrice de incidenta")
        else:
            print('lista de adiacenta')
            print(n,m,ok)
        
            


deschide()