def zeros (n):
    y = [0 for i in range(0, n)]
    return y
def matriz_nula(n,m):
    N = zeros(n)
    for i in range (0,n):
        N[i] = zeros(m)
    return N
def mult_matrix(A, B):
    C = matriz_nula(len(A),len(B[0]))
    D=""
    for i in range (0,len(A)):
        for j in range (0,len(B[0])):
            for k in range(0, len(B[0])):
                C[i][j] += A[i][k]*B[k][j]
    for m in range(len(C)):
        D = print(C[m]," ")
    return D
A=[[1,1],
   [2,4]]
B=[[2,1],
   [7,3]]
C=mult_matrix(A, B)


