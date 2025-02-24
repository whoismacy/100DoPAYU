from flask import Flask, render_template, flash, request, url_for
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5

class Login(FlaskForm):
    email = StringField("Email:", validators=[Email(), DataRequired(), Length(min=12)])
    password = PasswordField("Password:", validators=[Length(min=8, max=32), DataRequired()])
    submit = SubmitField("submit")

app = Flask(__name__)
app.config['SECRET_KEY'] = '*47Ha!)M#hO*38(*T82*'
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def log_in():
    form = Login()
    if form.validate_on_submit() and request.method == "POST":
        if form.email.data == "admin@gmail.com" and form.password.data == "12345678":
            flash("Successful login", "success")
            return render_template("success.html")
        else:
            flash("Unsuccessful attempt", category='error')
            return render_template("denied.html")
    return render_template("login.html")

@app.route("/fill_in")
def fill_in():
    form = Login()
    return render_template("login.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
