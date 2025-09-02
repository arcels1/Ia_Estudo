import numpy as np
import matplotlib.pyplot as plt

plt.show()
listaEntrada = np.array([[0,0,1,1],[0,1,0,1]])
print(listaEntrada)
def perceptron_exemplo_duas_entradas(x1, x2):

    #pesos
    w1 = 0.5
    w2 = 0.5

    x=[x1,x2]
    w=[w1,w2]

    n= len(w)
    v = 0
    for j in n:
        v += x[j]*w[j]

    return v
