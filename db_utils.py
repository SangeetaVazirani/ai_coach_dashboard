import sqlite3

def init_db():
    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS events (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date TEXT,
                        name TEXT,
                        event_type TEXT,
                        reminder INTEGER)""")
    conn.commit()
    conn.close()

def save_event(event_date, name, event_type, reminder):
    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO events (date, name, event_type, reminder) VALUES (?, ?, ?, ?)",
                   (event_date, name, event_type, reminder))
    conn.commit()
    conn.close()