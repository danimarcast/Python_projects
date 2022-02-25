import tkinter as tkr
from tkinter import *
from tkinter import ttk
import hashlib as hb
import numpy as np
import pygame, time, json, subprocess
from tkinter import messagebox

global nivel,fondo_reg,main,jugando,count,im_press,bt_press,arr3carta,botones,matrizimagenes2,usuario,usuario1,clave,clave1
global vacas,perros,gallinas,leones,gatos,patos,caballos,elefantes,sonidos,texto,cont,f1,v1,cm,L1

cont=0
count=0
bt_press=[]
im_press=[]
arr3=[]
imagenes=[]
botones=[[],[],[],[]]
v={}
Principal = Tk()
Principal.geometry('500x407+50+50');Principal.resizable(0,0);Principal.title("Juego de Parejas")
ag=(141,216,202)

# Imagen de la Ventana Principal y las ventanas registro de usuario
main = PhotoImage(file='main.png')
fondo_reg = PhotoImage(file='fondo_reg.png')
fon = PhotoImage(file='jugando.png')
f1 = PhotoImage(file = 'fon_ventananiveles.png')
# Se crean las variables que contiene las imagenes de los Animales
vacas = PhotoImage(file='vacas.png')
perros = PhotoImage(file='perros.png')
gatos = PhotoImage(file='gatos.png')
patos = PhotoImage(file='patos.png')
leones = PhotoImage(file='leones.png')
caballos = PhotoImage(file='caballos.png')
gallinas = PhotoImage(file='gallinas.png')
elefantes = PhotoImage(file='elefantes.png')
carta = PhotoImage(file='carta.png')
cm=PhotoImage(file='cm_jugar.png')

def abrir_carta(a,b):
    global count,im_press,bt_press,arr3,sonidos,sound,imagenes2,matrizimagenes2,cont
    botones[a][b].config(image=matrizimagenes2[a][b])
    count+=1
    bt_press.append(botones[a][b])
    im_press.append(matrizimagenes2[a][b])
    arr3.append(a)
    arr3.append(b)
    if count==3:
        if (im_press[0]==im_press[1]):
            bt_press[0].config(image=im_press[0])
            bt_press[1].config(image=im_press[1])
            arr2=[];arr2.append(botones[a][b])

        else:
            bt_press[0].config(image=carta)
            bt_press[1].config(image=carta)


imagenes2=[gallinas,gallinas,leones,leones,perros,perros,gatos,gatos,patos,patos,vacas,vacas,elefantes,elefantes,caballos,caballos]
np.random.shuffle(imagenes2)
matrizimagenes2=np.array(imagenes2).reshape(4,4)
print(imagenes2)


for i in range(4):
     for j in range(4):
         botones[i].append((ttk.Button(Principal,padding=(1, 1),command=lambda a=i,b=j:abrir_carta(a,b),text='click',image=carta)))
         botones[i][j].grid(row=i, column=j)






Principal.mainloop()
