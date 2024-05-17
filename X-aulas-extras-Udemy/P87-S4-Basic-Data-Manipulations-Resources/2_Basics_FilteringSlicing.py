import os
import pandas as pd
import numpy as np

# Definindo o caminho do arquivo relativo ao diretório onde o script está localizado
script_dir = os.path.dirname(__file__)  # Diretório onde o script está localizado
file_path = os.path.join(script_dir, 'AB_NYC_2019.csv')

# Carregando o dataset do Airbnb
df = pd.read_csv(file_path)

# Exibindo as duas primeiras linhas do DataFrame
print(f"Primeiras 2 linhas do DataFrame:\n{df.head(2)}\n")

# ## Slicing Columns
# Selecionando a coluna 'host_name' do DataFrame
host_name_col = df["host_name"]
print(f"Coluna 'host_name':\n{host_name_col}\n")

# Selecionando a coluna 'host_name' do DataFrame usando notação de ponto
host_name_col_dot = df.host_name
print(f"Coluna 'host_name' (notação ponto):\n{host_name_col_dot}\n")

# Selecionando múltiplas colunas do DataFrame
multiple_cols = df[["host_name", "neighbourhood_group"]]
print(f"Colunas 'host_name' e 'neighbourhood_group':\n{multiple_cols.head(2)}\n")

# ## Filtering on rows (mask filtering)
# Filtrando linhas onde o 'host_name' é "Taz"
taz_hosts = df[df.host_name == "Taz"]
print(f"Linhas onde 'host_name' é 'Taz':\n{taz_hosts}\n")

# Verificando a condição para cada linha
taz_condition = df.host_name == "Taz"
print(f"Condição 'host_name == Taz':\n{taz_condition}\n")

# Contando o número de ocorrências onde a condição é verdadeira
taz_count = (df.host_name == "Taz").sum()
print(f"Número de ocorrências de 'Taz': {taz_count}\n")

# Criando uma máscara para filtrar linhas onde 'host_name' é "Taz"
mask = df.host_name == "Taz"
filtered_taz = df[mask].head(2)
print(f"Primeiras 2 linhas com 'host_name' igual a 'Taz':\n{filtered_taz}\n")

# Filtrando linhas com preço menor que 100 e noites mínimas menor que 3
quick_and_cheap = (df.price < 100) & (df.minimum_nights < 3)
quick_and_cheap_count = quick_and_cheap.sum()
print(f"Número de registros rápidos e baratos: {quick_and_cheap_count}\n")

# Exibindo as primeiras 2 linhas que atendem aos critérios de 'quick_and_cheap'
quick_and_cheap_rows = df[quick_and_cheap].head(2)
print(f"Primeiras 2 linhas rápidas e baratas:\n{quick_and_cheap_rows}\n")

# Filtrando linhas onde 'reviews_per_month' > 3 ou 'number_of_reviews' > 50
reviews_consistent = df[(df.reviews_per_month > 3) | (df.number_of_reviews > 50)]
print(f"Linhas com reviews consistentes:\n{reviews_consistent.head(3)}\n")

# Criando uma máscara usando np.logical_or
mask_or = np.logical_or((df.reviews_per_month > 3), (df.number_of_reviews > 50))
filtered_or = df[mask_or].head(2)
print(f"Primeiras 2 linhas com máscara OR:\n{filtered_or}\n")

# Filtrando linhas onde a condição é negada (~mask_or)
filtered_not_or = df[~mask_or].head(2)
print(f"Primeiras 2 linhas com negação da máscara OR:\n{filtered_not_or}\n")

# ## Filtering columns and rows together
# Filtrando colunas e linhas usando .loc
loc_filtered = df.loc[mask_or, ["name", "host_name"]]
print(f"Colunas 'name' e 'host_name' para a máscara OR:\n{loc_filtered}\n")

# Usando .loc para filtrar todas as colunas baseadas na máscara
loc_filtered_all_cols = df.loc[mask_or, :].head()
print(f"Linhas completas filtradas com máscara OR:\n{loc_filtered_all_cols}\n")

# ## Filtering based on index
# Selecionando um valor específico usando iloc
specific_value = df.iloc[0, 1]
print(f"Valor específico usando iloc[0, 1]: {specific_value}\n")

# Definindo uma coluna como índice e acessando uma linha inteira
df2 = df.set_index("id")
row_by_index = df2.iloc[0, :]
print(f"Linha inteira pelo novo índice:\n{row_by_index}\n")

# Selecionando um intervalo de linhas e colunas usando iloc
range_selection = df2.iloc[1:4, 6:]
print(f"Seleção de intervalo usando iloc:\n{range_selection}\n")

# ## Provided mask helpers
# Usando .between para filtrar valores de uma coluna
between_filter = df.loc[df.price.between(100, 200), "price"]
print(f"Preços entre 100 e 200:\n{between_filter.head()}\n")

# Usando .isin para filtrar valores específicos de uma coluna
isin_filter = df.loc[df.price.isin([100, 200]), "price"]
print(f"Preços iguais a 100 ou 200:\n{isin_filter.head()}\n")

# Verificando se algum valor no DataFrame é "John"
is_john = df == "John"
print(f"DataFrame comparado com 'John':\n{is_john.head()}\n")

# Usando .any para verificar se qualquer valor é "John"
any_john = (df == "John").any()
print(f"Qualquer valor é 'John' (colunas):\n{any_john}\n")

# Usando .any no eixo 1 (linhas)
any_john_rows = (df == "John").any(axis=1)
print(f"Qualquer valor é 'John' (linhas):\n{any_john_rows.head()}\n")

# ## Views vs Copy
# Criando uma cópia do DataFrame
df2 = df.copy()

# Modificando uma célula na cópia (usando notação de ponto, pode gerar SettingWithCopyWarning)
df2["name"][0] = "TESTING"
print(f"Primeira linha após modificação direta:\n{df2.head(1)}\n")

# Modificando uma célula na cópia (usando .loc, maneira segura)
df2.loc[df2.index == 0, "name"] = "TESTING2"
print(f"Primeira linha após modificação com loc:\n{df2.head(1)}\n")

# Tentativa de modificação direta com filtro, pode não funcionar corretamente
df2[df2.host_name == "John"]["name"] = "Oh no"
print(f"Primeira linha após tentativa de modificação com filtro:\n{df2.head(1)}\n")

# ## Funções do pandas explicadas
# .loc: Seleciona dados com base em rótulos.
# .iloc: Seleciona dados com base em índices posicionais.
# .between: Filtra valores entre um intervalo especificado.
# .isin: Filtra valores que estão em uma lista de valores.
# .any: Retorna True se qualquer valor for verdadeiro ao longo de um eixo.
# .all: Retorna True se todos os valores forem verdadeiros ao longo de um eixo.
# .copy: Cria uma cópia do DataFrame.
# Boolean operators: & (e), | (ou), ^ (ou exclusivo), ~ (não).
# View vs copy: Views são referências a dados originais, enquanto cópias são duplicatas independentes dos dados.
