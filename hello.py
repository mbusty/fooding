# TODO: Get rid of 'user'

from ast import Sub
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Create a Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


# Index page, playing around with Jinja
@app.route('/')
def index():
    first_name = 'Miguel'
    return render_template('index.html', 
        first_name=first_name)

# Alternate page to use templates
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

# 404 Error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# 500 Error page
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template('name.html',
        name = name,
        form = form)



if __name__ == '__main__':
    app.run(debug=True, port=8080)