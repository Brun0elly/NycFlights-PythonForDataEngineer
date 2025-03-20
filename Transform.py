import pandas as pd

def tempo_voo_horas(df, coluna_tempo):
    df["tempo_voo_horas"] = pd.to_timedelta(df[coluna_tempo], unit='m')  # Converte minutos para timedelta
    df["tempo_voo_horas"] = df["tempo_voo_horas"].apply(lambda x: str(x).split()[2] if len(str(x).split()) > 1 else str(x))  # Formata para HH:mm:ss
    
    return df


def turno_partida(df, coluna_datetime):
    # Garantir que a coluna esteja em formato datetime
    df[coluna_datetime] = pd.to_datetime(df[coluna_datetime], errors='coerce')

    def classificar_turno(hora):
        if 5 <= hora < 12:
            return "Manhã"
        elif 12 <= hora < 18:
            return "Tarde"
        elif 18 <= hora < 24:
            return "Noite"
        else:
            return "Madrugada"
          
    df["turno_partida"] = df[coluna_datetime].dt.hour.apply(classificar_turno)
    
    return df
