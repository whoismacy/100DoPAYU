from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os
import man_db as mdb

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('secret_key')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
    return mdb.user_exists(id)
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        if mdb.email_exists(email):
            flash("Email exists, consider logging in.")
            return redirect(url_for("login"))
        else:
            if mdb.add_user(email, password, name):
                flash("Registration Successful, you can now login", "success")
                return redirect(url_for('login'))
            else:
                flash("Registration Failed, please try again", "error")
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form.get("password")
        email = request.form.get("email")
        reg_user = mdb.check_user(email, password)
        if reg_user:
            login_user(reg_user)
            flash("Logged in successfully", "success")
            return redirect(url_for(('secrets')))
        else:
            flash("Login Failed, Check your email and Password", "error")
    return render_template('login.html')

@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/download')
def download():
    return send_from_directory('static', "files/cheat_sheet.pdf")

if __name__ == "__main__":
    app.run(debug=True)
