import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(5, 4), index = ["A", "B", "C", "D", "E"], columns = "W X Y Z".split())
print('Dataframe criado: pd.DataFrame(randn(5, 4), index = ["A", "B", "C", "D", "E"], columns = "W X Y Z".split())')
print("\nDataframe")
print(df)
print("\nAcessando coluna W")
print(df["W"])
print("\nAcessando coluna W com formatação")
print(df[["W"]])
print("\nCriando nova coluna 'new' e igualando à coluna 'W'")
df["new"] = df["W"]
print(df["new"])
print("\nColuna 'new' sendo igual ao somatório da coluna 'W' com a coluna 'Y' - equivale a uma Series")
df["new"] = df["W"] + df["Y"]
print(df["new"])
print("\nUsando método drop - apenas 'esconde' a coluna 'new'")
df.drop("new", axis = 1)
print(df)
print("\nCriando um novo dataframe (df2) sem a coluna 'new'")
df2 = df.drop("new", axis = 1)
print(df2)
print("\nRemovendo a coluna 'new' com o argumento 'inplace'")
df.drop("new", axis = 1, inplace = True)
print(df)
print("\nUsando o método loc para obter o conteúdo da linha 'A'")
print(df.loc["A"])
print("\nUsando o método loc para obter o conteúdo da linha 'A' e 'B'")
print(df.loc[["A", "B"]])
print("\nUsando o método iloc para acessar a linha 'A' e a coluna 'Y' - 0, 2")
print(df.iloc[0, 2])