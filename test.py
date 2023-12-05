from tkinter import filedialog as fd
import config

v=8
m=12
muchii=[[1,2],[2,3],[2,4],[2,5],[3,4],[3,6],[4,7],[5,8],[5,7],[1,8],[7,8],]

file=open("graf_neor_test.txt","r")

config.graf = file.readlines()
print(config.graf)
tip_graf=  config.graf[0][:len(config.graf[0])-1]
space_poz= config.graf[1].find(' ')
nr_varfuri = int(config.graf[1][:space_poz])
nr_perechi  = int(config.graf[1][space_poz:])

matrice=[]
for i in range(0,nr_varfuri+1):
    lista=[]
    for j in range(0,nr_perechi+1):
        lista.append(0)
    matrice.append(lista)


for j in range(2,nr_perechi +2):
    space_poz=config.graf[j].find(' ')
    v1=int(config.graf[j][space_poz:])
    v2=int(config.graf[j][:space_poz])
    matrice[v1][j-1]=1
    matrice[v2][j-1]=1

for i in range(1,nr_varfuri+1):
    for j in range(1,nr_perechi+1):
        print(matrice[i][j],end=" ")
    print()
