def miremos(A):
  if A[0] % 2 == 0:
    par = True   # True para par
  else:
    par = False  # False para impar

  listas = []
  lista  = []

  for i in A:
    if i % 2 == 0 and par == True:
      lista.append(i)
    elif i % 2 == 1 and par == False:
      lista.append(i)
    else:
      listas.append(lista)
      lista = [i]
      par = not par
  return listas

import random

P = [random.randint(0, 100) for _ in range(100)]
LN = miremos(P)
a = sorted(LN, key = lambda x: len(x))[-1]
print(a)
print(f"Ganan {'Azules/Pares' if a[0]%2==0 else 'Rojas/Impares'}")