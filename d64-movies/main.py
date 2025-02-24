from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
import fetchmovies, renderdb
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os

# Creating an Add movie form
class AddMovie(FlaskForm):
    movie_name = StringField("Enter title of the Movie to Add:  ", validators=[DataRequired()])
    submit_button = SubmitField("Press to add New Movie")


# Creating an Edit movie form
class EditMovie(FlaskForm):
    new_rating = StringField("Input New Rating: ", validators=[DataRequired()])
    submit_button = SubmitField("Press to Edit")


# Creating an Edit movie form
class DeleteMovie(FlaskForm):
    movie_name = StringField("Re-enter name of the movie to confirm deletion (THIS ACTION CANNOT BE UNDONE): ", validators=[DataRequired()])
    submit_button = SubmitField("Press to Delete")


# Getting all the Movie Details, interacting with API
movies = ("memento", "se7en", "trainspotting")

get_movie = fetchmovies.FetchMovies()
get_movie.fetch_movie(*movies)

# Adding initial movies to db if they don't exist
renderdb.add_to_db(get_movie.get_as_list())

# Getting movie from the database
movie_list = renderdb.get_all()
movie_list_len = len(movie_list)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("CSRF_TOKEN")
Bootstrap5(app)

@app.route("/")
def home():
    return render_template("index.html", movie_list=movie_list, length=movie_list_len)

@app.route("/add", methods=["GET", "POST"])
def add_movie():
    global movie_list
    global movie_list_len
    form = AddMovie()
    if form.validate_on_submit():
        name = form.movie_name.data.title()
        get_movie.fetch_movie(name)
        renderdb.add_to_db(get_movie.get_as_list())
        movie_list = renderdb.get_all()
        movie_list_len = len(movie_list)
        return redirect(url_for('home'))
    return render_template('add.html', form=form)

@app.route("/edit/<movie>", methods=["GET", "POST"])
def edit_movie(movie):
    global movie_list
    global movie_list_len
    form = EditMovie()
    if form.validate_on_submit():
        name = movie.title()
        rating = form.new_rating.data
        if renderdb.edit_movie(name, rating):
            movie_list = renderdb.get_all()
            movie_list_len = len(movie_list)
            return redirect(url_for('home'))
    return render_template('edit.html', form=form)

@app.route("/delete/<movie>", methods=["GET", "POST"])
def delete_movie(movie):
    global movie_list
    global movie_list_len
    form = DeleteMovie()
    if form.validate_on_submit():
        name = form.movie_name.data.strip().title()
        if movie == name:
            if renderdb.drop_movie(name):
                movie_list = renderdb.get_all()
                movie_list_len = len(movie_list)
                return redirect(url_for('home'))
    return render_template('delete.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
