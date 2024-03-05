import config
from tkinter import filedialog as fd

#citesc din fisier tipul grafului si apoi reprezentarea

def deschide():
    reprezentare=[]
    def verifMA(matrice): #verificare matrice de adiacenta
        for i in range(n):
            S=0
            if matrice[i][i]!=0:
                return False
            for j in range(n):
                if matrice[i][j]!=matrice[j][i]:
                    return False
                
                if matrice[i][j]!=0 and matrice[i][j]!=1:
                    return False
                S=S+matrice[i][j]
            if S > n-1:
                return False
        return True
    def verifMI(matrice): #verificare matrice de incidenta
        for j in range(m):
            S=0
            for i in range(n):  
                if matrice[i][j]!=0 and matrice[i][j]!=1:
                    return False
                S=S+matrice[i][j]
            if S != 2:
                return False
        return True
    '''
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    
    filename = fd.askopenfile(title='Deschide un fisier', initialdir='/',filetypes=filetypes)
    config.graf = filename.readlines()
    print(config.graf)'''
    tip_graf= config.graf[0][:len(config.graf[0])-1]
    tip_graf=tip_graf.replace(' ','')
    print(tip_graf)
    if tip_graf.isnumeric() == False:
        print("e scris sub forma listei de muchii")
        return 0
    else:
        print("e o reprezentare")
        matrice=[]
        n=len(config.graf)
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
        
        if ok==1: #pt ok=1 reprezentarea este o matrice de n linii si m coloane completa
            
            if verifMA(matrice)==True and n==m: #este matrice de adiacenta si nr. de linii este egal cu nr. de coloane
                tip='MA'
                reprezentare.append(tip)
                reprezentare.append(n)
                reprezentare.append(m)
                reprezentare.append(matrice)
                return reprezentare
            #este matrice de incidenta    
            if(verifMI(matrice)==True):
                        tip='MI'
                        reprezentare.append(tip)
                        reprezentare.append(n)
                        reprezentare.append(m)
                        reprezentare.append(matrice)
                        return reprezentare
            else:
                print("matrice oarecare")
                return
        else: #pt ok=0 reprezentarea este o matrice de n linii si m coloane incompleta
            tip='LA'
            reprezentare.append(tip)
            reprezentare.append(n)
            reprezentare.append(m)
            reprezentare.append(matrice)
            return reprezentare
            
def convertire(reprezentare): #converteste orice reprezentare intr-o lista de muchii(LM)      
    graf=[]
    tip_graf='neorientat\n'
    graf.append(tip_graf)
    tip=reprezentare[0]
    n=reprezentare[1]
    m=reprezentare[2]
    
    matrice=reprezentare[3]
    LM=[]
    if tip=='MA':
        for i in range(n):
            for j in range(n):
                if i<j and matrice[i][j]==1:
                    LM.append([i+1,j+1])
    else:
        if tip=='MI':
            for j in range(m):
                muchie=[]
                for i in range(n):
                    if matrice[i][j]==1:
                        muchie.append(i+1)
                LM.append(muchie)
        else:
            if tip=='LA':
                for i in range(n):
                    muchie=[]
                    for j in range(len(matrice[i])):
                        x=i+1
                        y=matrice[i][j]
                        if ([x,y] in LM or [y,x] in LM)==False:
                            LM.append([x,y])
    graf.append(str(n)+' '+str(len(LM))+ '\n')
    for i in range(len(LM)):
        graf.append(str(LM[i][0])+' '+str(LM[i][1])+'\n')
    return graf      

def functie():
    if deschide()!=0:
        reprezentare=deschide()
        graf=convertire(reprezentare)
        config.graf=graf
        print(graf)

