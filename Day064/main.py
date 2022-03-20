from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length
import requests


class MovieRatingForm(FlaskForm):
    review = StringField(label='Review', validators=[DataRequired(), Length(min=20)])
    rating = FloatField(label='Rating', validators=[DataRequired()])
    submit = SubmitField(label="Update")


class AddMovie(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    submit = SubmitField(label="Submit")


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Movie-database.db"
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float(250), nullable=True)
    ranking = db.Column(db.Integer(), nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


API_KEY = '661aca351e681f28e69fb3cfba98a5bd'
API_URL = 'https://api.themoviedb.org/3/search/movie'
db.create_all()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=['GET', 'POST'])
def edit_movie():
    form = MovieRatingForm()
    movie_id = request.args.get("id")
    selected_movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        selected_movie.rating = float(form.rating.data)
        selected_movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=selected_movie, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        response = requests.get(url=API_URL, params={"api_key": API_KEY, "query": form.title.data, "language": "en-US"})
        search_results = response.json()['results']
        return render_template('select.html', results=search_results)
    return render_template('add.html', form=form)


@app.route("/find", methods=['GET', 'POST'])
def find_movie():
    movie_id = request.args.get('id')
    if movie_id:
        parameters = {'api_key': API_KEY, "language": "en-US"}
        search_api = f"https://api.themoviedb.org/3/movie/{movie_id}"
        response = requests.get(url=search_api, params=parameters)
        results = response.json()
        title = results['original_title']
        image_url = f'https://image.tmdb.org/t/p/w500{results["poster_path"]}'
        year = results['release_date'].split('-')[0]
        description = results['overview']

        new_movie = Movie(title=title, img_url=image_url, year=year, description=description)
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit_movie", id=new_movie.id))


if __name__ == '__main__':
    app.run()
