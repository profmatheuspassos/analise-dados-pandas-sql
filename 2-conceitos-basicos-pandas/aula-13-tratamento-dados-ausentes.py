import pandas as pd
import numpy as np

# Criando um DataFrame com valores nulos
df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [5, np.nan, np.nan],
    'C': [1, 2, 3]
})

# Removendo linhas que contêm qualquer valor NaN
df.dropna()  # Equivale a df.dropna(axis=0)

# Removendo colunas que contêm qualquer valor NaN
df.dropna(axis=1)

# Removendo colunas que têm pelo menos 2 valores NaN
df.dropna(axis=1, thresh=2)

# Preenchendo todos os valores NaN com 0
df.fillna(0)

# Preenchendo todos os valores NaN com a string "Conteúdo"
df.fillna("Conteúdo")

# Calculando a média dos valores na coluna 'A'
df["A"].mean()

# Preenchendo os valores NaN na coluna 'A' com a média dos valores existentes nessa coluna
df["A"].fillna(value=df["A"].mean())

# Preenchendo valores NaN com o último valor válido anterior na mesma coluna
df.ffill()

# Preenchendo valores NaN com o próximo valor válido na mesma coluna
df.bfill()
