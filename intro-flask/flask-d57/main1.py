from flask import Flask, render_template, url_for
import random
from datetime import datetime
import requests

year = datetime.now().year

try:
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
except Exception as e:
    print(f"Error using n-point api {e}")
else:
    data = response.json()
app = Flask(__name__)

@app.route("/")
def homepage():
    random_number= random.randint(1, 10)
    return render_template("index1.html", num=random_number, year=year)

@app.route("/guess/<name>")
def guess_page(name):
    json = {
        "name": name
    }
    try:
        response = requests.get(" https://api.genderize.io", params=json)
    except Exception as e:
        print(f"Error while interacting with genderize API {e}")
    else:
        data = response.json()
        ggender = data['gender']
        gname = data['name'].title()
        gprobs = float(data['probability']) * 100

    return render_template("guess.html", name=gname, gender=ggender, probability=gprobs)

@app.route("/blog/<num>")
def blogs(num):
    try:
        response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    except Exception as e:
        print(f"Error using n-point api {e}")
    else:
        data = response.json()
    return render_template("blog.html", all_blogs=data)

@app.route("/new_blog")
def nblog():
    return render_template("index.html", blogposts=data)

@app.route("/read/<num>")
def read_more(num):
    num = int(num)
    return render_template("post.html", number=num, blogpost=data)

app.run(debug=True)

print(data)
print(data[0])

