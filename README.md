
# Investment Management App

## Visão Geral

O Investment Management App é uma aplicação para controle de investimentos que permite cadastrar ativos, registrar e visualizar histórico de preços, registrar compras e vendas de ativos, e gerar relatórios diversos. A aplicação utiliza PostgreSQL como banco de dados e a biblioteca yfinance para obter dados financeiros atualizados.

## Funcionalidades

- Cadastro de Ativos: Adicione e atualize ativos com informações como ticker, nome, setor, indústria, quantidade e valor atual.
- Histórico de Preços: Atualize o histórico de preços de ativos utilizando dados da biblioteca yfinance.
- Registro de Compras e Vendas: Registre compras e vendas de ativos com detalhes como data, ticker, quantidade, valor unitário e valor total.
- Listagem de Ativos: Visualize todos os ativos cadastrados com suas respectivas informações e valores.
- Relatórios: Gere relatórios sobre valorização/desvalorização de ativos e ganho em vendas.

## Pré-requisitos
- Python 3.8 ou superior
- PostgreSQL
- Biblioteca psycopg2 para conexão com PostgreSQL
- Biblioteca yfinance para obtenção de dados financeiros
- Biblioteca tkinter para interface gráfica


### Crie o banco de dados e as tabelas necessárias. Use o script SQL:

CREATE TABLE ativos (
    ticker VARCHAR(10) PRIMARY KEY,
    name VARCHAR(255),
    sector VARCHAR(255),
    industry VARCHAR(255),
    quantity NUMERIC DEFAULT 0,
    current_price NUMERIC DEFAULT 0
);

CREATE TABLE historico_precos (
    id SERIAL PRIMARY KEY,
    ticker VARCHAR(10) REFERENCES ativos(ticker),
    date DATE,
    open NUMERIC,
    low NUMERIC,
    high NUMERIC,
    close NUMERIC,
    volume NUMERIC
);

CREATE TABLE compras (
    id SERIAL PRIMARY KEY,
    data DATE,
    ticker VARCHAR(10) REFERENCES ativos(ticker),
    quantidade NUMERIC,
    valor_unitario NUMERIC,
    valor_total NUMERIC
);

CREATE TABLE vendas (
    id SERIAL PRIMARY KEY,
    data DATE,
    ticker VARCHAR(10) REFERENCES ativos(ticker),
    quantidade NUMERIC,
    valor_unitario NUMERIC,
    valor_total NUMERIC
);

### Execute o Programa

Use o comando no terminal: python main.py

## Autor

- [@eulergomees](https://github.com/eulergomees)
- [@wanessahela](https://github.com/wanessahelena)


## Referência

 - [Python](https://www.python.org/)
 - [yFinance](https://pypi.org/project/yfinance/)
 - [PostgreSQL](https://www.postgresql.org/)
 - [Psycopg2](https://www.psycopg.org/docs/#)

