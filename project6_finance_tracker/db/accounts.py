import sqlite3

def create_account(name, account_type):
    connection = None
    try:
        connection = sqlite3.connect('finance_tracker.db')
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Accounts (name, account_type) VALUES (?, ?)", (name, account_type))
        connection.commit()
        return cursor.rowcount > 0
    except sqlite3.Error: 
        return False
    finally:
        if connection:
            connection.close()

def get_all_accounts():
    connection = None
    try:
        connection = sqlite3.connect('finance_tracker.db')
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("SELECT account_id, name, account_type, is_active FROM Accounts WHERE is_active = 1")
        return cursor.fetchall()
    except sqlite3.Error:
        return []
    finally:
        if connection:
            connection.close()

def get_account(account_id):
    connection = None
    try:
        connection = sqlite3.connect('finance_tracker.db')
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("SELECT account_id, name, account_type, is_active FROM Accounts WHERE account_id = ?", (account_id,))
        return cursor.fetchone()
    except sqlite3.Error:
        return None
    finally:
        if connection:
            connection.close()

def edit_account(account_id, name, account_type):
    connection = None
    try:
        connection = sqlite3.connect('finance_tracker.db')
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("UPDATE Accounts SET name = ?, account_type = ? WHERE account_id = ?", (name, account_type, account_id))
        connection.commit()
        return cursor.rowcount > 0
    except sqlite3.Error:
        return False
    finally:
        if connection:
            connection.close()

def delete_account(account_id):
    connection = None
    try:
        connection = sqlite3.connect('finance_tracker.db')
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("UPDATE Accounts SET is_active = 0 WHERE account_id = ?", (account_id,))
        connection.commit()
        return cursor.rowcount > 0
    except sqlite3.Error:
        return False
    finally:
        if connection:
            connection.close()