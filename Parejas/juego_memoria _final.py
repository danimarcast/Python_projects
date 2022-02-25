import tkinter as tkr
from tkinter import *
from tkinter import ttk
import hashlib as hb
import numpy as np
import pygame, time, json, subprocess
from tkinter import messagebox
import time as tm


global nivel,fondo_reg,main,jugando,count,arr1,arr2,arr3carta,botones,matrizimagenes,usuario,usuario1,clave,clave1
global vacas,perros,gallinas,leones,gatos,patos,caballos,elefantes,sonidos,texto,cont,f1,v1,cm,L1,tiempo1,tiempo,tf,ll2,b22,H,final
final=0
cont=0
count=0
arr1=[]
arr2=[]
arr3=[]
best_time=[]
imagenes=[]
botones=[[],[],[],[]]
v={}
Principal = Tk()
Principal.geometry('307x407+50+50');Principal.resizable(0,0);Principal.title("Juego de Parejas")
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
carta = PhotoImage(file='carta.png')
elefantes = PhotoImage(file='elefantes.png')
cm=PhotoImage(file='cm_jugar.png')

# Sonidos de Animales , se crean las variables que contienen las rutas de los sonidos y
# y se crea el vector sonidos con las variables anterior mencionadas
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
#Creacion del arreglo imagenes el cual contiene la creacion de las imagenes que se pondran i
#como imagen de los botones
#Creacion del arreglo texto el contiene los valores retornados al presionar los botones
imagenes=[gallinas,gallinas,leones,leones,perros,perros,gatos,gatos,patos,patos,vacas,vacas,elefantes,elefantes,caballos,caballos]
texto=["pyimage17","pyimage18","pyimage19","pyimage20","pyimage21","pyimage22","pyimage23","pyimage24","pyimage26","pyimage27","pyimage28","pyimage29","pyimage25","pyimage30","pyimage31","pyimage32","pyimage33","pyimage34"]


Label(Principal,image=main).place(x=0,y=0)

usuario = Entry(Principal,background="#DAFFFB")
usuario.place(x=90,y=80)

clave = Entry(Principal, show="*",background="#DAFFFB")
clave.place(x=90,y=130)
cont=0


        # Se define la funcion sonar la cual permitira insertar el sonido al boton que es presionado
        #sonar recibe como parametro un string y valida si dicho valor es igual a alguno de los estan
        #dentro del arreglo texto,en caso de ser iguales reproduce el sonido asociado a dicho string
def sonar(x):
    global cont
    pygame.init()
    pygame.mixer.init()
    for i in range(len(texto)):
        if(str(x)==texto[i]):
            sounda=pygame.mixer.Sound(sonidos[i])
            sounda.play(1)
            time.sleep (1)
            sounda.stop()

    # if(cont==8):
    #     messagebox.showerror("Juego terminado","Ganaste!")
    #     exit()

        #Se define la funcion inicio la cual correra el juego luego de validar los datos del usuario
        #dentro de la funcion inicio se define la funcion cambiar la cual validara si cada par de
        #botones presionados tienen la misma imagen de ser asi deja fija las imagenes de lo contrario
        #volvera a tapar las imagenes
def nada():
    print("hola")
    # pass
def reinicio():
    v[usuario.get()]["nivel1"]=0
    v[usuario.get()]["nivel2"]=0
    v[usuario.get()]["nivel3"]=0
    nivel1.config(state=NORMAL)
    nivel2.config(state=NORMAL)
    nivel3.config(state=NORMAL)
