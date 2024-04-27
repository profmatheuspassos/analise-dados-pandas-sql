# %%
import pandas as pd
import numpy as np

# %%
data = {'Classe': ['Júnior', 'Júnior', 'Pleno', 'Pleno', 'Sênior', 'Sênior'], 'Nome': ['Jorge', 'Carlos', 'Roberta', 'Patrícia', 'Bruno', 'Vera'],
'Venda': [200, 120, 340, 124, 243, 350]}

# %%
data

# %%
df = pd.DataFrame(data)

# %%
df

# %%
df.groupby("Classe")

# %%
grupo = df.groupby("Classe")

# %%
grupo.sum() # Soma tudo - no caso de strings, ocorre concatenação

# %%
grupo.sum(numeric_only=True) # Ignora valores não numéricos

# %%
grupo.mean(numeric_only=True)

# %%
df.groupby("Classe").min(numeric_only=True)

# %%
df.groupby("Classe").min()

# %%
df.groupby("Classe").max(numeric_only=True)

# %%
df.groupby("Classe").max()

# %%
df

# %%
df2 = df.copy() # Cria uma cópia; se colocar apenas como "=" será criado um ponteiro

# %%
df2["Venda"] = [150, 432, 190, 230, 410, 155]

# %%
df

# %%
df2

# %%
df3 = pd.concat([df, df2])

# %%
df3

# %%
df3.groupby(["Classe", "Nome"]).sum()


print(df3.groupby(["Classe", "Nome"]).sum())