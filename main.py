import numpy as np
import matplotlib.pyplot as plt

listaEntrada = np.array([[0,0,1,1],
                         [0,1,0,1]])
print(listaEntrada)
def perceptron_elementar_exemplo_duas_entradas(x1, x2):

    #pesos
    w1 = 1
    w2 = 1

    x=[x1,x2]
    w=[w1,w2]

    n= len(w)
    v = 0
    for j in range(0,n):
        v += x[j]*w[j]

    return v

def funcao_ativacao(u,z):
    if(u>z):
        return +1
    return 0

print("_______________")
print("A | B | U | Y |  limiar = 0")
for i in range(0,4):

    x1 = listaEntrada[0][i]
    x2 = listaEntrada[1][i]
    u = perceptron_elementar_exemplo_duas_entradas(x1, x2)
    y = funcao_ativacao(u,z=0)
    print(f"{x1} | {x2} | {u} | {y}")
    
print("_______________")
print("A | B | U | Y |  limiar = 1")
for i in range(0,4):

    x1 = listaEntrada[0][i]
    x2 = listaEntrada[1][i]
    u = perceptron_elementar_exemplo_duas_entradas(x1, x2)
    y = funcao_ativacao(u,z=1)
    print(f"{x1} | {x2} | {u} | {y}")


