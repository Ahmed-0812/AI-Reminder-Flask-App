from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# ================= APP CONFIG =================
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ================= DATABASE =================
db = SQLAlchemy(app)

# ================= MODEL =================
class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    reminder_date = db.Column(db.String(20), nullable=False)

    reminder_time = db.Column(db.String(20), nullable=False)

# ================= CREATE DATABASE =================
with app.app_context():
    db.create_all()

# ================= HOME =================
@app.route('/')
def home():
    return redirect('/login')

# ================= LOGIN =================
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if username == "admin" and password == "1234":
            return redirect('/dashboard')

    return render_template('login.html')

# ================= REGISTER =================
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        return redirect('/login')

    return render_template('register.html')

# ================= DASHBOARD =================
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    if request.method == 'POST':

        task_title = request.form['task']

        reminder_date = request.form['reminder_date']

        reminder_time = request.form['reminder_time']

        new_task = Task(
            title=task_title,
            reminder_date=reminder_date,
            reminder_time=reminder_time
        )

        db.session.add(new_task)
        db.session.commit()

        return redirect('/dashboard')

    tasks = Task.query.all()

    return render_template('dashboard.html', tasks=tasks)

# ================= DELETE =================
@app.route('/delete/<int:id>')
def delete(id):

    task = Task.query.get(id)

    if task:
        db.session.delete(task)
        db.session.commit()

    return redirect('/dashboard')

# ================= RUN =================
if __name__ == '__main__':
    app.run(debug=True)