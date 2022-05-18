
def unir_y_ordenar(lista1, lista2):
    lista=lista1+lista2
    longitud = len(lista)-1
    for i in range(0, longitud):
        for j in range(0, longitud):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return print(lista)


a = [1, -10, 3, 4]
b = [5, 6, -2]
print(a+b)
unir_y_ordenar(a, b)
