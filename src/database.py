import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="agentic_commerce",
        user="postgres",
        password="Mah@2005",
        host="localhost",
        port="5432"
    )
