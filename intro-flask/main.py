from flask import Flask

def make_underline(function):
    def wrapper():
        return f'<u>{function()}</u>'
    return wrapper

def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'
    return wrapper

def make_italic(function):
    def wrapper():
        return f'<em>{function()}</em>'
    return wrapper
app = Flask(__name__)

@app.route("/")
@make_bold
@make_italic
@make_underline
def welcome():
    return "Welcome to my Home Page!!"

@app.route("/bye")
def good_bye():
    return "Thank you for visiting bye !!"

@app.route("/name/<username>/<int:number>")
def greet(username, number):
    return f"<h1 style='text-align: center'>Greetings {username} you are {number} years old !!</h1>" \
            '<p>This is the first-most paragraph</p>' \
            '<img src="https://media.giphy.com/media/X8omQqfFyeq1a/giphy.gif?cid=ecf05e47knxoqkrvy23kle5v4tl7dtit3qxe8703qwufsqlm&ep=v1_gifs_search&rid=giphy.gif&ct=g" alt="Dragon">' \

app.run(debug=True)