def inicio():
    global f1,nivel1,nivel2,nivel3,cont,L1,v1,tiempo1,tiempo,ll2
    Principal.withdraw()

            # Se realiza la validacion de usuario y contrasena de la persona que desea jugar
            # si la persona esta registrada en el diccionario del json puede empezar a jugar
            # de lo contrario debe registrarse y esto se realiza presionando el boton de Registrar
            #usuario,Cuando se valida el usuario se crea la ventana que contiene los botones los
            #cuales tienen asociada una imagen

    def vn1():
        tiempo=tm.time()
        nivel2.config(state=DISABLED)
        nivel3.config(state=DISABLED)
        global imagenes1,arr1,arr3,arr2,matrizimagenes1,count,cont

        v2=Toplevel()
        v2.geometry('420x180')
        v2.title('Nivel 1')
        v2.resizable(0,0)

        count=0
        arr1=[]
        arr2=[]
        arr3=[]
        sonidos=[]
        def cambiar(a,b):

            global count,arr1,arr2,arr3,sonidos,sound,imagenes1,matrizimagenes1,cont,v1,final
            tiempo1=tm.time()

            botones[a][b].config(image=matrizimagenes1[a][b],command=sonar(matrizimagenes1[a][b]))
            botones[a][b].config(state=DISABLED)
            arr3.append(a)
            arr3.append(b)
            final+=1
            count+=1
            arr1.append(matrizimagenes1[a][b])
            arr2.append(botones[a][b])

            print(arr1)
            print(arr2)
            print(arr3)

            # if count == 2:
            #     if str(arr2[0]) == str(arr2[1]):
            #         count = 0
            #         arr2[0].config(image=carta)
            #         arr2[1].config(image=carta)
            #         arr2=[]
            #         arr3=[]
            #         arr1=[]


            if count==3:
                if arr1[0]==arr1[1] and str(arr2[0])!=str(arr2[1]):
                    arr2[0].config(state=DISABLED)
                    arr2[1].config(state=DISABLED)
                    arr1=[]
                    arr1.append(matrizimagenes1[a][b])
                    arr2=[]
                    arr2.append(botones[a][b])

                    arr3=[]
                    arr3.append(a)
                    arr3.append(b)
                    print("comparacion",arr1)
                    print("comparacion",arr2)
                    print("comparacion",arr3)

                    cont+=1
                    count=1
                    final=1
                else:
                    arr2[0].config(image=carta,state=NORMAL)
                    arr2[1].config(image=carta,state=NORMAL)
                    arr3=[]
                    arr2=[]
                    arr2.append(botones[a][b])
                    arr3.append(a)
                    arr3.append(b)
                    arr1=[]
                    arr1.append(matrizimagenes1[a][b])
                    count=1
                    final=1
            print(cont,final)

            tf=tiempo1-tiempo
            best_time=[]
            best_time.append(tf)
            if(cont==3 and final==2):
                best_time.append(tf)
                v[usuario.get()]["nivel1"]=1
                messagebox.showerror("Juego terminado","¡Felicidades,Ganaste!    "+"Completaste el nivel en: "+ str(tf) + "  Segundos" )
                if(tf<v[usuario.get()]["tiempo1"]):
                    v[usuario.get()]["tiempo1"]=tf
                with open("ojala.json","w")as file:
                    ok=json.dump(v,file)
                exit()




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
        nivel1.config(state=DISABLED)
        nivel3.config(state=DISABLED)
        tiempo=tm.time()

        global imagenes2,arr1,arr3,arr2,matrizimagenes2,count,cont
        v3=Toplevel()

        v3.geometry('420x340')
        v3.title('Nivel 2')
        v3.resizable(0,0)
        count=0

        arr1=[]
        arr2=[]
        arr3=[]
        sonidos=[]
        def cambiar(a,b):
            global count,arr1,arr2,arr3,sonidos,sound,imagenes2,matrizimagenes2,cont,final
            tiempo1=tm.time()

            botones[a][b].config(image=matrizimagenes2[a][b],command=sonar(matrizimagenes2[a][b]))
            botones[a][b].config(state=DISABLED)

            arr3.append(a)
            arr3.append(b)
            final+=1
            count+=1
            arr1.append(matrizimagenes2[a][b])
            arr2.append(botones[a][b])
            # if count == 2:
            #     if str(arr2[0]) == str(arr2[1]):
            #         count = 0
            #         arr2[0].config(image=carta)
            #         arr2[1].config(image=carta)
            #         arr2=[]
            #         arr3=[]
            #         arr1=[]
            if count==3:
                if arr1[0]==arr1[1] and str(arr2[0]) != str(arr2[1]):
                    arr2[0].config(state=DISABLED)
                    arr2[1].config(state=DISABLED)
                    arr1=[];arr1.append(matrizimagenes2[a][b])
                    arr2=[];arr2.append(botones[a][b])
                    arr3=[];arr3.append(a);arr3.append(b)
                    cont+=1
                    count=1
                    final=1
                else:
                    arr2[0].config(image=carta,state=NORMAL)
                    arr2[1].config(image=carta,state=NORMAL)
                    arr3=[]
                    arr2=[]
                    arr2.append(botones[a][b])
                    arr3.append(a)
                    arr3.append(b)
                    arr1=[]
                    final=1

                    arr1.append(matrizimagenes2[a][b])
                count=1
            tf=tiempo1-tiempo
            if(cont==7 and final==2):

                messagebox.showerror("Juego terminado","¡Felicidades,Ganaste!    "+"Completaste el nivel en: "+ str(tf) + "  Segundos" )
                v[usuario.get()]["nivel2"]=1
                if(tf<v[usuario.get()]["tiempo2"]):
                    v[usuario.get()]["tiempo2"]=tf
                with open("ojala.json","w")as file:
                    ok=json.dump(v,file)
                exit()

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
        nivel1.config(state=DISABLED)
        nivel2.config(state=DISABLED)
        tiempo=tm.time()
        global imagenes2,arr1,arr3,arr2,matrizimagenes3,count,cont


        v4=Toplevel()
        v4.geometry('630x460')
        v4.title('Nivel 3')
        v4.resizable(0,0)
        count=0
        arr1=[]
        arr2=[]
        arr3=[]
        sonidos=[]
        def cambiar(a,b):
            global count,arr1,arr2,arr3,sonidos,sound,imagenes3,matrizimagenes3,cont,final
            tiempo1=tm.time()

            botones[a][b].config(image=matrizimagenes3[a][b],command=sonar(matrizimagenes3[a][b]))
            botones[a][b].config(state=DISABLED)
            arr3.append(a)
            arr3.append(b)
            final+=1
            count+=1
            arr1.append(matrizimagenes3[a][b])
            arr2.append(botones[a][b])
            # if count == 2:
            #     if str(arr2[0]) == str(arr2[1]):
            #         count = 0
            #         arr2[0].config(image=carta)
            #         arr2[1].config(image=carta)
            #         arr2=[]
            #         arr3=[]
            #         arr1=[]
            if count==3:
                if arr1[0]==arr1[1] and str(arr2[0]) != str(arr2[1]):
                    arr2[0].config(state=DISABLED)
                    arr2[1].config(state=DISABLED)
                    arr1=[];arr1.append(matrizimagenes3[a][b])
                    arr2=[];arr2.append(botones[a][b])
                    arr3=[];arr3.append(a);arr3.append(b)
                    final=1
                    cont+=1
                    count=1
                else:
                    arr2[0].config(image=carta,state=NORMAL)
                    arr2[1].config(image=carta,state=NORMAL)
                    arr3=[]
                    arr2=[]
                    arr2.append(botones[a][b])
                    arr3.append(a)
                    arr3.append(b)
                    arr1=[]

                    arr1.append(matrizimagenes3[a][b])
                    count=1
                    final=1
            tf=tiempo1-tiempo
            if(cont==17 and final==2):
                messagebox.showerror("Juego terminado","¡Felicidades,Ganaste!    "+"Completaste el nivel en: "+ str(tf) + "  Segundos" )
                v[usuario.get()]["nivel3"]=1
                if(tf<v[usuario.get()]["tiempo3"]):
                    v[usuario.get()]["tiempo3"]=tf
                with open("ojala.json","w")as file:
                    ok=json.dump(v,file)
                exit()


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


    try:
        if(v[usuario.get()]):
            z=hb.md5(clave.get().encode()).hexdigest()

            if(v[usuario.get()]["clave"]==z):
                v1 = Toplevel()
                v1.geometry('460x460')
                v1.title('Elegir nivel')

                f1 = PhotoImage(file = 'fon_ventananiveles.png')

                Label(v1,image=f1).place(x=0,y=0)

                nivel1 = Button(v1,text='Nivel 1',width=10,height=6,command=vn1,activeforeground="#1928CE",bd=12,cursor="hand2")
                nivel1.place(x=30,y=150)
                nivel2 = Button(v1,text='Nivel 2',width=10,height=6,command=vn2,activeforeground="#1928CE",bd=12,cursor="hand2")
                nivel2.place(x=180,y=150)
                nivel3 = Button(v1,text='Nivel 3',width=10,height=6,command=vn3,activeforeground="#1928CE",bd=12,cursor="hand2")
                nivel3.place(x=330,y=150)
                reiniciar = Button(v1,text='Reiniciar',width=6,height=1,command=reinicio)
                reiniciar.place(x=28,y=15)

                L1 = Label(v1,text='Elige un nivel',background="#9FDEC0",height=2,width=12).place(x=170,y=50)
                ll2=Label(v1,text="Mejor Tiempo Nivel 1: ",background="#1928CE").place(x=30,y=300)
                ll3=Label(v1,text="Mejor Tiempo Nivel 2: ",background="#1928CE").place(x=30,y=350)
                ll4=Label(v1,text="Mejor Tiempo Nivel 3: ",background="#1928CE").place(x=30,y=400)
                ll5=Label(v1,text=str(v[usuario.get()]["tiempo1"]),width=20,height=1).place(x=200,y=300)
                ll6=Label(v1,text=str(v[usuario.get()]["tiempo2"]),width=20,height=1).place(x=200,y=350)
                ll7=Label(v1,text=str(v[usuario.get()]["tiempo3"]),width=20,height=1).place(x=200,y=400)
                if(v[usuario.get()]["nivel1"]!=0):
                    nivel1.config(state=DISABLED)
                if(v[usuario.get()]["nivel2"]!=0):
                    nivel2.config(state=DISABLED)
                if(v[usuario.get()]["nivel3"]!=0):
                    nivel3.config(state=DISABLED)
            else:
                messagebox.showerror("Error","Clave Erronea")
    except:
        messagebox.showerror("Error","Usuario no existe favor Registrarse")
        Principal.deiconify()


