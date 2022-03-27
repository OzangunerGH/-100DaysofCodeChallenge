from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Café TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.String(250), nullable=False)
    has_wifi = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.String(250), nullable=False)
    can_take_calls = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random", methods=['GET'])
def get_random_cafe():
    if request.method == 'GET':
        all_cafes = db.session.query(Cafe).all()
        rc = random.choice(all_cafes)
        return jsonify(cafe={
            "id": rc.id,
            "name": rc.name,
            "map_url": rc.map_url,
            "img_url": rc.img_url,
            "location": rc.location,
            "amenities": {"seats": rc.seats, "has_toilet": rc.has_toilet, "has_wifi": rc.has_wifi,
                          "has_sockets": rc.has_sockets, "can_take_calls": rc.can_take_calls,
                          "coffee_price": rc.coffee_price}
        })


@app.route("/all", methods=['GET'])
def get_all_cafe():
    if request.method == 'GET':
        cafes = db.session.query(Cafe).all()
        cafe_list = []
        for i in range(len(cafes)):
            new_json = {
                "id": cafes[i].id,
                "name": cafes[i].name,
                "map_url": cafes[i].map_url,
                "img_url": cafes[i].img_url,
                "location": cafes[i].location,
                "amenities": {"seats": cafes[i].seats, "has_toilet": cafes[i].has_toilet, "has_wifi": cafes[i].has_wifi,
                              "has_sockets": cafes[i].has_sockets, "can_take_calls": cafes[i].can_take_calls,
                              "coffee_price": cafes[i].coffee_price}
            }
            cafe_list.append(new_json)
        cafe_dict = {"cafes": cafe_list}
        return jsonify(cafe_dict)


@app.route("/search", methods=['GET'])
def search_cafe():
    if request.method == 'GET':
        location = request.args.get('location')
        rc = Cafe.query.filter_by(location=location).first()
        error_dict = {
            "error":
                {
                    "NotFound": "Sorry, we don't have a cafe at that location"

                }
        }

        if rc is None:
            return jsonify(error_dict)
        return jsonify(cafe={
            "id": rc.id,
            "name": rc.name,
            "map_url": rc.map_url,
            "img_url": rc.img_url,
            "location": rc.location,
            "amenities": {"seats": rc.seats, "has_toilet": rc.has_toilet, "has_wifi": rc.has_wifi,
                          "has_sockets": rc.has_sockets, "can_take_calls": rc.can_take_calls,
                          "coffee_price": rc.coffee_price}
        })


@app.route("/add", methods=['POST'])
def add_cafe():
    new_cafe = Cafe(name=request.form.get('name'),
                    map_url=request.form.get('map_url'),
                    img_url=request.form.get('img_url'),
                    location=request.form.get('location'),
                    seats=request.form.get('seats'), has_toilet=request.form.get('has_toilet'),
                    has_wifi=request.form.get('has_wifi'),
                    has_sockets=request.form.get('has_sockets'),
                    can_take_calls=request.form.get('can_take_calls'),
                    coffee_price=request.form.get('coffee_price')
                    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update-price/<cafe_id>", methods=['GET', 'POST', 'PATCH'])
def update_coffee_price(cafe_id):
    new_price = request.args.get('new_price')
    cafe_to_update = Cafe.query.get(cafe_id)
    if cafe_to_update is None:
        return jsonify({"error": {"Not Found": "Sorry a cafe with that id was not found in the database."}})
    else:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify({"success": "Successfully updated the price."})


@app.route("/report-closed/<cafe_id>", methods=['GET', 'POST','DELETE'])
def delete_cafe(cafe_id):
    api_key = request.args.get('api_key')
    if api_key == "TopSecretAPIKey":
        cafe_to_delete = Cafe.query.get(cafe_id)
        if cafe_to_delete is None:
            return jsonify({"error": {"Not Found": "Sorry a cafe with that id was not found in the database."}})
        else:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify({"success": "Successfully deleted the cafe from the database."})
    else:
        return jsonify({"error": "Sorry that is not allowed.Make sure you have the correct api_key."})


if __name__ == '__main__':
    app.run(debug=True)
