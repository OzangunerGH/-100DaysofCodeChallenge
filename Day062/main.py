from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv


COFFEE_RATINGS = ['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕']
WIFI_RATINGS = ['💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪']
POWER_RATINGS = ['🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌']

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    open_time = StringField('Open Time', validators=[DataRequired()])
    close_time = StringField('Closing Time', validators=[DataRequired()])
    cf_rating = SelectField(u'Coffee Rating', choices=COFFEE_RATINGS, validators=[DataRequired()])
    wf_rating = SelectField(u'Wifi Rating', choices=WIFI_RATINGS, validators=[DataRequired()])
    pw_rating = SelectField(u'Power Outlet Rating', choices=POWER_RATINGS, validators=[DataRequired()])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = ""
        for element in form.data:
            if element == 'csrf_token' or element == 'submit':
                pass
            else:
                new_cafe += str(form.data[element])
                if element != 'pw_rating':
                    new_cafe += ','

        with open('cafe-data.csv', newline='', encoding='utf-8', mode='a') as csv_file:
            new_cafe += '\n'
            csv_file.writelines(new_cafe)
            return cafes()

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
