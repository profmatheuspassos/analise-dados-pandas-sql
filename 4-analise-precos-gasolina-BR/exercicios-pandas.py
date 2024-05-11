"""
- CONVERTIDO DO JUPYTER USANDO CHATGPT
- INCLUÍDA A OPÇÃO DE SALVAR O RESULTADO EM UM ARQUIVO TXT
"""

import pandas as pd
from pathlib import Path

# Definindo o caminho absoluto para a pasta onde os arquivos estão localizados
pastaArquivos = Path("/Users/matheuspassossilva/Library/CloudStorage/Dropbox/GitHub/analise-dados-pandas-sql/arquivos")

# Caminhos para os arquivos CSV
arquivoGasolina2000 = pastaArquivos / "gasolina_2000+.csv"
arquivoGasolina2010 = pastaArquivos / "gasolina_2010+.csv"

# Definindo o caminho para o arquivo de saída dos resultados
arquivoResultados = pastaArquivos / "resultados-exercicios-pandas.py"

# Abrindo o arquivo de resultados para escrita
with open(arquivoResultados, "w") as file:

    # Carregando os arquivos CSV em DataFrames
    dfGasolina2000 = pd.read_csv(arquivoGasolina2000, index_col=0, low_memory=False)
    dfGasolina2010 = pd.read_csv(arquivoGasolina2010, index_col=0, low_memory=False)

    # Combinando ambos os DataFrames em um único DataFrame
    dfCombinado = pd.concat([dfGasolina2000, dfGasolina2010], ignore_index=True)

    # Convertendo as colunas DATA INICIAL e DATA FINAL para o formato de data
    dfCombinado[["DATA FINAL", "DATA INICIAL"]] = dfCombinado[["DATA FINAL", "DATA INICIAL"]].apply(pd.to_datetime)

    # Criando uma nova coluna para representar o ano e o mês (aaaa-mm)
    dfCombinado['ANO_MES'] = dfCombinado['DATA FINAL'].dt.to_period('M')

    # Filtrando o DataFrame para obter apenas dados de 'GASOLINA COMUM'
    dfGasolinaComum = dfCombinado[dfCombinado['PRODUTO'] == 'GASOLINA COMUM']

    # Calculando o preço médio de revenda da gasolina em agosto de 2008
    preco_medio_ago2008 = dfGasolinaComum[dfGasolinaComum["ANO_MES"] == "2008-08"]["PREÇO MÉDIO REVENDA"].mean()
    resultado_ago2008 = f"Preço médio de revenda da gasolina em agosto de 2008: R$ {preco_medio_ago2008:.2f}\n\n\n\n"
    print(resultado_ago2008)
    file.write(resultado_ago2008)

    # Calculando o preço médio de revenda da gasolina em maio de 2014 em São Paulo
    preco_medio_mai2014_sp = dfGasolinaComum[(dfGasolinaComum["ESTADO"] == "SAO PAULO") & (dfGasolinaComum["ANO_MES"] == "2014-05")]["PREÇO MÉDIO REVENDA"].mean()
    resultado_mai2014_sp = f"Preço médio de revenda da gasolina em maio de 2014 em São Paulo: R$ {preco_medio_mai2014_sp:.2f}\n\n\n\n"
    print(resultado_mai2014_sp)
    file.write(resultado_mai2014_sp)

    # Determinando em que estado e quando a gasolina ultrapassou a barreira dos R$ 5,00
    dfAcimaDeCinco = dfGasolinaComum[dfGasolinaComum["PREÇO MÁXIMO REVENDA"] > 5]
    resultado = dfAcimaDeCinco[["ANO_MES", "ESTADO", "PREÇO MÁXIMO REVENDA"]]
    print("Estados e meses em que o preço da gasolina ultrapassou R$ 5,00:")
    print(resultado.drop_duplicates())
    file.write("Estados e meses em que o preço da gasolina ultrapassou R$ 5,00:\n")
    file.write(resultado.drop_duplicates().to_string() + "\n\n\n\n")

    # Calculando a média de preço dos estados da região Sul em 2012
    preco_medio_sul_2012 = dfGasolinaComum[(dfGasolinaComum["REGIÃO"] == "SUL") & (dfGasolinaComum["ANO_MES"].dt.strftime('%Y') == "2012")]["PREÇO MÉDIO REVENDA"].mean()
    resultado_sul_2012 = f"Média de preço da gasolina na região Sul em 2012: R$ {preco_medio_sul_2012:.2f}\n\n\n\n"
    print(resultado_sul_2012)
    file.write(resultado_sul_2012)

    # Criando uma tabela com a variação percentual ano a ano para o estado do Rio de Janeiro
    dfGasolinaComum["MES"] = dfGasolinaComum["DATA FINAL"].apply(lambda x: x.month)
    dfRio = dfGasolinaComum[dfGasolinaComum["ESTADO"] == "RIO DE JANEIRO"]
    dfMesRio = dfRio.groupby("ANO_MES")[["PREÇO MÉDIO REVENDA", "MES"]].last()
    var_ano_rio = (dfMesRio[dfMesRio["MES"] == 12] / dfMesRio[dfMesRio["MES"] == 12].shift(1) - 1) * 100
    print("Variação percentual anual para o estado do Rio de Janeiro:")
    print(var_ano_rio.dropna())
    file.write("Variação percentual anual para o estado do Rio de Janeiro:\n")
    file.write(var_ano_rio.dropna().to_string() + "\n\n\n\n")

    # Desafio: Criando uma tabela com a diferença absoluta e percentual entre os preços mais baratos e caros, incluindo estados
    dfMax = dfGasolinaComum.groupby("ANO_MES").max()["PREÇO MÉDIO REVENDA"]
    dfMin = dfGasolinaComum.groupby("ANO_MES").min()["PREÇO MÉDIO REVENDA"]
    dfDiff = pd.DataFrame()
    dfDiff["ABS_DIFF"] = dfMax - dfMin
    dfDiff["PERCENT_DIFF"] = (dfMax - dfMin) / dfMin * 100
    dfDiff["MAX"] = dfMax
    dfDiff["MIN"] = dfMin

    idxMax = dfGasolinaComum.groupby("ANO_MES")["PREÇO MÉDIO REVENDA"].idxmax()
    idxMin = dfGasolinaComum.groupby("ANO_MES")["PREÇO MÉDIO REVENDA"].idxmin()
    dfDiff["ESTADO_MAX"] = dfGasolinaComum.loc[idxMax, :]["ESTADO"].values
    dfDiff["ESTADO_MIN"] = dfGasolinaComum.loc[idxMin, :]["ESTADO"].values

    print("Diferença absoluta e percentual entre os preços mais caros e baratos, por estado:")
    print(dfDiff)
    file.write("Diferença absoluta e percentual entre os preços mais caros e baratos, por estado:\n")
    file.write(dfDiff.to_string() + "\n")

# Encerrando o bloco with para garantir que o arquivo seja fechado corretamente
