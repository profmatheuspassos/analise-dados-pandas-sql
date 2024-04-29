import pandas as pd
from pathlib import Path

# Definindo o caminho da pasta atual e preparando o caminho para o arquivo de exemplo
caminhoPasta = Path(__file__).parent
caminhoArquivo = caminhoPasta.parents[0] / "arquivos" / "exemplo.csv"

# Carregando um arquivo CSV com separador ";" e ponto como separador decimal
df1 = pd.read_csv(caminhoArquivo, sep=";", decimal=".")
print("DataFrame carregado com separador ';' e ponto decimal:")
print(df1)

# Carregando um arquivo CSV com separador "," e ponto como separador decimal
df1 = pd.read_csv(caminhoArquivo, sep=",", decimal=".")
print("\nDataFrame carregado com separador ',' e ponto decimal:")
print(df1)

# Exibindo informações do DataFrame
print("\nInformações do DataFrame:")
df1.info()

# Salvando o DataFrame em um novo arquivo CSV com separador ";" e vírgula como separador decimal
caminhoNovoArquivo = caminhoPasta.parents[0] / "arquivos" / "exemplo2.csv"
df1.to_csv(caminhoNovoArquivo, sep=";", decimal=",")
print(f"\nDataFrame salvo em '{caminhoNovoArquivo}'.")

# Carregando dados de uma tabela HTML de um website
df = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')
print("\nDataFrame carregado a partir de uma página HTML:")
print(df)

# Exibindo a primeira tabela extraída
print("\nPrimeira tabela extraída do HTML:")
print(df[0])

# O comando pd.read_clipboard() foi comentado, pois requer uma interação especial não executável em um script tradicional.
# Se estiver executando este código num ambiente onde o clipboard (área de transferência) possa ser acessado, você pode descomentar a linha abaixo.
df = pd.read_clipboard()
print("\nDataFrame carregado a partir da área de transferência:")
print(df)

