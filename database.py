import sqlite3
import pandas as pd
from datetime import date

DB_PATH = "data/tracker.db"

def get_conn():
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    
    conn = get_conn()
    conn.executescript("""
                       
        CREATE TABLE IF NOT EXISTS contacts (...);
        CREATE TABLE IF NOT EXISTS daily_log (...);
        CREATE TABLE IF NOT EXISTS goals (...)
        """)
    conn.commit(); conn.close()
    
def get_funnel():
    
    conn = get_conn()
    cur = conn.execute("""
        SELECT COUNT(*) AS sent,
        SUM(CASE WHEN status IN ('replied', 'call', 'closed)
            THEN 1 ELSE 0 END) AS replied ...
    """)
    return dict(cur.fetchone())

