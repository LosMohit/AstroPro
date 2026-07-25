import sqlite3
import os

if not os.path.exists("data"):
    os.makedirs("data")

conn = sqlite3.connect("data/astro.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    dob TEXT,
    birth_time TEXT,
    birth_place TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS calendar_forecasts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    date TEXT,
    status TEXT,
    pros TEXT,
    cons TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")
conn.commit()


def save_user(name, dob, time, place):
    cursor.execute(
        """
    INSERT INTO users(name, dob, birth_time, birth_place)
    VALUES(?, ?, ?, ?)
    """,
        (name, dob, time, place),
    )
    conn.commit()
    return cursor.lastrowid


def save_daily_forecast(user_id, date, status, pros, cons):
    cursor.execute(
        """
    INSERT INTO calendar_forecasts(user_id, date, status, pros, cons)
    VALUES(?, ?, ?, ?, ?)
    """,
        (user_id, date, status, pros, cons),
    )
    conn.commit()
