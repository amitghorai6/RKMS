import sqlite3

conn = sqlite3.connect("jobs.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    call_no TEXT,
    name TEXT,
    phone TEXT,
    status TEXT,
    engineer TEXT
)
""")

conn.commit()
conn.close()