# Importando a biblioteca pandas
import pandas as pd
# Importando a função randn da biblioteca numpy
from numpy.random import randn

# Criando um DataFrame com dados aleatórios, índices de A a E e colunas nomeadas como W, X, Y, Z
df = pd.DataFrame(randn(5, 4), index=["A", "B", "C", "D", "E"], columns="W X Y Z".split())

# Exibindo o DataFrame criado
print(f"DataFrame completo:\n{df}\n")

# Acessando os valores na coluna 'W' para os índices 'A' e 'B'
print(f"Valores em 'W' para índices 'A' e 'B':\n{df.loc[['A', 'B'], 'W']}\n")

# Atribuindo os valores acessados a uma variável e verificando seu tipo
teste = df.loc[["A", "B"], "W"]
print(f"Tipo do objeto 'teste': {type(teste)}\n")

# Acessando os valores na coluna 'W' para os índices 'A' e 'B' e mantendo a estrutura de DataFrame
print(f"DataFrame com 'W' para índices 'A' e 'B':\n{df.loc[['A', 'B'], ['W']]}\n")

# Atribuindo os valores acessados a outra variável e verificando seu tipo
teste2 = df.loc[["A", "B"], ["W"]]
print(f"Tipo do objeto 'teste2': {type(teste2)}\n")

# Acessando subconjunto de linhas e colunas usando índices numéricos
print(f"Valores da segunda até a última coluna, excluindo a última linha:\n{df.iloc[:-1, 1:4]}\n")
print(f"Valores da segunda até a terceira coluna, da segunda até a quarta linha:\n{df.iloc[1:4, 1:3]}\n")

# Criando um DataFrame booleano onde os valores são maiores que zero
print(f"DataFrame booleano (valores > 0):\n{df > 0}\n")

# Aplicando o filtro anterior para manter apenas valores positivos no DataFrame
print(f"DataFrame com valores positivos:\n{df[df > 0]}\n")

# Verificando quais valores na coluna 'X' são maiores que zero
print(f"Valores em 'X' maiores que zero:\n{df['X'] > 0}\n")

# Filtrando o DataFrame para manter apenas as linhas onde 'X' > 0
print(f"Linhas onde 'X' > 0:\n{df[df['X'] > 0]}\n")

# Filtrando o DataFrame para manter apenas as linhas onde 'X' > 0 e 'W' > 0
print(f"Linhas onde 'X' > 0 e 'W' > 0:\n{df[(df['X'] > 0) & (df['W'] > 0)]}\n")
