# %%
import pandas as pd
import numpy as np

# %%
df = pd.DataFrame({'A': [1,2,np.nan],
                   'B': [5,np.nan,np.nan],
                   'C': [1,2,3]}
                   )

# %%
df

# %%
df.dropna() # = df.dropna(axis=0) - remove a linha que contém valores NaN

# %%
df.dropna(axis=1) # Remove a coluna que contém valores NaN

# %%
df.dropna(axis=1, thresh=2) # Limite de números ausentes para descarte - no caso, se houver 2 ou mais valores NaN ele é removido

# %%
df.fillna(0) # Preenche os valores NaN com o que for inserido como parâmetro

# %%
df.fillna("Conteúdo")

# %%
df["A"].mean() # Calcula a média

# %%
df["A"].fillna(value=df["A"].mean())

# %%
df

# %%
df.ffill() # Preenche com o último valor encontrado - veja o original acima

# %%
df.bfill() # Contrário do anterior - pega o valor posterior e preenche o NaN - mas neste exemplo não vai funcionar bem


