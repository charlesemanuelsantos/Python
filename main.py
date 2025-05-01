import os
from dotenv import load_dotenv
import psycopg2 as pg

# Carregar variáveis do .env
load_dotenv()

# Ler variáveis de ambiente
config = {
    'dbname': os.getenv('POSTGRES_DB'),
    'user': os.getenv('POSTGRES_USER'),
    'password': os.getenv('POSTGRES_PASSWORD'),
    'host': os.getenv('POSTGRES_HOST'),
    'port': os.getenv('POSTGRES_PORTA'),
}

try:
    conn = pg.connect(**config)
    with conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT version();')
            print('Conectado ao Banco de Dados. Versão do PostgreSQL:', cursor.fetchone())

except Exception as e:
    print("Erro na conexão:", e)