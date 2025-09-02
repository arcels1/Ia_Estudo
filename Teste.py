import matplotlib.pyplot as plt


# Criar figura e eixos
fig, ax = plt.subplots()

# Definir limites do gráfico
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Adicionar linhas dos eixos X e Y no meio do gráfico
ax.axhline(0, color='black', linewidth=1)  # eixo X
ax.axvline(0, color='black', linewidth=1)  # eixo Y

# Adicionar grade
ax.grid(True, linestyle='--', alpha=0.5)
# Adicionando um ponto
ax.plot(3, 4, 'bo')  # ponto azul em (3, 4)

# Adicionando uma função linear
x = range(-10, 11)
y = [2*i + 1 for i in x]
ax.plot(x, y, 'g-')  # linha verde representando y = 2x + 1

# Marcar o ponto de origem
ax.plot(0, 0, 'ro')  # ponto vermelho na origem

# Títulos dos eixos
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_title('Plano Cartesiano 2D')

plt.gca().set_aspect('equal')  # deixa os eixos com mesma escala
plt.show()






xLinha = np.random.uniform(-2,2,size=60)
    print(len(xLinha))
    yLinha = np.zeros(len(xLinha))
    for i in range(0,len(xLinha)):
        if (xLinha[i] >= 0):
            yLinha[i] = 1
            continue
        yLinha[i] = 0


    ax.plot(xLinha, yLinha, 'go')