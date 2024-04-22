from pathlib import Path
import pandas as pd

caminhoPasta = Path(__file__).parent
caminhoArquivo = caminhoPasta.parents[0] / "arquivos" / "supermarket_sales.csv"

dfData = pd.read_csv(caminhoArquivo)
print(dfData.head())

print("Faturamento por filial")
print(dfData.groupby("City")[["Total", "gross income"]].sum())

print("\n")

print("Percentual de participação na receita de cada tipo de produto")
print((dfData.groupby("Product line")["Total"].sum() / dfData.groupby("Product line")["Total"].sum().sum()).sort_values() * 100)

print("\n")

print("Distribuição do tipo de produto consumido por gênero")
print(dfData.groupby(["Product line", "Gender"])[["Total"]].sum().pivot_table(index="Product line", columns="Gender"))

print("\n")

print("Faturamento por mês")
dfData["Date"] = pd.to_datetime(dfData["Date"])
dfData["Month"] = dfData["Date"].apply(lambda x: x.month)
dfData["Year"] = dfData["Date"].apply(lambda x: x.year)
print(dfData.groupby(["Month"])["Total"].sum())

print("\n")

print("Média de avaliação por cada filial em janeiro de 2019")
print(dfData[(dfData["Year"] == 2019) & (dfData["Month"] == 1)]["Rating"].mean())


print("\n")

print("Como se distribui o gasto por tipo de consumidor em cada filial")
print(dfData.groupby(["Customer type", "City"])["Total"].sum())