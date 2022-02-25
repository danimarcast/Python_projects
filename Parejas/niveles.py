import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import font
import pygame, time, json, subprocess
from tkinter import messagebox
import hashlib as hb

global f1,f2,f3,f4,nivel1,nivel2,nivel3,v1,v2,v3,v4,count,arr1,arr2,arr3,sonidos,sound,contar,b1,b2,b3,imagenes1,imagenes2,imagenes3
count=0

s1='son_gallinas.wav'
s2='son_leones.wav'
s3='son_perros.wav'
s4='son_gatos.wav'
s5='son_patos.wav'
s6='son_vacas.wav'
s7='son_elefantes.wav'
s8='son_caballos.wav'
s9='son_osos.wav'
s10='son_pandas.wav'
s11='son_focas.wav'
s12='son_aguilas.wav'
s13='son_tigres.wav'
s14='son_monos.wav'
s15='son_loros.wav'
s16='son_conejos.wav'
s17='son_cobras.wav'
s18='son_ovejas.wav'
sonidos=[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18]

texto3=["pyimage25","pyimage26","pyimage27","pyimage28","pyimage29","pyimage30","pyimage31","pyimage32","pyimage34","pyimage35","pyimage36","pyimage37","pyimage33","pyimage38","pyimage39","pyimage40","pyimage41","pyimage42"]

v1 = Tk()
v1.geometry('460x460')
v1.title('Elegir nivel')
f1 = PhotoImage(file = 'fon_ventananiveles.png')
f2 = PhotoImage(file = 'fon_nv1.png')
f3 = PhotoImage(file = 'fon_nv2.png')
f4 = PhotoImage(file = 'fon_nv3.png')
Label(v1,image=f1).place(x=0,y=0)

def sonar(x):
    global cont
    pygame.init()
    pygame.mixer.init()

    for i in range(len(texto3)):
        if(str(x)==texto3[i]):
            sounda=pygame.mixer.Sound(sonidos[i])
            sounda.play(1)
            time.sleep (1)
            sounda.stop()

def nadita ():
    print("")
    return ()

def vn1():

    global imagenes1,arr1,arr3,arr2,matrizimagenes1,count
    v2=Toplevel()
    v2.geometry('420x160')
    v2.title('Nivel 1')
    Label(v2,image=f2).place(x=0,y=0)
    count=0
    arr1=[]
    arr2=[]
    arr3=[]
    sonidos=[]
    def cambiar(a,b):

        global count,arr1,arr2,arr3,sonidos,sound,imagenes1,matrizimagenes1

        botones[a][b].config(image=matrizimagenes1[a][b],command=sonar(matrizimagenes1[a][b]))

        arr3.append(a)
        arr3.append(b)

        count+=1
        arr1.append(matrizimagenes1[a][b])
        arr2.append(botones[a][b])
        if count==3:
            if arr1[0]==arr1[1]:
                arr1=[];arr1.append(matrizimagenes1[a][b])
                arr2=[];arr2.append(botones[a][b])
                arr3=[];arr3.append(a);arr3.append(b)
                botones[a][b].config(command=nadita)

            else:
                arr2[0].config(image=carta,command=lambda a=arr3[0],b=arr3[1]:cambiar(a,b))
                arr2[1].config(image=carta,command=lambda a=arr3[2],b=arr3[3]:cambiar(a,b))
                arr3=[]
                arr2=[]
                arr2.append(botones[a][b])
                arr3.append(a)
                arr3.append(b)
                arr1=[]

                arr1.append(matrizimagenes1[a][b])
            count=1


            #matrizsonidos=np.array(sound).reshape(4,4)
    botones=[[],[],[]]
    carta=PhotoImage(file="carta.png")
    gallinas=PhotoImage(file="gallinas.png")
    leones=PhotoImage(file="leones.png")
    perros=PhotoImage(file="perros.png")
    gatos=PhotoImage(file="gatos.png")
    patos=PhotoImage(file="patos.png")
    vacas=PhotoImage(file="vacas.png")
    elefantes=PhotoImage(file="elefantes.png")
    caballos=PhotoImage(file="caballos.png")
    imagenes1=[gallinas,gallinas,leones,leones,perros,perros,gatos,gatos]
    np.random.shuffle(imagenes1)
    matrizimagenes1=np.array(imagenes1).reshape(2,4)
    for i in range(2):
        for j in range(4):
            botones[i].append((ttk.Button(v2, padding=(1, 1),text='click',image=carta,command=lambda a=i,b=j:cambiar(a,b))))
            botones[i][j].grid(row=i, column=j)

