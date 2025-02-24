from flask import Flask, render_template, url_for, request
import requests
from dotenv import load_dotenv
import smtplib
import os

load_dotenv()

email = os.getenv("email")
passwords = os.getenv("passwd")
recipient = os.getenv("recipient")

try:
    response = requests.get("https://api.npoint.io/2bd62b30a106f88bec0d")
except Exception as e:
    print(f"Error accessing n-point API {e}")
else:
    data = response.json()
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html", data=data)

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/post/<number>")
def post(number):
    number = int(number)
    return render_template("post.html", num=number, blogposts=data)

@app.route("/form-entry", methods=["POST"])
def form_entry():
    if request.method == "POST":
        name = request.form['name']
        emails = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        content_to_send = f"Subject:Customer-Reach-Out\n\nName:{name}\ne-mail:{emails}\nphone:{phone}\nmessage:{message}"
        msgs = content_to_send.encode('utf-8')
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=passwords)
            connection.sendmail(from_addr=email,
                                to_addrs=recipient,
                                msg=content_to_send)
    return render_template("about.html")

@app.route("/test")
def test():
    return render_template("post.html")
if __name__ == "__main__":
    app.run(debug=True)