import sqlite3

def create_transaction(date, account_id, category_id, transaction_type, amount):
    connection = sqlite3.connect('finance_tracker.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Transactions (date, account_id, category_id, transaction_type, amount) VALUES (?, ?, ?, ?, ?)", (date, account_id, category_id, transaction_type, amount))
    rows_affected = cursor.rowcount
    connection.commit()
    connection.close()
    if rows_affected == 0:
        return False
    else:
        return True

def get_all_transactions():
    connection = sqlite3.connect('finance_tracker.db')
    cursor = connection.cursor()
    cursor.execute("SELECT transaction_id, date, account_id, category_id, transaction_type, amount FROM Transactions")
    transactions_list = cursor.fetchall()
    connection.close()
    return transactions_list

def get_transaction(transaction_id):
    connection = sqlite3.connect('finance_tracker.db')
    cursor = connection.cursor()
    cursor.execute("SELECT transaction_id, date, account_id, category_id, transaction_type, amount FROM Transactions WHERE transaction_id = ?", (transaction_id,))
    single_transaction = cursor.fetchone()
    connection.close()
    return single_transaction

def get_transactions_by_filter(transaction_type, category_id):
    connection = sqlite3.connect('finance_tracker.db')
    cursor = connection.cursor()
    base_query = "SELECT transaction_id, date, account_id, transaction_type, category_id, amount FROM Transactions"
    conditions = []
    values = []
    if transaction_type is not None:
        conditions.append("transaction_type = ?")
        values.append(transaction_type)
    if category_id is not None:
        conditions.append("category_id = ?")
        values.append(category_id)
    if conditions:
        base_query += " WHERE " + " AND ".join(conditions)

    cursor.execute(base_query, values)
    results = cursor.fetchall()
    connection.close()
    return results

def edit_transaction(transaction_id, category_id, transaction_type, amount):
    connection = sqlite3.connect('finance_tracker.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE Transactions SET category_id = ?, transaction_type = ?, amount = ? WHERE transaction_id = ?", (category_id, transaction_type, amount, transaction_id))
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