from flask import Flask
import random

app = Flask(__name__)

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

@app.route("/")
def homepage():
    return "<h1 style='color:green; font-size:40px; font-weight:900;'>Guess a number between 0-9</h1>"\
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='countdown-0-9'>"

@app.route("/test")
def another():
    return "<h1 style='color: red; font-size: 60px; font-weight: 800; font-family: Helvetica, sans-serif;'>TOO LOW TRY AGAIN !!</h1>" \
           "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDRsd2VydjhhcnFmeGlmNHRnMTdqamo3cXdpdTZoa3ptb3k0dzg4aCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3OhXBaoR1tVPW/giphy.gif' alt='sad-cat'>"


@app.route("/<int:number>")
def router_value(number):
    random_value = random.randint(0, 9)
    if random_value > number > 0:
        return "<h1 style='color:red; font-size:60px; font-weight:800; font-family:Helvetica, sans-serif;'>TOO LOW TRY AGAIN !!</h1>"\
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDRsd2VydjhhcnFmeGlmNHRnMTdqamo3cXdpdTZoa3ptb3k0dzg4aCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3OhXBaoR1tVPW/giphy.gif' alt='sad-cat'>"
    elif number == random_value:
        return "<h1 style='color:green; font-size:60px; font-weight:800; font-family:Helvetica, sans-serif;'>Congratulations you done it.</h1>"\
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDdmbzY3NXNrMGhjdHp0Y2tjdHc1d25yOWFoMDVjaGRnMm1lYTRvNyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/xT8qBepJQzUjXpeWU8/giphy.gif' alt='great-you-done-it.'>"
    elif random_value < number < 9:
        return "<h1 style='color:red; font-size:60px; font-weight:800; font-family:Helvetica, sans-serif'>Too high try again !!</h1>"\
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDRsd2VydjhhcnFmeGlmNHRnMTdqamo3cXdpdTZoa3ptb3k0dzg4aCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3OhXBaoR1tVPW/giphy.gif' alt='sad-cat'>"
    else:
        return "<h1 style='color:red; font-size:60px; font-weight:800; font-family:Helvetica, sans-serif;'>VALUE SHOULD BE GREATER THAN 0 AND LESS THAN 9</h1>"\
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeG13cnVhdmR4aDh5MXJjNWdpN241bzM4cm1uM2NnOXNucGN6MjM5OSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/d1E1msx7Yw5Ne1Fe/giphy.gif' alt='no'>"

if __name__ == "__main__":
    app.run(debug=True)
