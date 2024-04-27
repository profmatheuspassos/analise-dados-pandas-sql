import pandas as pd
import numpy as np

# Definindo dados iniciais com três colunas: Classe, Nome e Venda
data = {
    'Classe': ['Júnior', 'Júnior', 'Pleno', 'Pleno', 'Sênior', 'Sênior'],
    'Nome': ['Jorge', 'Carlos', 'Roberta', 'Patrícia', 'Bruno', 'Vera'],
    'Venda': [200, 120, 340, 124, 243, 350]
}

# Criando um DataFrame a partir dos dados fornecidos
df = pd.DataFrame(data)
print("DataFrame original:")
print(df)

# Agrupando os dados por 'Classe'
grupo = df.groupby("Classe")

# Calculando a soma dos valores de cada grupo; em dados não numéricos realiza concatenação
print("\nSoma dos valores por classe (concatenação nos dados não numéricos):")
print(grupo.sum())

# Calculando a soma apenas dos valores numéricos, ignorando campos não numéricos
print("\nSoma apenas dos valores numéricos por classe:")
print(grupo.sum(numeric_only=True))

# Calculando a média apenas dos valores numéricos
print("\nMédia dos valores numéricos por classe:")
print(grupo.mean(numeric_only=True))

# Encontrando o valor mínimo para cada classe, apenas dos valores numéricos
print("\nValor mínimo apenas dos valores numéricos por classe:")
print(df.groupby("Classe").min(numeric_only=True))

# Encontrando o valor mínimo para cada classe, incluindo todos os tipos de dados
print("\nValor mínimo para cada classe (inclui todos os tipos de dados):")
print(df.groupby("Classe").min())

# Encontrando o valor máximo para cada classe, apenas dos valores numéricos
print("\nValor máximo apenas dos valores numéricos por classe:")
print(df.groupby("Classe").max(numeric_only=True))

# Encontrando o valor máximo para cada classe, incluindo todos os tipos de dados
print("\nValor máximo para cada classe (inclui todos os tipos de dados):")
print(df.groupby("Classe").max())

# Criando uma cópia de df e armazenando em df2
df2 = df.copy()
df2["Venda"] = [150, 432, 190, 230, 410, 155]
print("\nDataFrame modificado (df2):")
print(df2)

# Concatenando df e df2
df3 = pd.concat([df, df2])
print("\nDataFrame resultante após concatenação de df e df2:")
print(df3)

# Agrupando df3 por 'Classe' e 'Nome' e calculando a soma dos valores
print("\nResultado após agrupar por 'Classe' e 'Nome' e calcular a soma dos valores:")
print(df3.groupby(["Classe", "Nome"]).sum())
