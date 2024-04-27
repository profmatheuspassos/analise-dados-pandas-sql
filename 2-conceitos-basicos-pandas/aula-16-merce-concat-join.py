import pandas as pd
import numpy as np

# Criando um DataFrame df1 com colunas A, B, C, D e índice de 0 a 3
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
}, index=[0, 1, 2, 3])

# Criando um DataFrame df2 com colunas A, B, C, D e índice de 4 a 7
df2 = pd.DataFrame({
    'A': ['A4', 'A5', 'A6', 'A7'],
    'B': ['B4', 'B5', 'B6', 'B7'],
    'C': ['C4', 'C5', 'C6', 'C7'],
    'D': ['D4', 'D5', 'D6', 'D7']
}, index=[4, 5, 6, 7])

# Criando um DataFrame df3 com colunas A, B, C, D e índice de 8 a 11
df3 = pd.DataFrame({
    'A': ['A8', 'A9', 'A10', 'A11'],
    'B': ['B8', 'B9', 'B10', 'B11'],
    'C': ['C8', 'C9', 'C10', 'C11'],
    'D': ['D8', 'D9', 'D10', 'D11']
}, index=[8, 9, 10, 11])

# Concatenando df1, df2 e df3 verticalmente
pd.concat([df1, df2, df3])

# Tentativa de concatenar df1, df2 e df3 horizontalmente, resultando em um DataFrame com muitos valores NaN devido a índices não alinhados
pd.concat([df1, df2, df3], axis=1)

# Criando dois DataFrames, esquerda e direita, com uma coluna chave comum para futuras operações de merge
esquerda = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})
direita = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})

# Mesclando os DataFrames esquerda e direita usando a coluna "key" como chave
pd.merge(esquerda, direita, on="key")

# Criando DataFrames esquerda e direita com múltiplas chaves para demonstrar merge complexo
esquerda = pd.DataFrame({
    'key1': ['K0', 'K0', 'K1', 'K2'],
    'key2': ['K0', 'K1', 'K0', 'K1'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})
direita = pd.DataFrame({
    'key1': ['K0', 'K1', 'K1', 'K2'],
    'key2': ['K0', 'K0', 'K0', 'K0'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})

# Demonstrando diferentes tipos de joins: inner, outer, right, e left com múltiplas chaves
pd.merge(esquerda, direita, on=["key1", "key2"])
pd.merge(esquerda, direita, how="outer", on=["key1", "key2"])
pd.merge(esquerda, direita, how="right", on=["key1", "key2"])
pd.merge(esquerda, direita, how="left", on=["key1", "key2"])

# Criando DataFrames esquerda e direita para demonstrar join com índices como chaves
esquerda = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
}, index=['K0', 'K1', 'K2'])
direita = pd.DataFrame({
    'C': ['C0', 'C2', 'C3'],
    'D': ['D0', 'D2', 'D3']
}, index=['K0', 'K2', 'K3'])

# Realizando join entre esquerda e direita com diferentes tipos de joins: inner e outer
esquerda.join(direita)
esquerda.join(direita, how="outer")
