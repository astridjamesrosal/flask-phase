import sqlite3

def create_category(category_name, color='#ffffff'):
    connection = None
    try:
        connection = sqlite3.connect('finance_tracker.db')
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Categories (category_name, color) VALUES (?, ?)", (category_name, color))
        connection.commit()
        return cursor.rowcount > 0
    except sqlite3.Error:
        return False
    finally:
        if connection:
            connection.close()

def get_all_categories():
    connection = None
    try:
        connection = sqlite3.connect('finance_tracker.db')
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("SELECT category_id, category_name, is_active, color FROM Categories WHERE is_active = 1")
        return cursor.fetchall()
    except sqlite3.Error:
        return []
    finally:
        if connection:
            connection.close()

def get_category(category_id):
    connection = None
    try:
        connection = sqlite3.connect('finance_tracker.db')
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("SELECT category_id, category_name, is_active FROM Categories WHERE category_id = ?", (category_id,))
        return cursor.fetchone()
    except sqlite3.Error:
        return None
    finally:
        if connection:
            connection.close()

def edit_category(category_id, category_name):
    connection = None
    try:
        connection = sqlite3.connect('finance_tracker.db')
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("UPDATE Categories SET category_name = ? WHERE category_id = ?", (category_name, category_id))
        connection.commit()
        return cursor.rowcount > 0
    except sqlite3.Error:
        return False
    finally:
        if connection:
            connection.close()

def delete_category(category_id):
    connection = None
    try:
        connection = sqlite3.connect('finance_tracker.db')
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("UPDATE Categories SET is_active = 0 WHERE category_id = ?", (category_id,))
        connection.commit()
        return cursor.rowcount > 0
    except sqlite3.Error:
        return False
    finally:
        if connection:
            connection.close()