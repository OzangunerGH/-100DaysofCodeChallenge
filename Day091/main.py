import os
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from colorthief import ColorThief

app = Flask(__name__)
SECRET_KEY = os.urandom(32)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY
app.config['UPLOAD_FOLDER'] = "/uploads/"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

bootstrap = Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/results', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        color_thief = ColorThief(f.filename)
        palette = color_thief.get_palette(color_count=11, quality=1)
        return render_template('results.html', colors=palette)


if __name__ == '__main__':
    app.run(debug=True)
