import sqlite3

def create_account(name, account_type):
    connection = sqlite3.connect('finance_tracker.db')
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Accounts (name, account_type) VALUES (?, ?)", (name, account_type))
    rows_affected = cursor.rowcount
    connection.commit()
    connection.close()
    if rows_affected == 0:
        return False
    else:
        return True

def get_all_accounts():
    connection = sqlite3.connect('finance_tracker.db')
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT account_id, name, account_type, is_active FROM Accounts WHERE is_active = 1")
    accounts_list = cursor.fetchall()
    connection.close()
    return accounts_list

def get_account(account_id):
    connection = sqlite3.connect('finance_tracker.db')
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT account_id, name, account_type, is_active FROM Accounts WHERE account_id = ?", (account_id,))
    single_account = cursor.fetchone()
    connection.close()
    return single_account

def edit_account(account_id, name, account_type):
    connection = sqlite3.connect('finance_tracker.db')
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("UPDATE Accounts SET name = ?, account_type = ? WHERE account_id = ?", (name, account_type, account_id))
    rows_affected = cursor.rowcount
    connection.commit()
    connection.close()
    if rows_affected == 0:
        return False
    else:
        return True

def delete_account(account_id):
    connection = sqlite3.connect('finance_tracker.db')
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("UPDATE Accounts SET is_active = 0 WHERE account_id = ?", (account_id,))
    rows_affected = cursor.rowcount
    connection.commit()
    connection.close()
    if rows_affected == 0:
        return False
    else:
        return True