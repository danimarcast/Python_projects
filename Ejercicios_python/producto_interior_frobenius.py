def pfrobenius(A, B):
    p_interno = 0
    if len(A)== len(B):
        for i in range(len(A)):
            for j in range(len(B)):
                p_interno +=A[i][j]*B[i][j]
    return print(p_interno)

A=[[1,2],[3,4]]
B=[[5,6],[7,8]]
pfrobenius(A,B)
