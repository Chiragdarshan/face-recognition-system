from flask import Flask, render_template, request, redirect, url_for, flash
import threading
import webbrowser
import subprocess
import sys

# Create Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Automatically open browser after server starts
def open_browser():
    webbrowser.open("http://127.0.0.1:5000/")

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'chirag' and password == '1234':
            flash('Login Successful!', 'success')
            # ✅ Launch student.py after login
            subprocess.Popen([sys.executable, "main.py"])
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

@app.route('/home')
def home():
    return "<h2>Welcome! You're logged in.</h2>"

if __name__ == '__main__':
    threading.Timer(1, open_browser).start()
    app.run(debug=True, use_reloader=False)
