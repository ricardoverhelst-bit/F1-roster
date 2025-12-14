import sqlite3
from pathlib import Path

DB_PATH = Path("data/f1_roster.db")

def get_connection():
    return sqlite3.connect(DB_PATH)
