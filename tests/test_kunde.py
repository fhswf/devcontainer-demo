import psycopg
import pytest
from testcontainers.postgres import PostgresContainer
import db

@pytest.fixture
def conn():
    # jeder Test bekommt eine frische Datenbank
    with PostgresContainer("postgres:17", driver=None) as pg:
        with psycopg.connect(pg.get_connection_url()) as c:
            db.init(c)
            yield c

def test_kunde_anlegen(conn):
    db.kunde_anlegen(conn, "Ada")
    assert db.anzahl(conn) == 1

def test_start_ist_leer(conn):
    assert db.anzahl(conn) == 0