Iniciar=ttk.Button(Principal, text='¡¡Empieza A Jugar!!',command=inicio,cursor="heart").place(x=130,y=180)
            #Se define la funcion de acceso la cual es la encargada de validar si el usuario
            #esta registrado

def abrir():
    global H
    H.destroy()
    Principal.deiconify()
    como_jugar.config(state=NORMAL)


def acceso():
    try:
        if(v[usuario1.get()]):
            messagebox.showerror("Alerta","Usuario Ya Existe")
    except:
        v[usuario1.get()]={"clave":hb.md5(clave1.get().encode()).hexdigest(),"nivel1":0,"nivel2":0,"nivel3":0,"tiempo1":1000,"tiempo2":1000,"tiempo3":1000}
    with open("ojala.json","w")as file:
        ok=json.dump(v,file)
    #print(x)
            #Se define la funcion de registro la cual se encarga de realizar el registro de los usuario
            #para que posterior pueda empezar a Jugar
def registro_():
    global fondo_reg,clave1,usuario1
    reg_usr = Toplevel()
    reg_usr.geometry('308x360')
    reg_usr.resizable(0,0)
    reg_usr.title("Ventana de Registro")
    fondo_=Label(reg_usr,image=fondo_reg).place(x=0,y=0)

    label=Label(reg_usr, text="Usuario: ",background="#8BDFD6").place(x=10,y=80)
    label1=Label(reg_usr, text="Clave:     ",background="#8BDFD6").place(x=10,y=130)

    usuario1 = Entry(reg_usr,background="#7CC6C4")
    usuario1.place(x=90,y=80)

    clave1 = Entry(reg_usr, show="*",background="#7CC6C4")
    clave1.place(x=90,y=130)


    confirmar=ttk.Button(reg_usr, text='Confirmar',command=acceso,cursor="pirate")
    confirmar.place(x=130,y=180)

            #creacion,ubiacacion y configuracion  del boton registrar usuario
def cj():
    global cm,b22,H
    Principal.iconify()
    H=Toplevel()

    H.geometry('511x310')
    H.title('Como Jugar')
    H.resizable(0,0)

    cm=PhotoImage(file = 'cm_jugar.png')

    Label(H,image=cm).place(x=0,y=0)
    b22=ttk.Button(H,text="Cerrar",command=abrir)
    b22.place(x=400,y=250)
    como_jugar.config(state=DISABLED)




registro = ttk.Button(Principal, text='Registrar Usuario',command=registro_,cursor="spider")
registro.place(x=5,y=5)
como_jugar = Button(Principal,text="Como Jugar",command=cj,cursor="spider")
como_jugar.place(x=170,y=6.5)
label=Label(Principal, text="Usuario: ",background="#8BDFD6").place(x=10,y=80)
label1=Label(Principal, text="Clave:     ",background="#8BDFD6").place(x=10,y=130)

archivo="ojala.json"
try:
    with open(archivo,"r") as archivo_l:
        v=json.load(archivo_l)
        print("si existe el archivo",archivo)
        print(v)
except:
    print("no existe el archivo",archivo)


Principal.mainloop()
