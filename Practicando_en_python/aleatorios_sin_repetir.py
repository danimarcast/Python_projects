import numpy as np

n=int(input("digite un numero: "))

def intentos(l):
    m=np.arange(n-l)
    m2=m
    x=True
    intento=1
    while x:
    
        x=False
        np.random.shuffle(m2)
        for i in range(0,n-l):
            if(m2[i]==i):
                x
            else:
                intento=intento+1
#                print(m2)
                x=True
     
   
    return(intento)


print("n","cantidad")
for i in range(n-2,-1,-1):
    k=int(intentos(i)/2)
    print(abs(i-n),k*"* ")
    
