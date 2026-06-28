import sqlite3

def create_transaction(date, account_id, category_id, transaction_type, amount, description):
    connection = None
    try:
        connection = sqlite3.connect('finance_tracker.db')
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Transactions (date, account_id, category_id, transaction_type, amount, description) VALUES (?, ?, ?, ?, ?, ?)", (date, account_id, category_id, transaction_type, amount, description))
        connection.commit()
        return cursor.rowcount > 0
    except sqlite3.Error:
        return False
    finally:
        if connection:
            connection.close()

def get_total_income():
    connection = None
    try:
        connection = sqlite3.connect('finance_tracker.db')
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("SELECT SUM (amount) FROM Transactions WHERE transaction_type = 'income'")
        return cursor.fetchone()
    except sqlite3.Error:
        return None
    finally:
        if connection:
            connection.close()

def get_total_expense():
    connection = None
    try:
        connection = sqlite3.connect('finance_tracker.db')
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("SELECT SUM (amount) FROM Transactions WHERE transaction_type = 'expense'")
        return cursor.fetchone()
    except sqlite3.Error:
        return None
    finally:
        if connection: 
            connection.close()

def get_recent_transactions(limit=3):
    connection = None
    try:
        connection = sqlite3.connect('finance_tracker.db')
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("SELECT Transactions.*, Accounts.name, Categories.category_name FROM Transactions JOIN Accounts ON Transactions.account_id = Accounts.account_id JOIN Categories ON Transactions.category_id = Categories.category_id ORDER BY date DESC LIMIT ?", (limit,))
        return cursor.fetchall()
    except sqlite3.Error:
        return []
    finally:
        if connection:
            connection.close()

def get_all_transactions():
    connection = None
    try:
        connection = sqlite3.connect('finance_tracker.db')
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("SELECT Transactions.*, Accounts.name, Categories.category_name FROM Transactions JOIN Accounts ON Transactions.account_id = Accounts.account_id JOIN Categories ON Transactions.category_id = Categories.category_id ORDER BY date DESC")
        return cursor.fetchall()
    except sqlite3.Error:
        return []
    finally:
        if connection:
            connection.close()

def get_transaction(transaction_id):
    connection = None
    try:
        connection = sqlite3.connect('finance_tracker.db')
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("SELECT Transactions.*, Accounts.name, Categories.category_name FROM Transactions JOIN Accounts ON Transactions.account_id = Accounts.account_id JOIN Categories ON Transactions.category_id = Categories.category_id WHERE transaction_id = ?", (transaction_id,))
        return cursor.fetchone()
    except sqlite3.Error:
        return None
    finally:
        if connection:
            connection.close()

def get_transactions_by_filter(transaction_type, category_id):
    connection = None
    try:
        connection = sqlite3.connect('finance_tracker.db')
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        base_query = "SELECT Transactions.*, Accounts.name, Categories.category_name FROM Transactions JOIN Accounts ON Transactions.account_id = Accounts.account_id JOIN Categories ON Transactions.category_id = Categories.category_id"
        conditions = []
        values = []
        if transaction_type is not None:
            conditions.append("transaction_type = ?")
            values.append(transaction_type)
        if category_id is not None:
            conditions.append("Transactions.category_id = ?")
            values.append(category_id)
        if conditions:
            base_query += " WHERE " + " AND ".join(conditions)
        base_query += " ORDER BY date DESC"

        cursor.execute(base_query, values)
        return cursor.fetchall()
    except sqlite3.Error:
        return []
    finally: 
        if connection:
            connection.close()

def edit_transaction(transaction_id, category_id, transaction_type, amount, description):
    connection = None
    try:
        connection = sqlite3.connect('finance_tracker.db')
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("UPDATE Transactions SET category_id = ?, transaction_type = ?, amount = ?, description = ? WHERE transaction_id = ?", (category_id, transaction_type, amount, description, transaction_id))
        connection.commit()
        return cursor.rowcount > 0
    except sqlite3.Error:
        return False
    finally:
        if connection:
            connection.close()
    
def delete_transaction(transaction_id):
    connection = None
    try:
        connection = sqlite3.connect('finance_tracker.db')
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Transactions WHERE transaction_id = ?", (transaction_id,))
        connection.commit()
        return cursor.rowcount > 0
    except sqlite3.Error:
        return False
    finally:
        if connection:
            connection.close()