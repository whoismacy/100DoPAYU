from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/login", methods=['POST', 'GET'])
def login_post():
    if request.method == "POST":
        name = request.form['usrname']
        passwd = request.form['passwd']
    return f"Successfully logged in: {name} ->{passwd}"

if __name__ == "__main__":
    app.run(debug=True)
