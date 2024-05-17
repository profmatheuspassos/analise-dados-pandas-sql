import os
import pandas as pd

# Definindo o caminho do arquivo relativo ao diretório onde o script está localizado
script_dir = os.path.dirname(__file__)  # Diretório onde o script está localizado
file_path = os.path.join(script_dir, 'AB_NYC_2019.csv')

# Carregando o dataset do Airbnb
df = pd.read_csv(file_path)

# Exibindo as três primeiras linhas do dataframe
print(f"Primeiras três linhas do dataframe:\n{df.head(3)}\n")

# Configurando a coluna 'id' como índice do dataframe
df2 = df.set_index("id")

# Exibindo as três primeiras linhas do novo dataframe com 'id' como índice
print(f"Primeiras três linhas do dataframe com 'id' como índice:\n{df2.head(3)}\n")

# Acessando o valor da coluna 'name' para o índice 2539
name_2539 = df2.name[2539]
print(f"Nome do Airbnb com id 2539: {name_2539}\n")

# Acessando o valor da coluna 'host_name' para o índice 3647
host_name_3647 = df2.host_name[3647]
print(f"Nome do anfitrião com id 3647: {host_name_3647}\n")

# Exibindo informações sobre o dataframe
print(f"Informações do dataframe:\n{df2.info()}\n")

# Selecionando apenas colunas numéricas
df_numeric = df.select_dtypes(include='number')

# Adicionando a coluna 'room_type' de volta ao dataframe numérico
df_numeric['room_type'] = df['room_type']

# Agrupando por 'room_type' e calculando a média
df3 = df_numeric.groupby("room_type").mean()

# Exibindo as médias agrupadas por tipo de quarto
print(f"Médias agrupadas por tipo de quarto:\n{df3}\n")

# Exibindo os índices do dataframe agrupado
print(f"Índices do dataframe agrupado:\n{df3.index}\n")

# Redefinindo o índice do dataframe agrupado
df3_reset = df3.reset_index()
print(f"Dataframe agrupado com índice redefinido:\n{df3_reset}\n")

# Redefinindo o índice do dataframe agrupado, sem manter o índice antigo
df3_reset_drop = df3.reset_index(drop=True)
print(f"Dataframe agrupado com índice redefinido e sem manter o índice antigo:\n{df3_reset_drop}\n")

# Ordenando o dataframe agrupado pelo índice de forma decrescente
df3_sorted = df3.sort_index(ascending=False)
print(f"Dataframe agrupado ordenado pelo índice de forma decrescente:\n{df3_sorted}\n")

# Exibindo as três primeiras linhas do dataframe original
print(f"Primeiras três linhas do dataframe original:\n{df.head(3)}\n")

# Ordenando o dataframe original pelo nome do anfitrião
df_sorted_host_name = df.sort_values(["host_name"])
print(f"Dataframe original ordenado pelo nome do anfitrião:\n{df_sorted_host_name.head(3)}\n")

# Ordenando o dataframe original pelo grupo de bairro e pelo nome do anfitrião
df_sorted_neigh_host = df.sort_values(["neighbourhood_group", "host_name"])
print(f"Dataframe original ordenado pelo grupo de bairro e pelo nome do anfitrião:\n{df_sorted_neigh_host.head(3)}\n")

# Exibindo os grupos de bairro únicos
unique_neigh_groups = df.neighbourhood_group.unique()
print(f"Grupos de bairro únicos:\n{unique_neigh_groups}\n")

# Contando os valores únicos dos grupos de bairro
neigh_group_counts = df.neighbourhood_group.value_counts()
print(f"Contagem dos grupos de bairro:\n{neigh_group_counts}\n")

# Ordenando o dataframe original pelo grupo de bairro (decrescente) e pelo nome do anfitrião (crescente) e atualizando o dataframe original
df.sort_values(["neighbourhood_group", "host_name"], ascending=[False, True], inplace=True)
print(f"Dataframe original ordenado e atualizado:\n{df.head(3)}\n")

# Ordenando o dataframe original pelo preço de forma decrescente
dfp = df.sort_values("price", ascending=False)
print(f"Top 5 Airbnbs mais caros:\n{dfp[['id', 'host_name', 'price']].head(5)}\n")

# Adicionando a coluna 'price_rank' com o ranking dos preços
dfp["price_rank"] = dfp.price.rank(method="max", ascending=False)
print(f"Top 5 Airbnbs mais caros com ranking de preço:\n{dfp[['id', 'host_name', 'price', 'price_rank']].head(5)}\n")

# set_index: Define uma coluna do DataFrame como o índice.
# reset_index: Redefine o índice do DataFrame para o padrão numérico.
# sort_values: Ordena o DataFrame com base nos valores de uma ou mais colunas.
# sort_index: Ordena o DataFrame com base nos valores do índice.
# unique: Retorna os valores únicos de uma coluna.
# value_counts: Conta a frequência de valores únicos em uma coluna.
# rank: Atribui um ranking a cada valor em uma coluna, com base na ordem especificada.
