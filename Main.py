import pandas as pd
import logging
import datetime
import sqlite3
from Transform import tempo_voo_horas, turno_partida
from DataClean import data_clean

#ARQUIVO DE LOGS
logging.basicConfig(filename='Main.log', level=logging.INFO)
logger = logging.getLogger()

logger.info(f'Inicio da execucao ; {datetime.datetime.now()}')

#Executa DataClean
db_path = data_clean()

conn = sqlite3.connect(db_path)
df = pd.read_sql("SELECT * FROM DataClean", conn)

# REMOVE VALORES NULL
df = df.dropna()

#CHAMA A FUNÇÃO QUE CONVERTE O TEMPO DE VOO DE MINUTOS PARA HORAS
df = tempo_voo_horas(df, 'tempo_voo')

#CHAMA A FUNÇÃO QUE CLASSIFICA O PERIODO
df = turno_partida(df, 'data_hora')

#GRAVA O RESULTADO FINAL DA TABELA VoosTransformados do SQLITE
df.to_sql("VoosTransformados", conn, if_exists="replace", index=False)
df_vz = pd.read_sql("SELECT * FROM VoosTransformados", conn)
print(df_vz)
conn.close()

logger.info(f'Fim da execucao ; {datetime.datetime.now()}')