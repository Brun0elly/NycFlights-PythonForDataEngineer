# 🛫 NYC Flights - Python For Data Engineer

## 📖 Descrição
Este projeto faz parte da disciplina "Python for Data Engineer" de pós-graduação e tem como objetivo aplicar transformações em um conjunto de dados de voos de NYC.

## 📂 Estrutura do Projeto
- `Main.py`: Script principal para executar as funções e visualizar os resultados.
- `DataClean.py`: Script utilizado na aula para limpeza dos dados.
- `Transform.py`: Contém as funções de transformação dos dados.
- `requirements.txt`: Lista de dependências necessárias para executar o projeto.
- `nycflights.db`: Sqlite que contém as tabelas que foram criadas no processamento do projeto(Tabelas:`DataClean` e `VoosTransformados`).

## ⚙️ Funcionalidades
### ✅ 1. Converter tempo de voo de minutos para horas
A função `tempo_voo_horas(df, coluna_tempo)` adiciona uma nova coluna ao DataFrame convertendo o tempo de voo de **minutos para horas**.

### ✅ 2. Classificar turno de partida
A função `turno_partida(df, coluna_datetime)` classifica os horários de partida nos seguintes períodos:
   - **Manhã**: das 5h às 11h59
   - **Tarde**: das 12h às 17h59
   - **Noite**: das 18h às 23h59
   - **Madrugada**: das 0h às 4h59

## 🔧 Como rodar o projeto
1. Clone o repositório:
   ```bash
   git clone https://github.com/DanielsOfficial0102/NycFlights-PythonForDataEngineer.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd NycFlights-PythonForDataEngineer
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o script principal:
   ```bash
   python main.py
   ```

## 👥 Grupo
### Bruno Elly Ferreira
### Bruno Pereira Lima
### Daniel Lopes Braga Santos
### Gabriel Anchieta de Sales
## 🔗 Link do GitHub do projeto:
### https://github.com/DanielsOfficial0102/NycFlights-PythonForDataEngineer