from flask import Flask, render_template, request, url_for, redirect
import requests
import smtplib


def send_email(e_mail_variable, name, mail_text):
    """Sends an e-mail to recipient(s) on their birthday."""
    my_email = "danielkutcher92@gmail.com"
    password = "A123654789b."
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=f"{e_mail_variable}",
            msg=f"Subject:New User Form {name}!\n\n{mail_text}"
        )


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


@app.route('/form-entry', methods=['GET', 'POST'])
def form_entry():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        send_email(e_mail_variable=email, name=name, mail_text=message)
        return f'<h1>Your message {request.form["message"]} has been sent successfully {name}. You will be contacted via {email}.<h1>'


@app.route('/post/<int:artid>')
def get_post(artid):
    response = requests.get('https://api.npoint.io/316df46e158444ede945')
    result = response.json()[artid]
    return render_template("post.html", article=result)


if __name__ == "__main__":
    app.run(debug=True)
