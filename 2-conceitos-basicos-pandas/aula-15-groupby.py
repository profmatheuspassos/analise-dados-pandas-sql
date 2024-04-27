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

# Agrupando os dados por 'Classe'
grupo = df.groupby("Classe")

# Calculando a soma dos valores de cada grupo; em dados não numéricos realiza concatenação
grupo.sum()

# Calculando a soma apenas dos valores numéricos, ignorando campos não numéricos
grupo.sum(numeric_only=True)

# Calculando a média apenas dos valores numéricos
grupo.mean(numeric_only=True)

# Encontrando o valor mínimo para cada classe, apenas dos valores numéricos
df.groupby("Classe").min(numeric_only=True)

# Encontrando o valor mínimo para cada classe, incluindo todos os tipos de dados
df.groupby("Classe").min()

# Encontrando o valor máximo para cada classe, apenas dos valores numéricos
df.groupby("Classe").max(numeric_only=True)

# Encontrando o valor máximo para cada classe, incluindo todos os tipos de dados
df.groupby("Classe").max()

# Criando uma cópia de df e armazenando em df2
df2 = df.copy()

# Atualizando a coluna 'Venda' de df2 com novos valores
df2["Venda"] = [150, 432, 190, 230, 410, 155]

# Concatenando df e df2
df3 = pd.concat([df, df2])

# Agrupando df3 por 'Classe' e 'Nome' e calculando a soma dos valores
result = df3.groupby(["Classe", "Nome"]).sum()

# Exibindo o resultado do agrupamento e soma
print(result)
