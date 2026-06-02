import sqlite3

def init_db():
    connection = sqlite3.connect('study_sessions.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Sessions (
            session_id INTEGER PRIMARY KEY,
            subject TEXT,
            start_time TEXT,
            end_time TEXT,
            key_takeaways TEXT,
            productivity_rating INTEGER
        )
        """)
    connection.commit()

    connection.close()

init_db()