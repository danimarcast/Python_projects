
def ordenar_n (lista, n):
    longitud = len(lista)-1
    for i in range(0, n):
        for j in range(0, longitud):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return lista

print(ordenar_n([1,4,2,5,-1,8,-1],7))
print([1,4,2,5,-1,8,-1])