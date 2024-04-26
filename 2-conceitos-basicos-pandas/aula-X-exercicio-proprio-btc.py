import pandas as pd
from pathlib import Path

print("\nAbrindo arquivo na pasta arquivos/btc.csv...")
caminhoPasta = Path(__file__).parent
caminhoArquivo = caminhoPasta.parents[0] / "arquivos" / "btc.csv"

print("\nLendo arquivom com \"pd.read_csv(caminhoArquivo)\"")
dfData = pd.read_csv(caminhoArquivo)

print("\nInício do arquivo")
print(dfData.head())

print("\nTransformando em um dataframe...")
df = pd.DataFrame(dfData)

print("\nDataframe completo")
print(df)

print("\nMostrando as colunas do dataframe")
print(df.columns)

print("\nColuna 'Open'")
print(df["Open"])

print("\nColuna 'Open' como dataframe")
print(df[["Open"]])

print("\nVariação diária: df[\"Close\"] - df[\"Open\"]")
print(df["Close"] - df["Open"])

print("\nCriando um novo dataframe com o conteúdo da linha 4994 e da coluna 3 - 'Low'...")
resultado_df = pd.DataFrame({
    'Valor': [df.iloc[4993, 3]],
    'Nome da Linha': [df.index[4993]],
    'Nome da Coluna': [df.columns[3]]
})

print("\nResultado")
print(resultado_df)