import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Criando grade de 2x2
X = np.array([[1, -1], [1, -1]])
Y = np.array([[1, 1], [-1, -1]])
Z = np.array([[1.5, 0.5], [0.5, -0.5]])
ax.grid(True)
ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")
ax.set_zlabel("Eixo Z")
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()