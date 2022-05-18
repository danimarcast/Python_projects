def log2(n):
    l2 = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            l2 -= 1 / i
        else:
            l2 += 1 / i
    return l2


def cantidad_necesaria(error):
    bandera = True
    n = 1
    while bandera:
        if abs(log2(n) - log2(n + 1)) <= error:
            bandera = False
            return n

        n += 1

print(cantidad_necesaria(1e-3))