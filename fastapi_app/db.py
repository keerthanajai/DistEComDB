import psycopg2
import os
from urllib.parse import urlparse

DATABASE_URL = os.getenv("DATABASE_URL")
url = urlparse(DATABASE_URL)

def get_connection():
    return psycopg2.connect(
        dbname=url.path[1:], 
        user=url.username,
        host=url.hostname,
        port=url.port,
        sslmode="disable"
    )
