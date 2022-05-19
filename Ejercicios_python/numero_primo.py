
def primo(p):
    primo = True
    for j in range(1,4294967295+1):
        if j != p and j != 1:
            if p % j == 0:
                primo = not primo
                break
            else:
                primo = primo
                break
    return primo
print(primo(17))