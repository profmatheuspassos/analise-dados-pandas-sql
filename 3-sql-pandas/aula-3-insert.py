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

# Carrega os dados do arquivo CSV para um DataFrame do Pandas
dfData = pd.read_csv(str(caminhoArquivoOriginal), index_col=0)

# Define o nome para o índice do DataFrame
dfData.index.name = "index_name"

# Insere o DataFrame na tabela 'data' do banco de dados SQLite, definindo 'index_name' como a label do índice
dfData.to_sql("data", conexao, index_label="index_name")

# COM SQL

# Cria um objeto cursor que permite executar comandos SQL no banco de dados
c = conexao.cursor()

# Executa um comando SQL para criar uma tabela chamada 'produtos' com três colunas
c.execute("CREATE TABLE produtos (produto_ID, produto_nome, preco)")

# Confirma (commit) a transação para garantir que a criação da tabela seja efetivada no banco de dados
conexao.commit()

# Executa um comando SQL para deletar (drop) a tabela 'produtos' caso ela exista
c.execute("DROP TABLE produtos")

# Cria novamente a tabela 'produtos' com especificações mais detalhadas para cada coluna
# 'produto_ID' é definido como chave primária e inteiro
# 'produto_nome' é definido como texto
# 'preco' é definido como inteiro
c.execute("CREATE TABLE produtos ([produto_ID] INTEGER PRIMARY KEY, [produto_nome] TEXT, [preco] INTEGER)")

# Insere dados na tabela 'produtos' utilizando um comando SQL
c.execute("""INSERT INTO produtos (produto_ID, produto_nome, preco)
          VALUES
          (1, "Computador", 800),   # Insere um produto com ID 1, nome "Computador" e preço 800
          (2, "Impressora", 200),   # Insere um produto com ID 2, nome "Impressora" e preço 200
          (3, "Tablet", 300)        # Insere um produto com ID 3, nome "Tablet" e preço 300
          """)

# Confirma as alterações na base de dados
conexao.commit()

# NOVAMENTE COM PANDAS - INSERINDO VALORES NA TABELA JÁ EXISTENTE

# Seleciona linhas do DataFrame dfData em passos de 2 em ordem inversa
dfData2 = dfData.iloc[::-2]

# Insere o DataFrame dfData2 na tabela 'data' do banco de dados, anexando os dados aos já existentes
dfData2.to_sql("data", conexao, if_exists="append")
