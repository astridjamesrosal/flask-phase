import sqlite3 

def init_db():
    connection = sqlite3.connect('finance_tracker.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Accounts (
            account_id INTEGER PRIMARY KEY,
            name TEXT,
            account_type TEXT,
            is_active INTEGER DEFAULT 1
        )
        """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Categories (
            category_id INTEGER PRIMARY KEY,
            category_name TEXT,
            is_active INTEGER DEFAULT 1
        )    
        """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Transactions (
            transaction_id INTEGER PRIMARY KEY,
            date TEXT,
            account_id INTEGER,
            FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
            category_id INTEGER REFERENCES Categories(category_id),
            transaction_type TEXT,
            amount FLOAT,
            description TEXT
        )
        """)
    connection.commit()
    connection.close()


