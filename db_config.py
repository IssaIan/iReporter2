import psycopg2
import os


# url = os.getenv('DATABASE_URL')
# test_url = os.getenv('DATABASE_URL')
url = "dbname='ireporter' host='localhost' port='5432' user='issa' password='Maina9176'"

def connection(url):
    conn = psycopg2.connect(url)
    return conn

def init_db():
    conn = connection(url)
    return conn

# def init_test_db():
#     conn = connection(test_url)
#     return conn

def create_tables():
    conn = connection(url)
    curr = conn.cursor()
    queries = tables()

    for query in queries:
        curr.execute(query)

    conn.commit()

def destroy_tables():
    pass

def tables():
    users = """CREATE TABLE IF NOT EXISTS users(
        user_id serial PRIMARY KEY NOT NULL,
        first_name character varying(50) NOT NULL,
        last_name character varying(50) NOT NULL,
        username character varying(50) NOT NULL,
        email character varying(50) NOT NULL,
        date_created timestamp with time zone DEFAULT ('now'::text):: date NOT NULL,
        password character varying(50) NOT NULL
    )"""
    incidents = """CREATE TABLE IF NOT EXISTS incidents (
        incident_id serial PRIMARY KEY NOT NULL,
        created_by numeric NOT NULL,
        type character varying(20) NOT NULL,
        description character varying (200) NOT NULL,
        status character varying(20) DEFAULT 0,
        location character varying(50) NOT NULL,
        created_on timestamp with time zone DEFAULT ('now'::text):: date NOT NULL
    )"""
    queries = [users, incidents]
    return queries