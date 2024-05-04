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

# SELECT NO SQL

# Cria um objeto cursor que permite executar comandos SQL no banco de dados
c = conexao.cursor()

# Executa uma consulta SQL para selecionar todos os registros da tabela 'data'
c.execute("SELECT * FROM data")

# Imprime o primeiro registro da consulta
print("Imprime o primeiro registro da consulta")
print(c.fetchone())

# Imprime todos os registros restantes da consulta
print("Imprime todos os registros restantes da consulta")
print(c.fetchall())

# Tenta criar um DataFrame a partir dos resultados restantes da consulta
# Nota: Isto não é uma boa prática porque os nomes das colunas tornam-se aleatórias
print("Tenta criar um DataFrame a partir dos resultados restantes da consulta")
df = pd.DataFrame(c.fetchall())
print(df)

# Executa uma consulta SQL para selecionar registros onde a coluna A é maior que 200
print("Executa uma consulta SQL para selecionar registros onde a coluna A é maior que 200")
c.execute("SELECT * FROM data WHERE A > 200")

# Cria um DataFrame a partir dos resultados da consulta e o imprime
print("Cria um DataFrame a partir dos resultados da consulta")
df = pd.DataFrame(c.fetchall())
print(df)

# Executa uma consulta SQL com uma condição mais específica, selecionando registros onde A > 200 e B > 100
print("Executa uma consulta SQL com uma condição mais específica, selecionando registros onde A > 200 e B > 100")
c.execute("SELECT * FROM data WHERE A > 200 AND B > 100")

# Cria um DataFrame a partir dos resultados e o imprime
print("Cria um DataFrame a partir dos resultados da consulta")
df = pd.DataFrame(c.fetchall())
print(df)

# Executa uma consulta SQL para selecionar apenas as colunas A, B, e C com condições específicas
print("Executa uma consulta SQL para selecionar apenas as colunas A, B, e C com condições específicas")
c.execute("SELECT A, B, C FROM data WHERE A > 200 AND B > 100")

# Cria um DataFrame a partir dos resultados e o imprime
print("Cria um DataFrame a partir dos resultados da consulta")
df = pd.DataFrame(c.fetchall())
print(df)

# Armazena uma consulta SQL em uma variável
pesquisa = "SELECT * FROM data"

# Executa a consulta armazenada e cria um DataFrame diretamente utilizando a função read_sql do pandas
print("Executa a consulta armazenada e cria um DataFrame diretamente utilizando a função read_sql do pandas")
df = pd.read_sql(pesquisa, con=conexao)
print(df)

# Executa a mesma consulta, mas especifica 'index_name' como a coluna índice do DataFrame
print("Executa a mesma consulta, mas especifica 'index_name' como a coluna índice do DataFrame")
df = pd.read_sql(pesquisa, con=conexao, index_col="index_name")
print(df)

# Executa uma consulta SQL mais complexa e diretamente cria um DataFrame especificando colunas
print("Executa uma consulta SQL mais complexa e diretamente cria um DataFrame especificando colunas")
df = pd.read_sql("SELECT A, B, C FROM data WHERE A > 200 AND B > 100", con=conexao)
print(df)
