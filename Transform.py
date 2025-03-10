import pandas as pd

def tempo_voo_horas(df, coluna_tempo):
    """
    Converte a coluna de tempo de voo de minutos para horas.
    
    :param df: DataFrame contendo os dados.
    :param coluna_tempo: Nome da coluna com tempo de voo em minutos.
    :return: DataFrame com nova coluna `tempo_voo_horas`.
    """
    df["tempo_voo_horas"] = df[coluna_tempo] / 60
    return df

def turno_partida(df, coluna_hora, coluna_minuto):
    """
    Classifica o horário de partida do voo em turnos (manhã, tarde, noite, madrugada).
    
    :param df: DataFrame contendo os dados.
    :param coluna_hora: Nome da coluna com a hora de partida.
    :param coluna_minuto: Nome da coluna com os minutos de partida.
    :return: DataFrame com nova coluna `turno_partida`.
    """
    def classificar_turno(hora):
        if 5 <= hora < 12:
            return "Manhã"
        elif 12 <= hora < 18:
            return "Tarde"
        elif 18 <= hora < 24:
            return "Noite"
        else:
            return "Madrugada"
    
    df["turno_partida"] = df[coluna_hora].apply(classificar_turno)
    return df