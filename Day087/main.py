from flask import Flask, jsonify, render_template, redirect, url_for,request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import random
import os
from flask_ckeditor import CKEditor, CKEditorField

# Setting Up the Flask App and DB
SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY

ckeditor = CKEditor(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

# Initializing Classes
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
    coffee_price = db.Column(db.String(250), nullable=False)

class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    map_url = StringField("Cafe Location on Google Maps URL", validators=[DataRequired(), URL()])
    img_url = StringField("Cafe Image URL", validators=[DataRequired(), URL()])
    location = StringField('Location', validators=[DataRequired()])
    seats = StringField('Seats Available', validators=[DataRequired()])
    has_toilet = StringField('Has Toilet', validators=[DataRequired()])
    has_wifi = StringField('Has Wifi', validators=[DataRequired()])
    has_sockets = StringField('Has Sockets', validators=[DataRequired()])
    can_take_calls = StringField('Can Take Calls?', validators=[DataRequired()])
    coffee_price = StringField('Coffee Price', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CreateCafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    map_url = StringField("Cafe Location on Google Maps URL", validators=[DataRequired(), URL()])
    img_url = StringField("Cafe Image URL", validators=[DataRequired(), URL()])
    location = StringField('Location', validators=[DataRequired()])
    seats = StringField('Seats Available', validators=[DataRequired()])
    coffee_price = StringField('Coffee Price', validators=[DataRequired()])
    submit = SubmitField("Submit")

class CreateSearchForm(FlaskForm):
    location = StringField('Location', validators=[DataRequired()])
    submit = SubmitField("Submit")


# Setting Up Routes

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/cafes',methods=['GET'])
def cafes():
    cafes = db.session.query(Cafe).all()
    return render_template('cafes.html', cafes=cafes)



@app.route("/add", methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if request.method == 'POST':
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
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route("/cafe/<int:index>")
def show_cafe(index):

    cafes = db.session.query(Cafe).all()
    requested_cafe = None
    for cafe in cafes:
        if cafe.id == index:
            requested_cafe = cafe
    return render_template("cafes.html", cafe=requested_cafe, is_cafe=True)


@app.route("/search", methods=['POST', 'GET'])
def search_cafe():
    search_form = CreateSearchForm()
    if request.method == 'POST':
        user_input = search_form.location.data.title()
        cafe_results = Cafe.query.filter_by(location=user_input).all()
        if cafe_results == None:
            error_dict = {
                "error":
                    {
                        "NotFound": "Sorry, we don't have a cafe at that location"

                    }
            }
            return jsonify(error_dict)
        else:
            return render_template('cafes.html', cafes=cafe_results)
    return render_template('search.html', form=search_form)


@app.route('/edit-cafe/<cafe_id>', methods=['GET', 'POST', 'PATCH'])
def edit_cafe(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    edit_form = CreateCafeForm(name=cafe.name, map_url=cafe.map_url, img_url=cafe.img_url, location=cafe.location,
                               seats=cafe.seats, coffee_price=cafe.coffee_price)

    if edit_form.validate_on_submit():
        cafe.name = edit_form.name.data
        cafe.map_url = edit_form.map_url.data
        cafe.img_url = edit_form.img_url.data
        cafe.location = edit_form.location.data
        cafe.seats = edit_form.seats.data
        cafe.coffee_price = edit_form.coffee_price.data
        db.session.commit()
        return redirect(url_for('show_cafe', index=cafe_id))
    return render_template('edit_cafe.html', form=edit_form)


@app.route('/delete/<cafe_id>', methods=['GET', 'DELETE'])
def delete_cafe(cafe_id):
    cafe_to_delete = Cafe.query.get(cafe_id)
    db.session.delete(cafe_to_delete)
    db.session.commit()
    return redirect(url_for('cafes'))

if __name__ == '__main__':
    app.run(debug=True)


