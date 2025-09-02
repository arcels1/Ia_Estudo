import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dados_treino = pd.read_csv('iris.csv')
dados_treino.head()
entrada_flor = dados_treino.iloc[:,[0,1,2,3]]
valor_esperado = dados_treino.iloc[:,4]

#//////////PLANO CARTESIANO/////////
def criar_plano_cartesiano():
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1, 2)
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.grid(True, linestyle='--', alpha=0.5)
    return ax

def criar_plano_cartesiano_completo():
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.grid(True, linestyle='--', alpha=0.5)
    return ax

def montar_plano_cartesiano(lista_resposta, y, cor, ax, label):
    coordenadasX = np.zeros(len(lista_resposta[0]))
    coordenadasY = np.zeros(len(lista_resposta[0]))
    for j in range(0, len(lista_resposta[0])):
        coordenadasX[j]=lista_resposta[2][j]
        coordenadasY[j]=y[j]

    print("coordenadas X")
    print(coordenadasX)

    print("coordenadas Y")
    print(coordenadasY)

    ax.plot(coordenadasX,coordenadasY,cor, label = label)
    ax.set_xlabel('V')
    ax.set_ylabel('Phi(V)')
    return ax


#//////////ADALINE /////////
def adaline(x,w):
    n= len(w)
    u = 0
    for i in range(0,n):
        u += x[i]*w[i]



    return u



#/////////// Potencial de ativacao //////////////
def potencial_ativacao(lista_resposta):
    X = np.array([[lista_resposta[0][0],lista_resposta[0][1]],
                 [lista_resposta[0][2],lista_resposta[0][3]]])

    Y = np.array([[lista_resposta[1][0],lista_resposta[1][1]],
                  [lista_resposta[1][2],lista_resposta[1][3]]])

    Z = np.array([[lista_resposta[2][0], lista_resposta[2][1]],
                  [lista_resposta[2][2], lista_resposta[2][3]]])





#///////////// Funcoes de ativacao //////////////

#Funcao de decisao abrupta
def funcao_de_limiar(lista_resposta):
    y = np.zeros(len(lista_resposta[0]))
    for i in range(len(lista_resposta[0])):
        if(lista_resposta[2][i] >= 0):
            y[i] = 1
            continue
        y[i] = 0
    return y

#Combinador linear com a tentativa de reduzir a limearidade
def funcao_de_linear_por_partes(lista_resposta, a):
    a = a
    y = np.zeros(len(lista_resposta[0]))

    for i in range(0,len(lista_resposta[0]-1)):
        if(lista_resposta[2][i] >= 0.5):
            y[i] = 1
            continue
        if(-0.5<(lista_resposta[2][i])<0.5):
            y[i] = lista_resposta[2][i]+0.5
            continue
        if(lista_resposta[2][i] < -0.5/a):
            y[i] = 0

    return y

#Funcoes signoides (sao funcoes com formato de S)

numero_euler = 2.71828183

def funcao_logistica(lista_resposta,amplificacao):
    y = np.zeros(len(lista_resposta[0]))
    for i in range(len(lista_resposta[0])):
        y[i] = 1/(1+(numero_euler**((-amplificacao)*lista_resposta[2][i])))
    return y

def funcao_tangente_hiperbolica(lista_resposta,amplificacao):
    y = np.zeros(len(lista_resposta[0]))
    for i in range(len(lista_resposta[0])):
        #senh =((numero_euler**(amplificacao*lista_resposta[2][i]))-numero_euler**(-(amplificacao*lista_resposta[2][i])))/2
        #cosh =((numero_euler**(amplificacao*lista_resposta[2][i]))+numero_euler**(-(amplificacao*lista_resposta[2][i])))/2
        #y[i] = senh/cosh
        y[i] = ((numero_euler**(2*(amplificacao*lista_resposta[2][i])))-1)/((numero_euler**(2*(amplificacao*lista_resposta[2][i])))+1)
    return y




#
# print("REFERENCIA")
# lista_referencia_com_resposta = np.zeros((3,60))
# for i in range(0,len(referencia[0])):
#
#     x1 = referencia[0][i]
#     x2 = referencia[1][i]
#     u = perceptron_elementar_exemplo_duas_entradas(x1, x2)
#     #y = funcao_ativacao(u,z=0)
#     lista_referencia_com_resposta[0][i]=x1
#     lista_referencia_com_resposta[1][i]=x2
#     lista_referencia_com_resposta[2][i]=u
# print(lista_referencia_com_resposta[0])
# print(lista_referencia_com_resposta[1])
# print(lista_referencia_com_resposta[2])
#
# plano_cartesiano_linear_por_partes = criar_plano_cartesiano()
# plano_cartesiano_limiar = criar_plano_cartesiano()
# plano_cartesiano_logistica = criar_plano_cartesiano()
# plano_cartesiano_tangente_hiperbolica= criar_plano_cartesiano_completo()
#
# plano_cartesiano_linear_por_partes.set_title("Linear Por Partes")
# plano_cartesiano_limiar.set_title("Limiar")
# plano_cartesiano_logistica.set_title("Logistica")
# plano_cartesiano_tangente_hiperbolica.set_title("Tangente Hiperbolica")
#
# y= funcao_de_linear_por_partes(lista_referencia_com_resposta,1)
# y_limiar = funcao_de_limiar(lista_referencia_com_resposta)
# y_logistica = funcao_logistica(lista_referencia_com_resposta,1)
# y_logistica_amplificacao10 = funcao_logistica(lista_referencia_com_resposta,10)
# y_tangente_hiperbolica = funcao_tangente_hiperbolica(lista_referencia_com_resposta,1)
# y_tangente_hiperbolica_amplificacao10  = funcao_tangente_hiperbolica(lista_referencia_com_resposta,10)
#
#
# print("Linear por partes")
# print(y)
#
# print("Limiar")
# print(y_limiar)
#
# print("Logistica A:1")
# print(y_logistica)
# print("Logistica A:10")
# print(y_logistica_amplificacao10)
#
# print("Tangente Hiperbolica A:1")
# print(y_tangente_hiperbolica)
# print("Tangente Hiperbolica A:10")
# print(y_tangente_hiperbolica_amplificacao10)
#
#
# plano_cartesiano_linear_por_partes = montar_plano_cartesiano(lista_referencia_com_resposta, y, 'go', plano_cartesiano_linear_por_partes, "Y")
#
# plano_cartesiano_limiar = montar_plano_cartesiano(lista_referencia_com_resposta, y_limiar, "bo", plano_cartesiano_limiar,"Y")
#
# plano_cartesiano_logistica= montar_plano_cartesiano(lista_referencia_com_resposta, y_logistica,"ro",plano_cartesiano_logistica,"A=1")
# plano_cartesiano_logistica= montar_plano_cartesiano(lista_referencia_com_resposta, y_logistica_amplificacao10,"co",plano_cartesiano_logistica,"A=10")
# plano_cartesiano_logistica.legend()
#
# plano_cartesiano_tangente_hiperbolica = montar_plano_cartesiano(lista_referencia_com_resposta, y_tangente_hiperbolica,"ro", plano_cartesiano_tangente_hiperbolica,"A=1")
# plano_cartesiano_tangente_hiperbolica = montar_plano_cartesiano(lista_referencia_com_resposta, y_tangente_hiperbolica_amplificacao10,"go", plano_cartesiano_tangente_hiperbolica,"A=10")
# plano_cartesiano_tangente_hiperbolica.legend()

#funcao_de_limiar(lista_resposta)
#funcao_de_linear_por_partes(lista_resposta, a=0.5)
#potencial_ativacao(lista_resposta)
plt.show()




