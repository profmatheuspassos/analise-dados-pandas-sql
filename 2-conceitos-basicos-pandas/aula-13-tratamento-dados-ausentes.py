import pandas as pd
import numpy as np

# Criando um DataFrame com valores nulos
df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [5, np.nan, np.nan],
    'C': [1, 2, 3],
    'D': [5, np.nan, 7]
})

print("DataFrame original:")
print(df)

# Removendo linhas que contêm qualquer valor NaN
print("\nDataFrame após remover linhas com qualquer valor NaN:")
print(df.dropna())  # Equivale a df.dropna(axis=0)

# Removendo colunas que contêm qualquer valor NaN
print("\nDataFrame após remover colunas com qualquer valor NaN:")
print(df.dropna(axis=1))

# Removendo colunas que têm pelo menos 2 valores NaN
print("\nDataFrame após remover colunas com pelo menos 2 valores NaN:")
print(df.dropna(axis=1, thresh=2))

# Preenchendo todos os valores NaN com 0
print("\nDataFrame após preencher todos os valores NaN com 0:")
print(df.fillna(0))

# Preenchendo todos os valores NaN com a string "Conteúdo"
print("\nDataFrame após preencher todos os valores NaN com 'Conteúdo':")
print(df.fillna("Conteúdo"))

# Calculando a média dos valores na coluna 'A'
media_a = df["A"].mean()
print(f"\nMédia dos valores na coluna 'A': {media_a}")

# Preenchendo os valores NaN na coluna 'A' com a média dos valores existentes nessa coluna
print("\nDataFrame após preencher valores NaN na coluna 'A' com a média:")
print(df["A"].fillna(value=media_a))

print("DataFrame original:")
print(df)

# Preenchendo valores NaN com o último valor válido anterior na mesma coluna
print("\nDataFrame após preencher valores NaN com o último valor válido (veja linha 1, coluna D):")
print(df.ffill())

# Preenchendo valores NaN com o próximo valor válido na mesma coluna
print("\nDataFrame após preencher valores NaN com o próximo valor válido (veja linha 1, coluna D):")
print(df.bfill())
