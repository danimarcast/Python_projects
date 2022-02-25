seguirChateando=True

while seguirChateando:
    texto = input(">")
    if texto=='salir':
        seguirChateando=False
    texto=texto.replace(':)',"🙂")
    texto=texto.replace(':P',"😛")
    texto=texto.replace(':p',"😛")
    texto=texto.replace(':(',"🙁")
    texto=texto.replace(':*',"😚")
    print(texto)
