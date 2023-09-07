import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt




# MLE
def mle(X):
    return X

# Estimador de James-Stein
def james_stein(X):
    assert len(X) > 2
    return np.maximum(1 - ((len(X) - 2) / sum(X**2)), 0) * X

# Calculalo del error de media cuadratica
def mse(X_pred, X):
    return ((X - X_pred)**2).mean()

def plot_range(k, B=100000):
    error_mle = np.empty(B)
    error_js = np.empty(B)
    for i in range(1,B):
        theta = np.ones(k)
        X = norm.rvs(loc=1, scale=1, size=k)
        theta_hat_mle = mle(X)
        theta_hat_js = james_stein(X)
        error_mle[i] = mse(theta_hat_mle, theta)
        error_js[i] = mse(theta_hat_js, theta)

    plt.figure(figsize=(12, 8))
    plt.hist(error_mle, density=True, bins=100, histtype='step', color='blue', label='MLE, k = ' + str(k))
    plt.hist(error_js, density=True, bins=100, histtype='step', color='red', label='James-Stein, k = ' + str(k))
    plt.legend(loc='upper right')
    #plt.show();



plot_range(3)
plt.savefig('Stein1.png')
plot_range(10)
plt.savefig('Stein2.png')
plot_range(100)
plt.savefig('Stein3.png')
plot_range(1000)
plt.savefig('Stein4.png')

