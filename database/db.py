import psycopg2

from data import config

conn = psycopg2.connect(
    dbname=config.DB_NAME, # database name
    user=config.DB_USER, # user
    password=config.DB_PASS, # password
    host=config.DB_HOST, # host
    port=config.DB_PORT #port
)