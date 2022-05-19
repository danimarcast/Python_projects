import random
def zeros(n):
    y = [0 for i in range(n)]
    return y

lista = zeros(20)
def lista_aleatorios(l):
    for i in range (0, len(l)-1):
        l[i] = random.randint(0, 1000)
    return l
l=lista_aleatorios(lista)
print(l)
def diviir(lista):
    l1=[] # Lista de pares
    l2=[] # lista de impares
    for i in range(0,len(lista)-1):
        if lista[i] % 2==0:
            l1.append(lista[i])
        else:
            l2.append(lista[i])
    return print(l1,l2)
diviir(l)