
def dfactorial(n):
    f = 1
    if n % 2 ==0:
        for i in range(1, n+1):
             if i % 2 == 0:
                 f *= i
    if n%2 != 0:
        for i in range(1, n+1):
             if i % 2 != 0:
                 f *= i
    return print(f)

dfactorial(15)