def vn2():
    global imagenes2,arr1,arr3,arr2,matrizimagenes2,count
    v3=Toplevel()

    v3.geometry('420x340')
    v3.title('Nivel 2')
    Label(v3,image=f3).place(x=0,y=0)
    count=0
    arr1=[]
    arr2=[]
    arr3=[]
    sonidos=[]
    def cambiar(a,b):

        global count,arr1,arr2,arr3,sonidos,sound,imagenes2,matrizimagenes2

        botones[a][b].config(image=matrizimagenes2[a][b],command=sonar(matrizimagenes2[a][b]))

        arr3.append(a)
        arr3.append(b)

        count+=1
        arr1.append(matrizimagenes2[a][b])
        arr2.append(botones[a][b])
        if count==3:
            if arr1[0]==arr1[1]:
                arr1=[];arr1.append(matrizimagenes2[a][b])
                arr2=[];arr2.append(botones[a][b])
                arr3=[];arr3.append(a);arr3.append(b)
                botones[a][b].config(command=nadita)
            else:
                arr2[0].config(image=carta,command=lambda a=arr3[0],b=arr3[1]:cambiar(a,b))
                arr2[1].config(image=carta,command=lambda a=arr3[2],b=arr3[3]:cambiar(a,b))
                arr3=[]
                arr2=[]
                arr2.append(botones[a][b])
                arr3.append(a)
                arr3.append(b)
                arr1=[]

                arr1.append(matrizimagenes2[a][b])
            count=1


            #matrizsonidos=np.array(sound).reshape(4,4)
    botones=[[],[],[],[]]
    carta=PhotoImage(file="carta.png")
    gallinas=PhotoImage(file="gallinas.png")
    leones=PhotoImage(file="leones.png")
    perros=PhotoImage(file="perros.png")
    gatos=PhotoImage(file="gatos.png")
    patos=PhotoImage(file="patos.png")
    vacas=PhotoImage(file="vacas.png")
    elefantes=PhotoImage(file="elefantes.png")
    caballos=PhotoImage(file="caballos.png")
    imagenes2=[gallinas,gallinas,leones,leones,perros,perros,gatos,gatos,patos,patos,vacas,vacas,elefantes,elefantes,caballos,caballos]
    np.random.shuffle(imagenes2)
    matrizimagenes2=np.array(imagenes2).reshape(4,4)
    for i in range(4):
        for j in range(4):
            botones[i].append((ttk.Button(v3, padding=(1, 1),text='click',image=carta,command=lambda a=i,b=j:cambiar(a,b))))
            botones[i][j].grid(row=i, column=j)

