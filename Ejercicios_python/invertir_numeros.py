x = 12345
def ceros(n):
    y = [0 for i in range(0,n)]
    return y
def invertir(x):
    x_lista = str(x)
    y = ceros(len(str(x)))
    for i in range(0, len(str(x))):
        y[i] = int(x_lista[i]) * 10 ** (i)
    print(sum(y))
invertir(x)