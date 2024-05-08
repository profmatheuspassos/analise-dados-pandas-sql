# Importar bibliotecas necessárias
import pandas as pd
from pathlib import Path

# Definir o caminho absoluto até a pasta onde os arquivos CSV estão localizados
pastaArquivos = Path("/Users/matheuspassossilva/Library/CloudStorage/Dropbox/GitHub/analise-dados-pandas-sql/arquivos")

# Definir os caminhos para os arquivos CSV
arquivoGasolina2000 = pastaArquivos / "gasolina_2000+.csv"
arquivoGasolina2010 = pastaArquivos / "gasolina_2010+.csv"

# Carregar os conjuntos de dados em dois DataFrames separados
dfGasolina2000 = pd.read_csv(arquivoGasolina2000, low_memory=False)
dfGasolina2010 = pd.read_csv(arquivoGasolina2010, low_memory=False)

# Combinar os dois DataFrames em um único DataFrame
dfCombinado = pd.concat([dfGasolina2000, dfGasolina2010], ignore_index=True)

# Imprimir as primeiras e últimas entradas do DataFrame combinado para verificar
print(f"Primeiras entradas:\n{dfCombinado.head()}")
print(f"Últimas entradas:\n{dfCombinado.tail()}\n")

# Imprimir informações sobre o DataFrame para entender sua estrutura
print(f"Informações sobre o DataFrame para entender sua estrutura: {dfCombinado.info()}\n")

# Imprimir as colunas do DataFrame
print(f"Colunas do DataFrame:\n{dfCombinado.columns}\n")

# Verificar o tipo de dado da terceira entrada das colunas DATA INICIAL e DATA FINAL
print(f"Tipo da terceira entrada de DATA INICIAL: {type(dfCombinado['DATA INICIAL'][2])}")
print(f"Tipo da terceira entrada de DATA FINAL: {type(dfCombinado['DATA FINAL'][2])}\n")

# Converter as colunas DATA INICIAL e DATA FINAL para o tipo datetime
dfCombinado[["DATA FINAL", "DATA INICIAL"]] = dfCombinado[["DATA FINAL", "DATA INICIAL"]].apply(lambda x: pd.to_datetime(x, format="%Y-%m-%d"))

# Criar uma nova coluna ANO_MES com o ano e mês da DATA FINAL
dfCombinado['ANO_MES'] = dfCombinado['DATA FINAL'].dt.to_period('M')

# Listar todos os tipos de produtos contidos na base de dados
print(f"Tipos de produtos:\n{dfCombinado['PRODUTO'].value_counts()}\n")

# Filtrar o DataFrame para obter apenas dados da 'GASOLINA COMUM'
dfGasolinaComum = dfCombinado[dfCombinado['PRODUTO'] == 'GASOLINA COMUM']

# Calcular e imprimir o preço médio de revenda da gasolina em agosto de 2008
preco_medio_2008 = dfGasolinaComum[dfGasolinaComum["ANO_MES"] == "2008-08"]["PREÇO MÉDIO REVENDA"].mean()
print(f"Preço médio de revenda da gasolina em agosto de 2008: {preco_medio_2008}\n")

# Calcular e imprimir o preço médio de revenda da gasolina em maio de 2014 em São Paulo
preco_medio_sp_2014 = dfGasolinaComum[(dfGasolinaComum["ESTADO"] == "SAO PAULO") & (dfGasolinaComum["ANO_MES"] == "2014-05")]["PREÇO MÉDIO REVENDA"].mean()
print(f"Preço médio de revenda da gasolina em maio de 2014 em São Paulo: {preco_medio_sp_2014}\n")

# Obter dados onde o preço máximo de revenda da gasolina ultrapassou R$ 5,00
dfAcimaDeCinco = dfGasolinaComum[dfGasolinaComum["PREÇO MÁXIMO REVENDA"] > 5]
resultado = dfAcimaDeCinco[["DATA INICIAL", "ESTADO", "PREÇO MÁXIMO REVENDA"]]
print(f"Estados e datas onde o preço máximo da gasolina ultrapassou R$ 5,00:\n{resultado}\n")

# Calcular e imprimir a média de preço dos estados da região Sul em 2012
media_preco_sul_2012 = dfCombinado[(dfCombinado["REGIÃO"] == "SUL") & (dfCombinado["ANO_MES"].dt.strftime('%Y') == "2012")][["PREÇO MÉDIO REVENDA", "ESTADO"]].groupby(["ESTADO"]).mean()
print(f"Média de preço dos estados da região Sul em 2012:\n{media_preco_sul_2012}\n")
