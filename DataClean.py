import pandas as pd
import datetime
import numpy as np
import re
import logging
import sqlite3

def data_clean():
    # Caminho do banco SQLite
    db_path = "nycflights.db"

    #FUNÇÃO PARA PADRONIZAR AS STRINGS
    def padroniza_str(obs):
        return re.sub('[^A-Za-z0-9]+', '', obs.upper())
    inicio = datetime.datetime.now()
    print(f"DataClean Iniciado: {inicio}")

    #LEITURA DO ARQUIVO COM OS DADOS DE ORIGEM
    df = pd.read_csv(
        "https://raw.githubusercontent.com/JackyP/testing/master/datasets/nycflights.csv",
        index_col=0
        )

    #COLUNAS QUE IREMOS UTILIZAR
    usecols=["year", "month",  "day", "hour", "minute","arr_delay","carrier","flight","air_time","distance", "origin", "dest"]

    #DADOS SELECIONADOS
    df_raw = df.loc[
    (~df["carrier"].isna()) \
    & (~df["flight"].isna()) \
    & (~df["year"].isna()) \
    & (~df["hour"].isna()) \
    & (~df["minute"].isna()) \
    & (~df["month"].isna()) \
    & (~df["day"].isna()) \
    & (df["air_time"] > 0)
].loc[:, usecols]

    #REMOVER LINHAS DUPLICADAS
    df_raw.drop_duplicates(inplace=True)

    #CONVERTER O DATAFRAME
    df_raw = df_raw.astype("object")

    #LÓGICA DE LIMPEZA DAS COLUNAS
    tmp = df.loc[:, usecols].copy()
    tmp = tmp[tmp["air_time"]>0]
    for col in ["carrier","flight", "year", "month", "day" ,"hour", "minute"]:
        tmp_df = tmp.loc[~df[col].isna()]
        tmp = tmp_df.copy()
    tmp.drop_duplicates(inplace=True)
    tmp.shape[0] == df_raw.shape[0]

    #CREATE COLUNA DATE_TIME
    df_raw["date_time"] =  pd.to_datetime(df_raw[["year", "month", "day", "hour", "minute"]],  dayfirst=True)

    #SELECIONAR COLUNAS QUE SERÃO UTILIZADAS
    usecols2 =["date_time", "arr_delay","carrier","flight","air_time","distance", "origin", "dest" ]

    #RENOMEAR COLUNAS
    new_columns = ["data_hora", "atraso_chegada", "companhia", "id_voo","tempo_voo", "distancia", "origem", "destino"]
    columns_map = {usecols2[i]: new_columns[i] for i in range(len(usecols2))}


    #COPIA DO DF E TRATAMENTO DF WORK
    df_work = df_raw.loc[:, usecols2].copy()
    df_work.rename(columns=columns_map, inplace=True)
    df_work.head()

    #CONVERSÃO DAS COLUNAS
    df_work["distancia"] = df_work.loc[:,"distancia"].astype(float)
    df_work["companhia"] = df_work.loc[:,"companhia"].astype(str)
    df_work["id_voo"] = df_work.loc[:,"id_voo"].astype(str)
    df_work["atraso_chegada"] = df_work.loc[:,"atraso_chegada"].astype(str)
    df_work["origem"] = df_work.loc[:,"origem"].astype(str)
    df_work["destino"] = df_work.loc[:,"destino"].astype(str)


    #TRATAMENTO DAS COLUNAS
    df_work["companhia"] = df_work.loc[:,"companhia"].apply(lambda x: padroniza_str(x))
    df_work["id_voo"] = df_work.loc[:,"id_voo"].apply(lambda x: padroniza_str(x))
    df_work["origem"] = df_work.loc[:,"origem"].apply(lambda x: padroniza_str(x))
    df_work["destino"] = df_work.loc[:,"destino"].apply(lambda x: padroniza_str(x))

    #df_work.to_csv("base_tratada.csv", index=False)
    # Conectar ao banco
    conn = sqlite3.connect(db_path)
    df_work.to_sql("DataClean", conn, if_exists="replace", index=False)
    conn.close()

    logger = logging.getLogger()

    #Gera uma falha no processo
    if not set(usecols).issubset(set(df.columns)):
        logger.error(f"Mudança de schema; {datetime.datetime.now()} ")
        raise Exception("Mudança de schema")
    
    final = datetime.datetime.now()
    print(f"DataClean finalizado: : {final}")
    return db_path
