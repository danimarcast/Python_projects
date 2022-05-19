
def zeros(n):
    y = [0 for i in range(n)]
    return y
def cambiar(n):
    lista = zeros(n+1)
    for i in range(0,n+1):
        lista[i] = i
        if lista[i]%3 == 0:
            if lista[i]%5 == 0 or lista[i]%n == 0:
                lista[i]="Fizz Buzz"
            else:
                lista[i]="Fizz"
        elif lista[i]%5 == 0:
            if lista[i] % 3 == 0 or lista[i]%n == 0:
                lista[i] = "Fizz Buzz"
            else:
                lista[i] = "Buzz"
    return lista
print(cambiar(40))