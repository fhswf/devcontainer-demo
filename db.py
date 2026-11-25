def init(conn):
    conn.execute("CREATE TABLE IF NOT EXISTS kunde "
                 "(id SERIAL PRIMARY KEY, name TEXT NOT NULL)")

def kunde_anlegen(conn, name):
    return conn.execute("INSERT INTO kunde (name) VALUES (%s) RETURNING id",
                        (name,)).fetchone()[0]

def anzahl(conn):
    return conn.execute("SELECT count(*) FROM kunde").fetchone()[0]
