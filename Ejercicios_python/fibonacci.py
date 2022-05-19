
#Diseñe un programa que calcule el n-esimo t́ermino de la serie
# de Fibonacci, recordando que la serie de Fibonacci se define por la expresión recursiva
# : f(0)=1, f(1) = 1, f(n)=f(n-1)+f(n-2)

def zeros(m):
    y = [0 for i in range(m)]
    return y
def fibonacci(n):
    lista = zeros(n)
    for i in range (0,n):
        lista[0] = 1  # Primer termino de fibonacci f0
        lista[1] = 1  # Segundo termino de fibonacci f1
        if i>1:
            lista[i]=lista[i-1]+lista[i-2]
    return lista[-1]
print(fibonacci(6))