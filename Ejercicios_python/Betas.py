
import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt

n = 10
k = 2

x = np.linspace(0, 1, 200)

plt.figure(figsize=(12, 8))
for a, b in [(1/2, 1/2), (1, 1), (10, 10), (100, 100)]:
    plt.plot(x, beta.pdf(x, k + a - 1, n - k + b - 1), label='prior = Beta(' + str(a) + ', ' + str(b) +')')
    plt.legend()

plt.savefig('betas.png')
plt.show();