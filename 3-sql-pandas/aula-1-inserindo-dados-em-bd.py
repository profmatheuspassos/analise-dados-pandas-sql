# Importa os módulos necessários
from pathlib import Path
import sqlite3
import pandas as pd

# Define o caminho da pasta onde o script está localizado
caminhoPasta = Path(__file__).parent
# Define o caminho para o arquivo CSV, subindo um nível na estrutura de diretórios e acessando a pasta 'arquivos'
caminhoArquivoOriginal = caminhoPasta.parents[0] / "arquivos" / "bd_data.csv"
# Define o caminho para o arquivo de banco de dados SQLite, similarmente ao caminho do arquivo CSV
caminhoArquivoBD = caminhoPasta.parents[0] / "arquivos" / "web.db"

# Estabelece uma conexão com o banco de dados SQLite
conexao = sqlite3.connect(str(caminhoArquivoBD))

# Carrega os dados do arquivo CSV para um DataFrame do Pandas
dfData = pd.read_csv(str(caminhoArquivoOriginal), index_col=0)

# Define o nome para o índice do DataFrame
dfData.index.name = "index_name"

# Imprime o DataFrame
print(dfData)

# Insere o DataFrame na tabela 'data' do banco de dados SQLite, definindo 'index_name' como a label do índice
dfData.to_sql("data", conexao, index_label="index_name")
