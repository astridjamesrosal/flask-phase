import sqlite3

def create_transaction(date, account_id, category_id, transaction_type, amount, description):
    connection = sqlite3.connect('finance_tracker.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Transactions (date, account_id, category_id, transaction_type, amount, description) VALUES (?, ?, ?, ?, ?, ?)", (date, account_id, category_id, transaction_type, amount, description))
    rows_affected = cursor.rowcount
    connection.commit()
    connection.close()
    if rows_affected == 0:
        return False
    else:
        return True

def get_total_income():
    connection = sqlite3.connect('finance_tracker.db')
    cursor = connection.cursor()
    cursor.execute("SELECT SUM (amount) FROM Transactions WHERE transaction_type = 'income'")
    total_income = cursor.fetchone()
    connection.close()
    return total_income

def get_total_expense():
    connection = sqlite3.connect('finance_tracker.db')
    cursor = connection.cursor()
    cursor.execute("SELECT SUM (amount) FROM Transactions WHERE transaction_type = 'expense'")
    total_expense = cursor.fetchone()
    connection.close()
    return total_expense

def get_recent_transactions(limit=3):
    connection = sqlite3.connect('finance_tracker.db')
    cursor = connection.cursor()
    cursor.execute("SELECT Transactions.*, Accounts.name, Categories.category_name FROM Transactions JOIN Accounts ON Transactions.account_id = Accounts.account_id JOIN Categories ON Transactions.category_id = Categories.category_id ORDER BY date DESC LIMIT ?", (limit,))
    recent_transactions_list = cursor.fetchall()
    connection.close()
    return recent_transactions_list

def get_all_transactions():
    connection = sqlite3.connect('finance_tracker.db')
    cursor = connection.cursor()
    cursor.execute("SELECT Transactions.*, Accounts.name, Categories.category_name FROM Transactions JOIN Accounts ON Transactions.account_id = Accounts.account_id JOIN Categories ON Transactions.category_id = Categories.category_id ORDER BY date DESC")
    transactions_list = cursor.fetchall()
    connection.close()
    return transactions_list

def get_transaction(transaction_id):
    connection = sqlite3.connect('finance_tracker.db')
    cursor = connection.cursor()
    cursor.execute("SELECT Transactions.*, Accounts.name, Categories.category_name FROM Transactions JOIN Accounts ON Transactions.account_id = Accounts.account_id JOIN Categories ON Transactions.category_id = Categories.category_id WHERE transaction_id = ?", (transaction_id,))
    single_transaction = cursor.fetchone()
    connection.close()
    return single_transaction

def get_transactions_by_filter(transaction_type, category_id):
    connection = sqlite3.connect('finance_tracker.db')
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
    results = cursor.fetchall()
    connection.close()
    return results

def edit_transaction(transaction_id, category_id, transaction_type, amount, description):
    connection = sqlite3.connect('finance_tracker.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE Transactions SET category_id = ?, transaction_type = ?, amount = ?, description = ? WHERE transaction_id = ?", (category_id, transaction_type, amount, description, transaction_id))
    rows_affected = cursor.rowcount
    connection.commit()
    connection.close()
    if rows_affected == 0:
        return False
    else:
        return True
    
def delete_transaction(transaction_id):
    connection = sqlite3.connect('finance_tracker.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Transactions WHERE transaction_id = ?", (transaction_id,))
    rows_affected = cursor.rowcount
    connection.commit()
    connection.close()
    if rows_affected == 0:
        return False
    else:
        return True