import pandas as pd
import datetime

numero_de_dias = 100
datas = pd.date_range(start='1/1/2021', periods=numero_de_dias) # Cria valores espaçados no tempo

print("Datas geradas:")
print(datas)

df = pd.DataFrame(range(numero_de_dias), columns=["number"], index=datas)
print("\nDataFrame criado com datas como índice:")
print(df)

print("\nÍndice do DataFrame:")
print(df.index)

print("\nPrimeiro índice do DataFrame:")
print(df.index[0])

print("\nDia do primeiro índice:")
print(df.index[0].day)

print("\nMês do primeiro índice:")
print(df.index[0].month)

print("\nAno do primeiro índice:")
print(df.index[0].year)

print("\nHora do primeiro índice (sempre zero, pois as datas não têm hora específica):")
print(df.index[0].hour)

print("\nLinhas do DataFrame onde o mês do índice é janeiro:")
print(df[df.index.month == 1])

print("\nLinhas do DataFrame onde o dia do índice é 10:")
print(df[df.index.day == 10])

df["Month"] = df.index.month
print("\nDataFrame após adicionar uma coluna com o mês do índice:")
print(df)

print("\nLinhas do DataFrame após '2021-03-10':")
print(df[df.index > datetime.datetime(2021, 3, 10)])
