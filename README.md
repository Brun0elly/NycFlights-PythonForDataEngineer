# 🛫 NYC Flights - Python For Data Engineer

## 📖 Descrição
Este projeto faz parte da disciplina de pós-graduação e tem como objetivo aplicar transformações em um conjunto de dados de voos de NYC.

## 📂 Estrutura do Projeto
- `Transform.py`: Contém as funções de transformação dos dados.
- `Main.py`: Script principal para executar as funções e visualizar os resultados.
- `requirements.txt`: Lista de dependências necessárias para executar o projeto.
- `DataClean.ipynb`: Notebook utilizado na aula para limpeza dos dados.
- `voos_transformados.csv`: Arquivo gerado com os dados transformados após a execução do `main.py`.

## ⚙️ Funcionalidades
### ✅ 1. Converter tempo de voo de minutos para horas
A função `tempo_voo_horas(df, coluna_tempo)` adiciona uma nova coluna ao DataFrame convertendo o tempo de voo de **minutos para horas**.

### ✅ 2. Classificar turno de partida
A função `turno_partida(df, coluna_hora, coluna_minuto)` classifica os horários de partida nos seguintes períodos:
   - **Manhã**: das 5h às 11h59
   - **Tarde**: das 12h às 17h59
   - **Noite**: das 18h às 23h59
   - **Madrugada**: das 0h às 4h59

## 🔧 Como rodar o projeto
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/NycFlights-PythonForDataEngineer.git
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
### Bruno Elly
### Bruno Lima
### Daniel Lopes
### Gabriel Anchieta
- 🔗 Link do GitHub do projeto:
#### https://github.com/DanielsOfficial0102/NycFlights-PythonForDataEngineer

- Print da publicação do projeto
- Print da execução do `main.py`