import pandas as pd
from Transform import tempo_voo_horas, turno_partida

# Carregar os dados do dataset
df = pd.read_csv(
    "https://raw.githubusercontent.com/JackyP/testing/master/datasets/nycflights.csv",
    index_col=0
)

# Filtrar colunas necessárias
df = df[['year', 'month', 'day', 'hour', 'minute', 'arr_delay', 'carrier', 'flight', 'air_time', 'distance', 'origin', 'dest']]

# Remover valores NaN e filtrar voos com tempo válido
df = df.dropna()
df = df[df['air_time'] > 0]

# Aplicar transformações
df = tempo_voo_horas(df, 'air_time')
df = turno_partida(df, 'hour', 'minute')

# Exibir as primeiras linhas para conferência
print(df.head())

# Salvar o resultado final em CSV
df.to_csv("voos_transformados.csv", index=False)
print("Arquivo 'voos_transformados.csv' salvo com sucesso!")
