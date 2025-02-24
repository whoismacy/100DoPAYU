import time
from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

import books_lib as blib

class BookDescription(FlaskForm):
    book_name = StringField("Book Name:", validators=[DataRequired()])
    book_author = StringField("Book Author:", validators=[DataRequired()])
    book_rating = SelectField("Book Rating:", validators=[DataRequired()], choices=[0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
    submit_button = SubmitField("Add Book")

class EditRating(FlaskForm):
    book_rating = SelectField("New Rating:", validators=[DataRequired()], choices=[0, 0.5, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
    submit_button = SubmitField("Change Rating")

app = Flask(__name__)
app.config['SECRET_KEY'] = "&gd+vM$!$(5oTzHYc534"

all_books = blib.get_all_books()

@app.route('/')
def home():
    return render_template("index.html", books_data=all_books)

@app.route("/add", methods=["POST", "GET"])
def add():
    global all_books
    form = BookDescription()
    if form.validate_on_submit():
        rating = float(form.book_rating.data)
        blib.create_book(title=form.book_name.data, author=form.book_author.data, rating=rating)
        all_books = blib.get_all_books()
        return redirect(url_for("home"))
    return render_template("add.html", form=form)


@app.route("/edit_rating/<string:title>/<rating>", methods=["GET", "POST"])
def edit_rating(title, rating):
    global all_books
    form = EditRating()
    det_tuple = (title, rating)
    if form.validate_on_submit() and request.method == "POST":
        title = title
        new_rating = form.book_rating.data
        if blib.change_rating(title, new_rating):
            all_books = blib.get_all_books()
            return redirect(url_for('home'))
    return render_template("edit_rating.html", form=form, details=det_tuple)

@app.route("/delete/<string:title>/<string:author>", methods=["GET"])
def delete(title, author):
    global all_books
    for book in all_books:
        if book['title'] == title and book['author'] == author:
            if blib.delete_book(title):
                all_books = blib.get_all_books()
                # time.sleep(0.5)
                return redirect(url_for('home'))
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
