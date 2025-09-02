import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dados_treino = pd.read_csv('iris.csv')
print(dados_treino)
dados_treino.head()
X = dados_treino.iloc[:, [0, 1, 2, 3]].values
y = dados_treino.iloc[0:100,4].values
print( dados_treino.iloc[:,[0,1,2,3]])
Sepala_comprimento = dados_treino.iloc[0:100, 0].values
Sepala_largura= dados_treino.iloc[0:100, 1].values
Petala_comprimento=dados_treino.iloc[0:100, 2].values
Petala_largura=dados_treino.iloc[0:100, 3].values


data = {'Sepala_Comprimento': Sepala_comprimento,
        'Sepala_Largura': Sepala_largura,
        'Petala_comprimento': Petala_comprimento,
        'Petala_largura': Petala_largura}
print(data)
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
# 'output.csv' is the desired file name
# index=False prevents writing the DataFrame index as a column in the CSV
df.to_csv('output.csv', index=False)

print("CSV file 'output.csv' created successfully.")
