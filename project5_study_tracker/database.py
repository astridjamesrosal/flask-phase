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

def add_session(subject, start_time, end_time, key_takeaways, productivity_rating):
    connection = None
    try:
        connection = sqlite3.connect('study_sessions.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Sessions (subject, start_time, end_time, key_takeaways, productivity_rating) VALUES (?, ?, ?, ?, ?)", (subject, start_time, end_time, key_takeaways, productivity_rating))
        connection.commit()
    except sqlite3.Error:
        return False
    finally:
        if connection:
            connection.close()

def get_session(session_id):
    connection = None
    try:
        connection = sqlite3.connect('study_sessions.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Sessions WHERE session_id = ?;", (session_id,))
        return cursor.fetchone()
    except sqlite3.Error:
        return None
    finally:
        if connection:
            connection.close()

def get_all_sessions():
    connection = None
    try:
        connection = sqlite3.connect('study_sessions.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Sessions")
        return cursor.fetchall()
    except sqlite3.Error:
        return []
    finally:
        if connection:
            connection.close()

def delete_session(session_id,):
    connection = None
    try:
        connection = sqlite3.connect('study_sessions.db')
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Sessions WHERE session_id = ?;", (session_id,))
        connection.commit()
    except sqlite3.Error:
        return False
    finally:
        if connection:
            connection.close()