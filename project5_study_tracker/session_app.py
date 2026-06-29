from flask import Flask, redirect, url_for, render_template, request, flash
from database import init_db, add_session, get_all_sessions, delete_session, get_session
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

init_db()

@app.route('/', methods=['GET'])
def index():
    sessions = get_all_sessions()
    return render_template('index.html', sessions=sessions)

@app.route('/add_session', methods=['GET', 'POST'])
def add_session_route():
    if request.method == 'GET':
        return render_template('add_session.html')
    if request.method == 'POST':
        subject = request.form['subject'].strip()
        start_time = request.form['start_time'].strip()
        end_time = request.form['end_time'].strip()
        key_takeaways = request.form['key_takeaways'].strip()
        if not all([subject, start_time, end_time, key_takeaways]):
            flash("Invalid Input, Please check your entries.", 'error')
            return render_template('add_session.html')
        productivity_rating = request.form['productivity_rating']
        try:
            productivity_rating = int(productivity_rating)
            if not (1 <= productivity_rating <= 5):
                flash("Invalid Rating, Please choose between 1 to 5", 'error')
                return render_template('add_session.html')
        except ValueError:
            flash("Invalid Rating, Please check your entry.", 'error')
            return render_template('add_session.html')
        add_session(subject, start_time, end_time, key_takeaways, productivity_rating)
        flash("Study Session created successfully!", 'success')
        return redirect(url_for('index'))

@app.route('/delete/<session_id>', methods=['POST'])
def delete_session_route(session_id):
    delete_session(session_id)
    flash("Study Session deleted Successfully", 'success')
    return redirect(url_for('index'))
    
@app.route('/confirm_delete/<session_id>', methods=['GET'])
def confirm_delete_session_route(session_id):
    session = get_session(session_id)
    if session is None:
        return redirect(url_for('index'))
    else:
        return render_template('delete_session.html', session=session)

if __name__ == '__main__':
    app.run(debug=False)