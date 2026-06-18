import unittest
import sqlite3
import os

class TestFinanceTracker(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect('test_finance_tracker.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Accounts (
            account_id INTEGER PRIMARY KEY, name TEXT, account_type TEXT, is_active INTEGER DEFAULT 1)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Categories (
            category_id INTEGER PRIMARY KEY, category_name TEXT, is_active INTEGER DEFAULT 1)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Transactions (
            transaction_id INTEGER PRIMARY KEY, date TEXT, account_id INTEGER, category_id INTEGER, transaction_type TEXT, amount FLOAT, description TEXT)""")
        self.connection.commit()

    def test_create_account(self):
        self.cursor.execute("INSERT INTO Accounts (name, account_type) VALUES (?, ?)", ('Gcash', 'E-wallet'))
        self.connection.commit()
        self.cursor.execute("SELECT name FROM Accounts WHERE name = 'Gcash'")
        result = self.cursor.fetchone()
        self.assertEqual(result[0], 'Gcash')

    def test_create_category(self):
        self.cursor.execute("INSERT INTO Categories (category_name) VALUES (?)", ('Food',))
        self.connection.commit()
        self.cursor.execute("SELECT category_name FROM Categories WHERE category_name = 'Food'")
        result = self.cursor.fetchone()
        self.assertEqual(result[0], 'Food')

    def test_create_transaction(self):
        self.cursor.execute("INSERT INTO Transactions (date, account_id, category_id, transaction_type, amount, description) VALUES (?, ?, ?, ?, ?, ?)", ('June 18, 2026', '1', '1', 'Expense', '4600', 'Bought Lunch from Mcdo'))
        self.connection.commit()
        self.cursor.execute("SELECT date, account_id, category_id, transaction_type, amount, description FROM Transactions WHERE date = 'June 18, 2026' AND account_id = '1' AND category_id = '1' AND transaction_type = 'Expense' AND amount = '4600' AND description = 'Bought Lunch from Mcdo'")
        result = self.cursor.fetchone()
        self.assertEqual(result[0], 'June 18, 2026')

    def test_edit_account(self):
        self.cursor.execute("INSERT INTO Accounts (name, account_type) VALUES (?, ?)", ('Gcash', 'E-wallet'))
        self.connection.commit()
        self.cursor.execute("UPDATE Accounts SET name = ? WHERE name = 'Gcash'", ('Tarsi',))
        self.connection.commit()
        self.cursor.execute("SELECT name FROM Accounts WHERE name = 'Tarsi'")
        result = self.cursor.fetchone()
        self.assertEqual(result[0], 'Tarsi')

    def test_edit_category(self):
        self.cursor.execute("INSERT INTO Categories (category_name) VALUES (?)", ('Food',))
        self.connection.commit()
        self.cursor.execute("UPDATE Categories SET category_name = ? WHERE category_name = 'Food'", ('School',))
        self.connection.commit()
        self.cursor.execute("SELECT category_name FROM Categories WHERE category_name = 'School'")
        result = self.cursor.fetchone()
        self.assertEqual(result[0], 'School')

    def test_edit_transaction(self):
        self.cursor.execute("INSERT INTO Transactions (date, account_id, category_id, transaction_type, amount, description) VALUES (?, ?, ?, ?, ?, ?)", ('June 18, 2026', '1', '1', 'Expense', '4600', 'Bought Lunch from Mcdo'))
        self.connection.commit()
        self.cursor.execute("UPDATE Transactions SET amount = ? WHERE date = 'June 18, 2026'", (460,))
        self.connection.commit()
        self.cursor.execute("SELECT amount FROM Transactions WHERE date = 'June 18, 2026'")
        result = self.cursor.fetchone()
        self.assertEqual(result[0], 460)

    def test_delete_account(self):
        self.cursor.execute("INSERT INTO Accounts (name, account_type, is_active) VALUES (?, ?, ?)", ('Gcash', 'E-wallet', '1'))
        self.connection.commit()
        self.cursor.execute("UPDATE Accounts SET is_active = ? WHERE name = 'Gcash'", (0,))
        self.connection.commit()
        self.cursor.execute("SELECT is_active FROM Accounts WHERE is_active = '0'")
        result = self.cursor.fetchone()
        self.assertEqual(result[0], 0)

    def test_delete_category(self):
        self.cursor.execute("INSERT INTO Categories (category_name) VALUES (?)", ('Food',))
        self.connection.commit()
        self.cursor.execute("UPDATE Categories SET is_active = ? WHERE category_name = 'Food'", (0,))
        self.connection.commit()
        self.cursor.execute("SELECT is_active FROM Categories WHERE is_active = '0'")
        result = self.cursor.fetchone()
        self.assertEqual(result[0], 0)

    def test_delete_transaction(self):
        self.cursor.execute("INSERT INTO Transactions (date, account_id, category_id, transaction_type, amount, description) VALUES (?, ?, ?, ?, ?, ?)", ('June 18, 2026', '1', '1', 'Expense', '4600', 'Bought Lunch from Mcdo'))
        self.connection.commit()
        self.cursor.execute("DELETE FROM Transactions WHERE date = 'June 18, 2026'")
        self.connection.commit()
        self.cursor.execute("SELECT date FROM Transactions WHERE date = 'June 18, 2026'")
        result = self.cursor.fetchone()
        self.assertIsNone(result)

    def tearDown(self):
        self.connection.close()
        os.remove('test_finance_tracker.db')


if __name__ == '__main__':
    unittest.main()