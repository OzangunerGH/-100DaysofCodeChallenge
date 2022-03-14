from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get('https://api.npoint.io/316df46e158444ede945')
    result = response.json()
    return render_template("index.html", articles=result)


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/contact')
def contact_page():
    return render_template("contact.html")


@app.route('/post/<int:artid>')
def get_post(artid):
    response = requests.get('https://api.npoint.io/316df46e158444ede945')
    result = response.json()[artid]
    return render_template("post.html", article=result)


if __name__ == "__main__":
    app.run(debug=True)
