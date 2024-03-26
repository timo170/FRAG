import config
from tkinter import filedialog as fd

#citesc din fisier tipul grafului si apoi reprezentarea

def deschide():
    reprezentare=[]
    def verifMA(matrice): #verificare matrice de adiacenta
        global tip_graf
        if n!=m:
            return False
        for i in range(n):
            if matrice[i][i]!=0:
                return False
            for j in range(n):
                if tip_graf=="neorientat":
                    if matrice[i][j]!=matrice[j][i]: #verificam simetria matricei pt graf neorientat
                        return False
                if matrice[i][j]!=0 and matrice[i][j]!=1:
                    return False
                
        return True
    def verifMI(matrice): #verificare matrice de incidenta
        global tip_graf
        for j in range(m):
            val_poz=0
            val_neg=0
            for i in range(n):  
                if matrice[i][j]!=0 and matrice[i][j]!=1 and matrice[i][j]!=-1:
                    return False
                if matrice[i][j]==1:
                    val_poz=val_poz+1
                elif matrice[i][j]==-1:
                    val_neg=val_neg+1
            if tip_graf == "neorientat":
                if val_poz!=2:
                    return False
            elif tip_graf == "orientat":
                if val_poz!=1 or val_neg!=1:
                    return False
        return True
    
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    
    filename = fd.askopenfile(title='Deschide un fisier', initialdir='/',filetypes=filetypes)
    config.graf = filename.readlines()
    print(config.graf)
    tip_graf= config.graf[0][:len(config.graf[0])-1]
    tip_reprezentare=config.graf[1][:len(config.graf[1])-1]
    tip_reprezentare=tip_reprezentare.replace(' ','')
    print(tip_graf,tip_reprezentare)
    if tip_reprezentare.isnumeric() == True:
        print("e scris sub forma listei de muchii")
        return 1
    else:
        print(tip_reprezentare)
        reprezentare=[]
        matrice=[] #citim matricea
        n=len(config.graf)-2 #nr de linii ale matricei
        print(n)
        linie=config.graf[2][:config.graf[2].find('\n')].replace(' ','') #tratam primul rand
        linie=list(map(int,linie))
        matrice.append(linie)
        ok=1
        for i in range(3,n+1):  #tratam randurile din mijloc
            linie=config.graf[i][:config.graf[i].find('\n')].replace(' ','')
            linie=list(map(int,linie))
            matrice.append(linie)
        linie=config.graf[n+1].replace(' ','') #tratam ultimul rand care nu are \n la sfarsit
        linie=list(map(int,linie))
        matrice.append(linie)
        m=len(matrice[0])
        if tip_reprezentare=="MA" and ok==1:
            if verifMA(matrice)==True: #este matrice de adiacenta si nr. de linii este egal cu nr. de coloane
                reprezentare.append(tip_graf)
                reprezentare.append(tip_reprezentare)
                reprezentare.append(n)
                reprezentare.append(m)   
                reprezentare.append(matrice)
                return reprezentare
            else:
                print("matrice oarecare")
                return
        if tip_reprezentare == "MI" and ok==1: #este matrice de incidenta    
            if verifMI(matrice)==True :
                reprezentare.append(tip_graf)
                reprezentare.append(tip_reprezentare)
                reprezentare.append(n)
                reprezentare.append(m)
                reprezentare.append(matrice)
                return reprezentare
            else:
                print("matrice oarecare")
                return
            
        if tip_reprezentare == "LA" and ok==0 : #este lista de adiacenta intr-o matrice de n linii si m coloane incompleta
            reprezentare.append(tip_graf)
            reprezentare.append(tip_reprezentare)
            reprezentare.append(n)
            reprezentare.append(m)
            reprezentare.append(matrice)
            return reprezentare
            
def convertire(reprezentare): #converteste orice reprezentare intr-o lista de muchii(LM)      
    graf=[]
    tip_graf=reprezentare[0]
    tip_reprezentare= reprezentare[1]
    n=reprezentare[2]
    m=reprezentare[3]
    matrice=reprezentare[4]
    LM=[]
    if tip_reprezentare=='MA':
        for i in range(n):
            for j in range(n):
                if i<j and matrice[i][j]==1:
                    LM.append([i+1,j+1])
    else:
        if tip_reprezentare=='MI':
            
            for j in range(m):
                muchie=[]
                for i in range(n):
                    if tip_graf=='"neorientat':
                        if matrice[i][j]==1:
                            muchie.append(i+1)
                    elif tip_graf == "orientat":
                        if matrice[i][j]==1:
                            poz=i+1
                        elif matrice[i][j] == -1:
                            neg=i+1
                if tip_graf=="orientat":
                    muchie.append(poz,neg)
                LM.append(muchie)
        else:
            if tip_reprezentare=='LA':
                for i in range(n):
                    muchie=[]
                    for j in range(len(matrice[i])):
                        x=i+1
                        y=matrice[i][j]
                        if tip_graf == "neorientat" and ([x,y] in LM or [y,x] in LM)==False:
                            LM.append([x,y])
                        else: 
                            LM.append([x,y])
    graf.append(str(tip_graf)+ '\n')
    graf.append(str(n)+' '+str(len(LM))+ '\n')
    for i in range(len(LM)):
        graf.append(str(LM[i][0])+' '+str(LM[i][1])+'\n')
    return graf      

def functie():
    reprezentare=deschide()
    if reprezentare!=0:
        graf=convertire(reprezentare)
        config.graf=graf
        print(graf)

functie()