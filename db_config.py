import psycopg2
import os
from psycopg2.extras import RealDictCursor


url = os.getenv('DB_URL')


def connection(url):
    conn = psycopg2.connect(url)
    return conn


def init_db():
    conn = connection(url)
    return conn


def create_tables():
    conn = connection(url)
    curr = conn.cursor(cursor_factory=RealDictCursor)
    queries = tables()

    for query in queries:
        curr.execute(query)

    conn.commit()


def tables():
    users = """CREATE TABLE IF NOT EXISTS users(
        user_id serial PRIMARY KEY NOT NULL,
        first_name character varying(100) NOT NULL,
        last_name character varying(100) NOT NULL,
        username character varying(100) NOT NULL,
        email character varying(100) NOT NULL,
        date_created timestamp with time zone DEFAULT ('now'::text):: date NOT NULL,
        phonenumber int,
        password character varying(150) NOT NULL
    )"""
    incidents = """CREATE TABLE IF NOT EXISTS incidents (
        incident_id serial PRIMARY KEY NOT NULL,
        created_by integer references users (user_id),
        type character varying(20) NOT NULL,
        description character varying (200) NOT NULL,
        status character varying(20) DEFAULT 0,
        location character varying(50) NOT NULL,
        created_on timestamp with time zone DEFAULT ('now'::text):: date NOT NULL
    )"""
    queries = [users, incidents]
    return queries


# def destroy_tables():
#     conn = connection(url)
#     curr = conn.cursor()

#     curr.execute("DROP TABLE users")
#     curr.execute("DROP TABLE incidents")
#     conn.commit()
