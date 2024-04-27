import pandas as pd
import numpy as np

# Criando listas que representam os níveis externo e interno de um índice hierárquico
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))  # Criando uma lista de tuplas que combinam os níveis externo e interno
print(f"Índice hierárquico criado: {hier_index}")

# Convertendo a lista de tuplas em um objeto MultiIndex do Pandas
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(f"Objeto MultiIndex criado: {hier_index}")

# Criando um DataFrame com o índice hierárquico definido e duas colunas de dados aleatórios
df = pd.DataFrame(np.random.randn(6, 2), index=hier_index, columns=['A', 'B'])
print("DataFrame criado com índice hierárquico:")
print(df)

# Acessando todos os dados sob o grupo "G1"
print("Dados do grupo 'G1':")
print(df.loc["G1"])

# Acessando os dados na posição (G1, 1)
print("Dados do grupo 'G1' na posição 1:")
print(df.loc["G1"].loc[1])

# Nomeando os níveis do índice como "Grupo" e "Número"
df.index.names = ["Grupo", "Número"]
print("DataFrame com índices nomeados:")
print(df)

# Usando o método 'xs' para acessar diretamente todos os dados sob o grupo "G1" sem referenciar o segundo nível
print("Acessando diretamente todos os dados do grupo 'G1' com xs:")
print(df.xs("G1"))

# Usando o método 'xs' para extrair todos os dados onde o segundo nível do índice é 1, independente do grupo
print("Dados onde o nível 'Número' é 1 em todos os grupos:")
print(df.xs(1, level="Número"))

# Usando o método 'xs' para extrair todos os dados onde o segundo nível do índice é 2, independente do grupo
print("Dados onde o nível 'Número' é 2 em todos os grupos:")
print(df.xs(2, level="Número"))
