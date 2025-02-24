"""REST api using flask"""
import os
from flask import Flask, jsonify, render_template, request
import wifi_cafe_db as wcaf
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
app = Flask(__name__)

def require_api_key(func):
    def wrapper(*args, **kwargs):
        api_key = request.args.get("api_key")
        if api_key != API_KEY:
            return jsonify({"error": {"invalid": "your api key could not be recognized"}}), 400
        return func(*args, **kwargs)
    return wrapper


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random", methods=["GET"])
def random_cafe():
    cafe = wcaf.return_rand_cafe()
    return jsonify(cafe)

@app.route("/all", methods=["GET"])
def all_cafes():
    cafes = wcaf.return_all_cafes()
    return jsonify(cafes)

@app.route("/search", methods=["GET"])
def search():
    location = request.args.get("loc")
    return jsonify(wcaf.find_by_location(location))

@app.route("/add", methods=["POST"])
def add():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided"}), 400
        else:
            response = wcaf.add_restaurant(data.get("name"), data.get("map_url"),
                                           data.get("img_url"), data.get("location"),
                                           data.get("seats"), data.get("has_toilet"),
                                           data.get("has_wifi"), data.get("has_sockets"),
                                           data.get("can_take_calls"), data.get("coffee_price"))
            return jsonify(response)
    except Exception as e:
        return jsonify({"error": f"{e}"}), 500

@app.route("/update_price/<id>", methods=["GET", "PATCH"])
def price_update(id):
    new_price = request.args.get("new_price")
    print(new_price)
    cafe_id = int(id)
    return wcaf.update_price(cafe_id, new_price)

@app.route("/delete/<cafe_id>", methods=["DELETE"])
@require_api_key
def delete_cafe(cafe_id):
    if wcaf.drop_cafe(cafe_id):
        return jsonify({"success": {"cafe dropped": "cafe has been deleted"}}), 200
    return jsonify({"error": {"sorry": "could not handle delete request"}}), 400


if __name__ == '__main__':
    app.run(debug=True)

