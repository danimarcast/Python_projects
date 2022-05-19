def conj_cubierto (S,n,P,m):
    contador = 0
    for i in range(0,n):
        for j in range(0,m):
            if S[i][0] <= P[j] <= S[i][1]:
                contador +=1
                break
    if contador == n:
        return True
    else:
        return False

print(conj_cubierto([[-10,3],[0,2],[2.5,4.1],[5,8],[4,6]],5,[1,3,4,2,8],5))
