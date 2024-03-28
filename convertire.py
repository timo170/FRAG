import config
from tkinter import filedialog as fd

#citesc din fisier tipul grafului si apoi reprezentarea

def deschide():
    reprezentare=[]
    def verifMA(matrice): #verificare matrice de adiacenta
        nonlocal tip_graf
        if n!=m:
            return False
        for i in range(n):
            if matrice[i][i]!=0:
                return False
            for j in range(n):
                if tip_graf == "neorientat":
                    if matrice[i][j]!=matrice[j][i]: #verificam simetria matricei pt graf neorientat
                        return False
                if matrice[i][j]!=0 and matrice[i][j]!=1:
                    return False
                
        return True
    def verifMI(matrice): #verificare matrice de incidenta
        nonlocal tip_graf
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
        linie=config.graf[2][:config.graf[2].find('\n')].replace(' ','').replace('-1','2') #tratam primul rand
        matrice.append(linie)
        for i in range(3,n+1):  #tratam randurile din mijloc
            linie=config.graf[i][:config.graf[i].find('\n')].replace(' ','').replace('-1','2')
            matrice.append(linie)
        linie=config.graf[n+1].replace(' ','').replace('-1','2') #tratam ultimul rand care nu are \n la sfarsit
        matrice.append(linie)
        if tip_reprezentare!="LA":
            for i in range (len(matrice)):
                linie=list(map(int,matrice[i]))
                for x in range (len(linie)):
                    if linie[x]==2:
                        linie[x]=-1
                matrice[i]=linie
        

        m=len(matrice[0])
        if tip_reprezentare=="MA":
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
        if tip_reprezentare == "MI": #este matrice de incidenta   
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
            
        if tip_reprezentare == "LA" : #este lista de adiacenta intr-o matrice de n linii si m coloane incompleta
            reprezentare.append(tip_graf)
            reprezentare.append(tip_reprezentare)
            reprezentare.append(n)
            reprezentare.append(m)
            reprezentare.append(matrice)
            return reprezentare
            
def convertire(reprezentare): #converteste orice reprezentare intr-o lista de muchii(LM)      
    graf=[]
    print(reprezentare)
    tip_graf=reprezentare[0]
    tip_reprezentare= reprezentare[1]
    n=reprezentare[2]
    m=reprezentare[3]
    matrice=reprezentare[4]
    LM=[]
    if tip_reprezentare=='MA':
        for i in range(n):
            for j in range(n):
                if matrice[i][j]==1:
                    if tip_graf == "neorientat":
                        if i<j:
                            LM.append([i+1,j+1])
                    else:
                        LM.append([i+1,j+1])
    else:
        if tip_reprezentare=='MI':
            for j in range(m):
                muchie=[]
                for i in range(n):
                    if tip_graf=="neorientat":
                        if matrice[i][j]==1:
                            muchie.append(i+1)
                    elif tip_graf == "orientat":
                        if matrice[i][j]==1:
                            poz=i+1
                        elif matrice[i][j] == -1:
                            neg=i+1
                if tip_graf=="orientat":
                    muchie=[neg,poz]
                LM.append(muchie)
        else:
            if tip_reprezentare=='LA':
                for i in range(n):
                    muchie=[]
                    for j in range(len(matrice[i])):
                        x=i+1
                        y=matrice[i][j]
                        if tip_graf == "neorientat":
                            if [x,y] not in LM and [y,x] not in LM:
                                LM.append([x,y])
                        else: 
                            LM.append([x,y])
    graf.append(str(tip_graf)+ '\n')
    graf.append(str(n)+' '+str(len(LM))+ '\n')
    print(LM)
    for i in range(len(LM)):
        graf.append(str(LM[i][0])+' '+str(LM[i][1])+'\n')
    return graf      

def functie():
    reprezentare=deschide()
    print(reprezentare)
    if reprezentare==1:
        print("Lista de muchii. Nu modific nimic")
    elif reprezentare!=None:     
        graf=convertire(reprezentare)
        config.graf=graf
        print(graf)
    else:
        print("Ati introdus o matrice oarecare care nu coresp. vreunui graf")
