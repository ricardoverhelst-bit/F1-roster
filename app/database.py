import sqlite3
from pathlib import Path

DB_PATH = Path("data/f1_roster.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS teams (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        country TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS drivers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        number INTEGER,
        team_id INTEGER,
        FOREIGN KEY(team_id) REFERENCES teams(id)
    )
    """)

    conn.commit()
    conn.close()