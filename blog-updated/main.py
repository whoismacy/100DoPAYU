import os
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from flask_bootstrap import Bootstrap5
import man_db as mdb

app = Flask(__name__)
ckeditor = CKEditor(app)
app.config['SECRET_KEY'] = os.getenv('secret_key')
Bootstrap5(app)

posts = mdb.return_all()

class AddBlog(FlaskForm):
    blog_title = StringField("Title", validators=[DataRequired()])
    blog_subtitle = StringField("Subtitle", validators=[DataRequired()])
    blog_author = StringField("Author", validators=[DataRequired()])
    url_image = StringField("Image URL")
    blog_body = CKEditorField("Body", validators=[DataRequired()])
    submit = SubmitField("Submit Form")

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route('/post/<post_id>', methods=["GET"])
def show_post(post_id):
    post_id = int(post_id)
    requested_post = mdb.fetch_post(post_id)
    return render_template("post.html", post=requested_post)

@app.route('/new_post', methods=["GET", "POST"])
def add_post():
    global posts
    form = AddBlog()
    val = request.args.get("value")
    blog_id = request.args.get("id")
    if form.validate_on_submit():
        title = form.blog_title.data
        subtitle = form.blog_subtitle.data
        author = form.blog_author.data
        url = form.url_image.data
        body = form.blog_body.data
        if mdb.add_to_db(title, subtitle, author, url, body):
            posts = mdb.return_all()
            return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=form, value=val)

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit(post_id):
    global posts
    post = mdb.fetch_post(post_id)
    form = AddBlog(blog_title=post['title'], blog_subtitle=post['subtitle'], blog_author=post['author'], blog_body=post['body'])
    if form.validate_on_submit():
        if mdb.edit_blog(int(post_id), form.blog_title.data, form.blog_subtitle.data, form.blog_author.data, form.blog_body.data):
            post = mdb.fetch_post(post_id)
            posts = mdb.return_all()
            return render_template('post.html', post=post)
    return render_template("make-post.html", form=form)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/delete/<int:post_id>")
def delete(post_id):
    global posts
    if mdb.drop_blog(post_id):
        posts = mdb.return_all()
        return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(debug=True, port=5003)
