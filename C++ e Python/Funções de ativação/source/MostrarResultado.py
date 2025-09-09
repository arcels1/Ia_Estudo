import pandas as pd
import numpy as np
import cffi as ffi
import matplotlib.pyplot as plt
import subprocess as subp
import sys

#//////////PLANO CARTESIANO/////////
def criar_plano_cartesiano():
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1, 2)
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.axhline(1, color='grey', linewidth=0.5)


    ax.grid(True, linestyle='--', alpha=0.5)
    return ax

def criar_plano_cartesiano_completo():
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.axhline(1, color='grey', linewidth=0.5)
    ax.axhline(-1, color='grey', linewidth=0.5)
    ax.grid(True, linestyle='--', alpha=0.5)
    return ax
#////////// MONTAR PLANO CARTESIANO
def montar_plano_cartesiano(entradas, saidas, cor, plano_cartesiano, label):
    print("coordenadas X")
    print(entradas)

    print("coordenadas Y")
    print(saidas)

    plano_cartesiano.plot(entradas,saidas,cor, label = label)
    plano_cartesiano.set_xlabel('V')
    plano_cartesiano.set_ylabel('Phi(V)')
    return plano_cartesiano

def mostrar_resultado(arquivoNome, plano_existente ,titulo_plano,completo, label):

    try:
        df = pd.read_csv("funcao/resultados/"+arquivoNome)
    except:
        print("Dados de "+arquivoNome+" não encontrados")
    entradas = df["entradas"].to_numpy()
    saidas = df["saidas"].to_numpy()
    if plano_existente is None:
     plano = None
     if(completo):
         plano = criar_plano_cartesiano_completo()
         plano.set_title(titulo_plano)

     else:
         plano = criar_plano_cartesiano()
         plano.set_title(titulo_plano)

     return montar_plano_cartesiano(entradas, saidas, "go", plano, label)
    else:
        return montar_plano_cartesiano(entradas, saidas, "ro", plano_existente, label)




limiar = mostrar_resultado("ResultadoLimiar.csv", None, "Resultado Limiar", False, "V")

linear_partes = mostrar_resultado("ResultadoLinearParte.csv", None, "Resultado Linear por Parte", False, "V")

logistica = mostrar_resultado("ResultadoLogisticaA1.csv", None, "Resultado Logistica", False, "A1")
logistica = mostrar_resultado("ResultadoLogisticaA10.csv", logistica, "Resultado Logistica", False, "A10")
logistica.legend()

hiperbolica = mostrar_resultado("ResultadoTanHipA1.csv", None, "Resultado Hiperbolica", True, "A1")
hiperbolica = mostrar_resultado("ResultadoTanHipA10.csv", hiperbolica, "Resultado Hiperbolica", True, "A10")
hiperbolica.legend()





plt.show()