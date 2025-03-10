# NYC Flights - Python For Data Engineer

## Descrição
Este projeto tem como objetivo processar e transformar dados de voos, aplicando funções de conversão de tempo de voo e classificação do turno de partida.

## Estrutura do Projeto
- `Transform.py`: Contém as funções de transformação dos dados.
- `Main.py`: Script principal para executar as funções e visualizar os resultados.
- `requirements.txt`: Lista de dependências necessárias para executar o projeto.
- `DataClean.ipynb`: Notebook utilizado na aula para limpeza dos dados.

## Funcionalidades
### 1. Converter tempo de voo de horas para minutos
A função `tempo_voo_horas(df, coluna_tempo)` adiciona uma nova coluna ao DataFrame convertendo o tempo de voo de horas para minutos.

### 2. Classificar turno de partida
A função `turno_partida(df, coluna_horario)` classifica o horário de partida em Manhã, Tarde, Noite ou Madrugada.

## Como Executar
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

## Grupo
- Nome dos integrantes do grupo
- Link do GitHub do projeto
- Print da publicação do projeto
- Print da execução do `main.py`