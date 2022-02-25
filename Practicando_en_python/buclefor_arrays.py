##Boleanos: True/False
#Numeros: 1234
##textos: "Hola mundo"
##Array un objeto de multiples entradas.
arreglo=['banana','melon','sandia','pera']
arreglo.reverse()
arreglo.remove('sandia')
#arreglo.clear()
arreglo.append('kiwi')

#print(arreglo.count('kiwi'))
for fruta in arreglo:
    if fruta =='sandia':
        break
    print("La fruta es " + fruta)

texto='hola mundo'
for letra in texto:
    print(letra)
for numero in range(10):
    print(numero)