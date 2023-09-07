import numpy as np
import matplotlib as mpl
import math
# Importar el módulo pyplot con el alias plt
import matplotlib.pyplot as plt

# Crear la figura y los ejes
fig=plt.figure(figsize=(6, 4))
ax=plt.axes()
ax.set_xlim([-9, 15])
ax.set_ylim([-0.01,0.32])
# Dibujar puntos y Gaussianas
plt.scatter(x = [-4, -2.5, -1, 0, 2, 4, 5], y = [0,0,0,0,0,0,0],c="#000000")
def normal_distribution(x, mean, sigma):
    return np.exp(-1*((x-mean)**2)/(2*(sigma**2)))/(math.sqrt(2*np.pi) * sigma)


#ss=normal_distribution(3, 0, 0.2)
mean1= -4
sigma1 =  1

x1 = np.linspace(-8,12, 300)

mean2=0
sigma2 =np.sqrt(0.2)

mean3=8
sigma3 = np.sqrt(3)


y1 = (1/3)*(normal_distribution(x1, mean1, sigma1))
y2 = (1/3)*(normal_distribution(x1, mean2, sigma2))
#print(normal_distribution(0,0,0.2))
y3 = (1/3)*(normal_distribution(x1, mean3, sigma3))

plt.plot(x1, y1, 'r', label='$\pi_1\mathcal{N}(x|\mu_1,\sigma_1^2)$',linestyle = 'dotted',linewidth=2)
plt.plot(x1, y2, 'g', label='$\pi_2\mathcal{N}(x|\mu_2,\sigma_2^2)$',linestyle = 'dotted',linewidth=2)
#plt.plot(x1, y3, 'b', label='$\pi_3\mathcal{N}(x|\mu_3,\sigma_3^2)$',linestyle = 'dotted',linewidth=2)
plt.plot(x1,y1+y2+0.01,'#000000',label ='GMM')
#plt.legend()

# Guardar el gráfico en formato png
plt.savefig('graf_gmm1.png')
# Mostrar el gráfico
plt.show()
