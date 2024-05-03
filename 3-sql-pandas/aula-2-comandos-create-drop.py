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
