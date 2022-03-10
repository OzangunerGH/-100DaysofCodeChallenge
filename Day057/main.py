from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get('https://api.npoint.io/4af156202f984d3464c3')
    result = response.json()
    return render_template("index.html", articles=result)


@app.route('/post/<int:artid>')
def get_post(artid):
    response = requests.get('https://api.npoint.io/4af156202f984d3464c3')
    result = response.json()[artid - 1]
    return render_template("post.html", article=result)


if __name__ == "__main__":
    app.run(debug=True)
