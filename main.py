import numpy as np
import matplotlib.pyplot as plt

listaEntrada = np.array([[1,1,-1,-1],
                         [1,-1,1,-1]])
print(listaEntrada)
def perceptron_elementar_exemplo_duas_entradas(x1, x2):

    #bias
    w0=0.5
    x0=1

    #pesos
    w1 = 0.5
    w2 = 0.5

    x=[x0,x1,x2]
    w=[w0,w1,w2]

    n= len(w)
    v = 0
    for j in range(0,n):
        v += x[j]*w[j]

    return v

def potencial_ativacao(lista_resposta):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')


    X = np.array([[lista_resposta[0][0],lista_resposta[0][1]],
                 [lista_resposta[0][2],lista_resposta[0][3]]])

    Y = np.array([[lista_resposta[1][0],lista_resposta[1][1]],
                  [lista_resposta[1][2],lista_resposta[1][3]]])

    Z = np.array([[lista_resposta[2][0], lista_resposta[2][1]],
                  [lista_resposta[2][2], lista_resposta[2][3]]])
    ax.grid(True)
    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.set_zlabel("v")
    ax.set_title("Plano de mapeamento potencial de ativação")
    surface = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='black', alpha=0.9)
    plt.show()

def funcao_de_limiar(lista_resposta):
    y = np.zeros(len(lista_resposta[0]))
    for i in range(len(lista_resposta[0])):
        if(lista_resposta[2][i] >= 0):
            y[i] = 1
            continue
        y[i] = 0

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1, 2)
    ax.set_title("Funcao de limiar (Hard-Limiter)")

    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.grid(True, linestyle='--', alpha=0.5)

    for j in range(0,len(lista_resposta[0])):
        ax.plot(lista_resposta[2][j], y[j], 'bo')

    # Referencia
    xLinha = np.random.uniform(-2,2,size=60)
    print(len(xLinha))
    yLinha = np.zeros(len(xLinha))
    for i in range(0,len(xLinha)):
        if (xLinha[i] >= 0):
            yLinha[i] = 1
            continue
        yLinha[i] = 0


    ax.plot(xLinha, yLinha, 'go')

    ax.set_xlabel('V')
    ax.set_ylabel('Phi(V)')
def funcao_de_linear_por_partes(lista_resposta, a):
    a = a
    y = np.zeros(len(lista_resposta[0]))

    for i in range(len(lista_resposta[0])):
        if(lista_resposta[2][i] >= 0.5/a):
            y[i] = 1
            continue
        if((-0.5/a)>(a*lista_resposta[2][i])>(0.5/a)):
            y[i] = a*lista_resposta[2][i]+0.5
            continue
        if(lista_resposta[2][i] <= -0.5/a):
            y[i] = 0

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1, 2)
    ax.set_title("Funcao de linear por partes")
    #Referencia
    xLinha = np.random.uniform(-2, 2, size=120)
    print(len(xLinha))
    yLinha = np.zeros(len(xLinha))
    for i in range(len(xLinha)):
        if (xLinha[i] >= (0.5 / a)):
            yLinha[i] = 1
            continue
        if ((-0.5 / a) > (a * xLinha[i])):
            if((a * xLinha[i])> (0.5/a)):
                yLinha[i] = a * xLinha[i] + 0.5
                print("Gay")
                continue
        if (xLinha[i] <= -0.5 / a):
            yLinha[i] = 0

    ax.plot(xLinha, yLinha, 'go')

    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.grid(True, linestyle='--', alpha=0.5)

    for j in range(0,len(lista_resposta[0])):
        ax.plot(lista_resposta[2][j], y[j], 'bo')



    ax.set_xlabel('V')
    ax.set_ylabel('Phi(V)')
    plt.show()
print("_______________")
print("A | B | U | Y |  ")

lista_resposta= np.zeros((3,4))
for i in range(0,len(lista_resposta[0])):

    x1 = listaEntrada[0][i]
    x2 = listaEntrada[1][i]
    u = perceptron_elementar_exemplo_duas_entradas(x1, x2)
    #y = funcao_ativacao(u,z=0)
    #print(f"{x1} | {x2} | {u} | {y}")
    print(f"{x1} | {x2} | {u} |")
    lista_resposta[0][i]=x1
    lista_resposta[1][i]=x2
    lista_resposta[2][i]=u
print(lista_resposta)
#funcao_de_limiar(lista_resposta)
#funcao_de_linear_por_partes(lista_resposta, a=0.5)
#potencial_ativacao(lista_resposta)




