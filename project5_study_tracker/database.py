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
    connection = sqlite3.connect('study_sessions.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Sessions (subject, start_time, end_time, key_takeaways, productivity_rating) VALUES (?, ?, ?, ?, ?)", (subject, start_time, end_time, key_takeaways, productivity_rating))
    connection.commit()
    connection.close()

def get_all_sessions():
    connection = sqlite3.connect('study_sessions.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Sessions")
    sessions = cursor.fetchall()
    connection.close()
    return sessions

def delete_session(session_id,):
    connection = sqlite3.connect('study_sessions.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Sessions WHERE session_id = ?;", (session_id,))
    connection.commit()
    connection.close()

init_db()