import psycopg2
from psycopg2 import sql

DATABASE_CONFIG = {
    'dbname': 'investments',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

def create_connection():
    """Cria uma conexão com o banco de dados PostgreSQL."""
    return psycopg2.connect(**DATABASE_CONFIG)

def create_tables():
    """Cria as tabelas necessárias no banco de dados."""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ativos (
            ticker VARCHAR(10) PRIMARY KEY,
            name VARCHAR(100),
            sector VARCHAR(100),
            industry VARCHAR(100)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS historico_precos (
            ticker VARCHAR(10),
            date DATE,
            open NUMERIC,
            low NUMERIC,
            high NUMERIC,
            close NUMERIC,
            volume BIGINT,
            PRIMARY KEY (ticker, date),
            FOREIGN KEY (ticker) REFERENCES ativos (ticker)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS compras (
            id SERIAL PRIMARY KEY,
            data DATE,
            ticker VARCHAR(10),
            quantidade INTEGER,
            valor_unitario NUMERIC,
            valor_total NUMERIC,
            FOREIGN KEY (ticker) REFERENCES ativos (ticker)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendas (
            id SERIAL PRIMARY KEY,
            data DATE,
            ticker VARCHAR(10),
            quantidade INTEGER,
            valor_unitario NUMERIC,
            valor_total NUMERIC,
            FOREIGN KEY (ticker) REFERENCES ativos (ticker)
        )
    ''')

    conn.commit()
    cursor.close()
    conn.close()
