# %%
import pandas as pd
import numpy as np

# %%
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside, inside))

# %%
hier_index

# %%
hier_index = pd.MultiIndex.from_tuples(hier_index)

# %%
hier_index

# %%
df = pd.DataFrame(np.random.randn(6,2), index=hier_index,columns=['A', 'B'])

# %%
df

# %%
df.loc["G1"]

# %%
df.loc["G1"].loc[1]

# %%
df.index.names = ["Grupo", "Número"]

# %%
df

# %%
df.xs("G1")

# %%
df.xs(1, level = "Número")

# %%
df.xs(2, level = "Número")


