import sqlite3

def create_category(category_name):
    connection = sqlite3.connect('finance_tracker.db')
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Categories (category_name) VALUES (?)", (category_name,))
    rows_affected = cursor.rowcount
    connection.commit()
    connection.close()
    if rows_affected == 0:
        return False
    else:
        return True

def get_all_categories():
    connection = sqlite3.connect('finance_tracker.db')
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT category_id, category_name, is_active FROM Categories WHERE is_active = 1")
    category_list = cursor.fetchall()
    connection.close()
    return category_list

def get_category(category_id):
    connection = sqlite3.connect('finance_tracker.db')
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT category_id, category_name, is_active FROM Categories WHERE category_id = ?", (category_id,))
    single_category = cursor.fetchone()
    connection.close()
    return single_category

def edit_category(category_id, category_name):
    connection = sqlite3.connect('finance_tracker.db')
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("UPDATE Categories SET category_name = ? WHERE category_id = ?", (category_name, category_id))
    rows_affected = cursor.rowcount
    connection.commit()
    connection.close()
    if rows_affected == 0:
        return False
    else:
        return True

def delete_category(category_id):
    connection = sqlite3.connect('finance_tracker.db')
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("UPDATE Categories SET is_active = 0 WHERE category_id = ?", (category_id,))
    rows_affected = cursor.rowcount
    connection.commit()
    connection.close()
    if rows_affected == 0:
        return False
    else:
        return True
