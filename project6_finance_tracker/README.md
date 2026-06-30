# Orchid - Growth in every entry

> A self-directed Flask project for tracking personal finances.

Orchid tracks your finances where accounts hold your money, categories organize your spending, and transactions record what happened.

## Live Demo
[Orchid Finance Tracker](https://astridrosal.pythonanywhere.com/)

## Note
This app does not include user authentication. 
It is intended for a single user personal tool and for portfolio demonstration.

## Features
- Home Page for Displaying total income, total expense, current balance, and a preview of the 3 most recent transactions
- Accounts Page for actions such as create, edit, and delete financial accounts (Cash, E-wallet, Bank, Credit Card)
- Categories Page for creating, editing, and deleting categories. Click a category to view all transactions under it
- Transactions Page for creating, editing, and deleting transactions. Users can also filter by income, expense, or both

## Tech Stack
- Python / Flask
- SQLite
- Jinja2
- Vanilla CSS

## How to Run
1. Clone the repository
2. Navigate to `project6_finance_tracker/`
3. Create a virtual environment: `python -m venv .venv`
4. Activate it: `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (Mac/Linux)
5. Install dependencies: `pip install -r requirements.txt`
6. Create a `.env` file with: `SECRET_KEY=your_secret_key_here`
7. Run: `python finance_app.py`
8. Open `http://127.0.0.1:5000` in your browser

## What I Learned
- Modals over page navigation - Instead of redirecting to a new page for every action, modals provide a faster and cleaner experience for creating, editing, and deleting records without leaving the current page.
- Jinja2 template inheritance - Using `{% extends %}` and `{% block %}` allows every page to inherit the navbar and base layout from base.html, removing duplication and keeping templates clean and maintainable.
- Jinja2 conditions and syntax - Learning `{% if %}`, `{% for %}`, `{% endif %}`, and `{% endblock %}` made dynamic rendering of data possible across all pages.
- Empty strings vs None in Python - When a form submits an empty field, Flask receives an empty string, not None. Query filters that check if value is not None will still apply the filter with an empty string, causing incorrect results. Using or None explicitly converts empty strings to None so filters behave correctly.
- SQL column ambiguity in JOINs - When joining multiple tables that share a column name, SQL requires table-qualified column names such as Transactions.category_id to avoid ambiguous column errors.
- Error handling at the database layer - I wrapped every database function in try, except, and finally to prevent unhandled exceptions from crashing routes and to ensure connections are always closed, even on failure. When a function hits an error, it returns a safe default such as None or an empty list, so templates don't break when handling missing data.
- Client-side vs server-side validation - A dropdown limiting input in the browser does not prevent a direct POST request that bypasses the form entirely. Client-side restrictions are the first layer of defense, but they're not enough. Every route that converts form input to int or float needs its own server-side try/except as the actual line of defense.
- Securing the secret key with environment variables - A secret key should never live in source code, since anyone with repo access could read it and forge session cookies. Moving it to a .env file, out of version control, keeps it out of the codebase entirely.
- NOT NULL checks belong in the schema, not just the form - Form validation can be bypassed but database constraints cannot. Adding NOT NULL to required columns is the last line of defense against bad data.
- Deployed a Flask App to a live server through PythonAnywhere - Configure the default WSGI File to point PythonAnywhere towards my App. Created a virtual environment on the remote server to isolate my app's required packages. Set up the .env file on the server because it was initially created solely on my end, so I had to recreate it so that PythonAnywhere would also have it.

## What I Would Add in the Future
- Orchid petal category view — Each category displayed as an orchid where petal size reflects transaction volume; hovering a petal previews the transaction, clicking opens the full detail
- Dynamic balance color — Balance label turns red when negative, green when positive
- Spending insights — Charts showing spending by category and monthly income vs expense trends
- Budget limits per category — Set a monthly budget per category with a visual indicator when approaching or exceeding the limit

## Preview 
![Empty Main Page](static/images/Empty_Main_Page.jpg)
![Populated Main Page](static/images/Populated_Main_Page.jpg)
![Populated Accounts Page](static/images/Populated_Accounts_Page.jpg)
![Populated Categories Page](static/images/Populated_Categories_Page.jpg)
![View Categories Page](static/images/View_Categories_Page.jpg)
![Populated Transactions Page](static/images/Populated_Transactions_Page.jpg)