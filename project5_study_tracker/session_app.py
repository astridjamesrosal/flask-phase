from flask import Flask, redirect, url_for, render_template, request
from database import init_db, add_session, get_all_sessions, delete_session
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    sessions = get_all_sessions()
    return render_template('index.html', sessions=sessions)

@app.route('/add_session', methods=['GET', 'POST'])
def add_session_route():
    if request.method == 'GET':
        return render_template('add_session.html')
    if request.method == 'POST':
        subject = request.form['subject']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        key_takeaways = request.form['key_takeaways']
        productivity_rating = int(request.form['productivity_rating'])
        add_session(subject, start_time, end_time, key_takeaways, productivity_rating)
        return redirect(url_for('index'))

@app.route('/delete/<session_id>', methods=['POST'])
def delete_session_route(session_id):
    delete_session(session_id)
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    init_db()
    app.run(debug=True)