# Importa os módulos necessários
from pathlib import Path
import sqlite3
import pandas as pd

# COM PANDAS

# Define o caminho da pasta onde o script está localizado
caminhoPasta = Path(__file__).parent
# Define o caminho para o arquivo CSV, subindo um nível na estrutura de diretórios e acessando a pasta 'arquivos'
caminhoArquivoOriginal = caminhoPasta.parents[0] / "arquivos" / "bd_data.csv"
# Define o caminho para o arquivo de banco de dados SQLite, similarmente ao caminho do arquivo CSV
caminhoArquivoBD = caminhoPasta.parents[0] / "arquivos" / "web.db"

# Estabelece uma conexão com o banco de dados SQLite
conexao = sqlite3.connect(str(caminhoArquivoBD))

# UPDATE E DELETE NO SQL

# Cria um objeto cursor que permite executar comandos SQL no banco de dados
c = conexao.cursor()

# Atualiza o valor da coluna A para 218 onde o index_name é 'b'
print("Atualizando o valor da coluna A para 218 onde o index_name é 'b'")
c.execute("UPDATE data SET A = 218 WHERE index_name = 'b'")

# Confirma as alterações na base de dados
print("Confirma as alterações no banco de dados")
conexao.commit()

# Atualiza os valores das colunas A e B para 220 e 228, respectivamente, onde o index_name é 'b'
print("Atualizando os valores das colunas A e B para 220 e 228, respectivamente, onde o index_name é 'b'")
c.execute("UPDATE data SET A = 220, B = 228 WHERE index_name = 'b'")

# Confirma as alterações na base de dados
print("Confirma as alterações no banco de dados")
conexao.commit()

# Deleta o registro da tabela 'data' onde o index_name é igual a 1
print("Deletando o registro da tabela 'data' onde o index_name é igual a 1")
c.execute("DELETE FROM data WHERE index_name = 1")

# Confirma as alterações na base de dados
print("Confirma as alterações no banco de dados")
conexao.commit()