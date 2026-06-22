from flask import Flask, redirect, url_for, render_template, request, flash
from init_db import init_db
from db.accounts import create_account, get_all_accounts, get_account, edit_account, delete_account
from db.categories import create_category, get_all_categories, get_category, edit_category, delete_category
from db.transactions import create_transaction, get_total_income, get_total_expense, get_all_transactions, get_transaction, get_transactions_by_filter, edit_transaction, delete_transaction
app = Flask(__name__)
app.secret_key = 'finance_secret_key'
init_db()

@app.route('/', methods=['GET'])
def index():
    total_income = get_total_income()[0] or 0
    total_expense = get_total_expense()[0] or 0
    balance = total_income - total_expense
    transaction_list = get_all_transactions()
    accounts_list = get_all_accounts()
    categories_list = get_all_categories()
    return render_template('index.html', total_income=total_income, total_expense=total_expense, balance=balance, transaction_list=transaction_list, accounts_list=accounts_list, categories_list=categories_list)

@app.route('/accounts', methods=['GET'])
def accounts_list_route():
    accounts_list = get_all_accounts()
    return render_template('accounts.html', accounts_list=accounts_list)

@app.route('/accounts/create', methods=['POST'])
def create_account_route():
    name = request.form['name']
    account_type = request.form['account_type']
    result = create_account(name, account_type)
    if result:
        return redirect(url_for('accounts_list_route'))
    else:
        flash("Unsuccessful Account Creation")
        return redirect(url_for('accounts_list_route'))

@app.route('/accounts/<account_id>/edit', methods=['POST'])
def edit_account_route(account_id):
    account_id = int(account_id)
    name = request.form['name']
    account_type = request.form['account_type']
    result = edit_account(account_id, name, account_type)
    if result:
        return redirect(url_for('accounts_list_route'))
    else:
        flash("Unsuccessful Account Edit") 
        return redirect(url_for('accounts_list_route'))
    
@app.route('/accounts/<account_id>/delete', methods=['POST'])
def delete_account_route(account_id):
    account_id = int(account_id)
    result = delete_account(account_id)
    if result:
        return redirect(url_for('accounts_list_route'))
    else:
        flash("Unsuccessful Account Deletion")
        return redirect(url_for('accounts_list_route'))

@app.route('/categories', methods=['GET'])
def categories_list_route():
    categories_list = get_all_categories()
    return render_template('categories.html', categories_list=categories_list)

@app.route('/categories/create', methods=['POST'])
def create_category_route():
    category_name = request.form['category_name']
    result = create_category(category_name)
    if result:
        return redirect(url_for('categories_list_route'))
    else:
        flash("Unsuccessful Category Creation")
        return redirect(url_for('categories_list_route'))

@app.route('/categories/<category_id>/edit', methods=['POST'])
def edit_category_route(category_id):
    category_id = int(category_id)
    category_name = request.form['category_name']
    result = edit_category(category_id, category_name)
    if result:
        return redirect(url_for('categories_list_route'))
    else:
        flash("Unsuccessful Category Edit")
        return redirect(url_for('categories_list_route'))
    
@app.route('/categories/<category_id>/', methods=['GET'])
def view_category_route(category_id):
    category_id = int(category_id)
    category_name = get_category(category_id)
    category_transactions = get_transactions_by_filter(None, category_id)
    return render_template('view_category.html', category_name=category_name, category_transactions=category_transactions)
    
@app.route('/categories/<category_id>/delete', methods=['POST'])
def delete_category_route(category_id):
    category_id = int(category_id)
    result = delete_category(category_id)
    if result:
        return redirect(url_for('categories_list_route'))
    else:
        flash("Unsuccessful Category Deletion")
        return redirect(url_for('categories_list_route'))

@app.route('/transactions', methods=['GET'])
def transactions_list_route():
    transaction_type = request.args.get('transaction_type') or None
    category_id = request.args.get('category_id') or None
    accounts_list = get_all_accounts()
    categories_list = get_all_categories()
    if 'transaction_type' in request.args or 'category_id' in request.args:
        if category_id is not None:
            category_id = int(category_id)
        transactions_list = get_transactions_by_filter(transaction_type, category_id)
        return render_template('transactions.html', transactions_list=transactions_list, accounts_list=accounts_list, categories_list=categories_list)
    else:
        transactions_list = get_all_transactions()
        return render_template('transactions.html', transactions_list=transactions_list, accounts_list=accounts_list, categories_list=categories_list)

@app.route('/transactions/create', methods=['POST'])
def create_transaction_route():
    date = request.form['date']
    account_id = request.form['account_id']
    category_id = request.form['category_id']
    transaction_type = request.form['transaction_type']
    amount = request.form['amount']
    description = request.form['description']
    account_id = int(account_id)
    category_id = int(category_id)
    amount = float(amount)
    result = create_transaction(date, account_id, category_id, transaction_type, amount, description)
    if result:
        return redirect(url_for('transactions_list_route'))
    else:
        flash("Unsuccessful Transaction")
        return redirect(url_for('transactions_list_route'))
    
@app.route('/transactions/<transaction_id>/edit', methods=['POST'])
def edit_transaction_route(transaction_id):
    category_id = request.form['category_id']
    transaction_type = request.form['transaction_type']
    amount = request.form['amount']
    description = request.form['description']
    transaction_id = int(transaction_id)
    category_id = int(category_id)
    amount = float(amount)
    result = edit_transaction(transaction_id, category_id, transaction_type, amount, description)
    if result:
        return redirect(url_for('transactions_list_route'))
    else:
        flash("Unsuccessful Transaction Edit")
        return redirect(url_for('transactions_list_route'))

@app.route('/transactions/<transaction_id>/delete', methods=['POST'])
def delete_transaction_route(transaction_id):
    transaction_id = int(transaction_id)
    result = delete_transaction(transaction_id)
    if result:
        return redirect(url_for('transactions_list_route'))
    else:
        flash("Unsuccessful Transaction")
        return redirect(url_for('transactions_list_route'))

if __name__ == '__main__': 
    app.run(debug=True)