def vn3():
    global imagenes2,arr1,arr3,arr2,matrizimagenes3,count

    v4=Toplevel()
    v4.geometry('630x460')
    v4.title('Nivel 3')
    Label(v4,image=f4).place(x=0,y=0)
    count=0
    arr1=[]
    arr2=[]
    arr3=[]
    sonidos=[]
    def cambiar(a,b):

        global count,arr1,arr2,arr3,sonidos,sound,imagenes3,matrizimagenes3

        botones[a][b].config(image=matrizimagenes3[a][b],command=sonar(matrizimagenes3[a][b]))

        arr3.append(a)
        arr3.append(b)

        count+=1
        arr1.append(matrizimagenes3[a][b])
        arr2.append(botones[a][b])
        if count==3:
            if arr1[0]==arr1[1]:
                arr1=[];arr1.append(matrizimagenes3[a][b])
                arr2=[];arr2.append(botones[a][b])
                arr3=[];arr3.append(a);arr3.append(b)
                botones[a][b].config(command=nadita)

            else:
                arr2[0].config(image=carta,command=lambda a=arr3[0],b=arr3[1]:cambiar(a,b))
                arr2[1].config(image=carta,command=lambda a=arr3[2],b=arr3[3]:cambiar(a,b))
                arr3=[]
                arr2=[]
                arr2.append(botones[a][b])
                arr3.append(a)
                arr3.append(b)
                arr1=[]

                arr1.append(matrizimagenes3[a][b])
            count=1


            #matrizsonidos=np.array(sound).reshape(4,4)
    botones=[[],[],[],[],[],[]]
    carta=PhotoImage(file="carta.png")
    gallinas=PhotoImage(file="gallinas.png")
    leones=PhotoImage(file="leones.png")
    perros=PhotoImage(file="perros.png")
    gatos=PhotoImage(file="gatos.png")
    patos=PhotoImage(file="patos.png")
    vacas=PhotoImage(file="vacas.png")
    elefantes=PhotoImage(file="elefantes.png")
    caballos=PhotoImage(file="caballos.png")
    tigres=PhotoImage(file="tigres.png")
    osos=PhotoImage(file="osos.png")
    pandas=PhotoImage(file="pandas.png")
    focas=PhotoImage(file="focas.png")
    aguilas=PhotoImage(file="aguilas.png")
    monos=PhotoImage(file="monos.png")
    loros=PhotoImage(file="loros.png")
    conejos=PhotoImage(file="conejos.png")
    cobras=PhotoImage(file="cobras.png")
    ovejas=PhotoImage(file="ovejas.png")

    imagenes3=[gallinas,gallinas,leones,leones,perros,perros,gatos,gatos,patos,patos,vacas,vacas,elefantes,elefantes,caballos,caballos,tigres,tigres,osos,osos,pandas,pandas,focas,focas,aguilas,aguilas,monos,monos,loros,loros,conejos,conejos,cobras,cobras,ovejas,ovejas]
    np.random.shuffle(imagenes3)
    matrizimagenes3=np.array(imagenes3).reshape(6,6)
    for i in range(6):
        for j in range(6):
            botones[i].append((ttk.Button(v4, padding=(1, 1),text='click',image=carta,command=lambda a=i,b=j:cambiar(a,b))))
            botones[i][j].grid(row=i, column=j)



carta=PhotoImage(file="carta.png")
gallinas=PhotoImage(file="gallinas.png")
leones=PhotoImage(file="leones.png")
perros=PhotoImage(file="perros.png")
gatos=PhotoImage(file="gatos.png")
patos=PhotoImage(file="patos.png")
vacas=PhotoImage(file="vacas.png")
elefantes=PhotoImage(file="elefantes.png")
caballos=PhotoImage(file="caballos.png")
tigres=PhotoImage(file="tigres.png")
osos=PhotoImage(file="osos.png")
pandas=PhotoImage(file="pandas.png")
focas=PhotoImage(file="focas.png")
aguilas=PhotoImage(file="aguilas.png")
monos=PhotoImage(file="monos.png")
loros=PhotoImage(file="loros.png")
conejos=PhotoImage(file="conejos.png")
cobras=PhotoImage(file="cobras.png")
ovejas=PhotoImage(file="ovejas.png")



imagenes1=[gallinas,gallinas,leones,leones]
imagenes2=[gallinas,gallinas,leones,leones,perros,perros,gatos,gatos]
imagenes3=[gallinas,gallinas,leones,leones,perros,perros,gatos,gatos,patos,patos,vacas,vacas,elefantes,elefantes,caballos,caballos,tigres,tigres,osos,osos,pandas,pandas,focas,focas,aguilas,aguilas,monos,monos,loros,loros,conejos,conejos,cobras,cobras,ovejas,ovejas]

v1.deiconify()
nivel1 = Button(v1,text='Nivel 1',width=10,height=6,command=vn1)
nivel1.place(x=30,y=150)
nivel2 = Button(v1,text='Nivel 2',width=10,height=6,command=vn2)
nivel2.place(x=180,y=150)
nivel3 = Button(v1,text='Nivel 3',width=10,height=6,command=vn3)
nivel3.place(x=330,y=150)


v1.mainloop()
