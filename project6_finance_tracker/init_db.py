import sqlite3 

def init_db():
    connection = sqlite3.connect('finance_tracker.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Accounts (
            account_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            account_type TEXT NOT NULL,
            is_active INTEGER NOT NULL DEFAULT 1
        )
        """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Categories (
            category_id INTEGER PRIMARY KEY,
            category_name TEXT NOT NULL,
            is_active INTEGER NOT NULL DEFAULT 1,
                   color TEXT NOT NULL DEFAULT '#a78bfa'
        )    
        """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Transactions (
            transaction_id INTEGER PRIMARY KEY,
            date TEXT NOT NULL,
            account_id INTEGER NOT NULL REFERENCES Accounts(account_id),
            category_id INTEGER NOT NULL REFERENCES Categories(category_id),
            transaction_type TEXT NOT NULL,
            amount FLOAT NOT NULL,
            description TEXT
        )
        """)
    connection.commit()
    connection.close()


