import pandas as pd

df = pd.DataFrame({'col1': [1,2,3,4], 'col2':[444, 555, 666, 444], 'col3':['abc', 'def', 'ghi', 'xyz']})

print("DataFrame original:")
print(df)

print("\nPrimeiras linhas do DataFrame:")
print(df.head())

print("\nInformações do DataFrame:")
df.info()

print("\nUso de memória de cada coluna do DataFrame:")
print(df.memory_usage())

print("\nValores únicos na coluna 'col2':")
print(df["col2"].unique())

print("\nContagem de valores únicos na coluna 'col2':")
print(df["col2"].value_counts())

def comp(x):
    return x ** 2 + 3

print("\nColuna 'col1' após aplicação da função comp:")
print(df["col1"].apply(comp))

df["col1_calc"] = df["col1"].apply(comp)
print("\nDataFrame após adicionar a coluna 'col1_calc':")
print(df)

print("\nResultados de aplicar uma expressão lambda à coluna 'col1':")
print(df["col1"].apply(lambda x: x ** 2 + 3))

print("\nSoma dos valores da coluna 'col1':", df["col1"].sum())
print("Média dos valores da coluna 'col1':", df["col1"].mean())
print("Produto dos valores da coluna 'col1':", df["col1"].product())
print("Desvio padrão dos valores da coluna 'col1':", df["col1"].std())
print("Valor máximo da coluna 'col1':", df["col1"].max())
print("Valor mínimo da coluna 'col1':", df["col1"].min())
print("Índice do valor máximo da coluna 'col1':", df["col1"].idxmax())
print("Índice do valor mínimo da coluna 'col1':", df["col1"].idxmin())

print("\nLinhas do DataFrame onde 'col2' é 444:")
print(df[df["col2"] == 444])

print("\nSoma das linhas do DataFrame onde 'col2' é 444:")
print(df[df["col2"] == 444].sum())

print("\nDataFrame ordenado pela coluna 'col2':")
print(df.sort_values(by="col2"))

data = {'A':['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
        'B':['one', 'one', 'two', 'two', 'one', 'one'],
        'C': ['x', 'y', 'x', 'y', 'x', 'y'],
        'D':[1,3,2,5,4,1]
        }

df = pd.DataFrame(data)

print("\nNovo DataFrame:")
print(df)

dict_map = {"one": "1", "two": "2"}

print("\nMapping de valores na coluna 'B' com dict_map:")
print(df["B"].map(dict_map))

df["E"] = df["B"].map(dict_map)
print("\nDataFrame após adicionar a coluna 'E':")
print(df)

print("\nPivot table do DataFrame:")
print(df.pivot_table(index="A", columns="B", values="D"))
