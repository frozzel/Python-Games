from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Email

import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

class MyForm(FlaskForm):
    email = StringField('Email', [Email(message="Please Enter A Real Email"), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), validators.Length(min=8, max=35)])
    submit = SubmitField('Login')


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')  # Use the secret key from .env file
print(f"Secret Key: {app.secret_key}")


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login  ", methods=['GET', 'POST'])
def login():
    form = MyForm()
    
    if form.validate_on_submit():
        # Process the form data
        email = form.email.data
        password = form.password.data
        
        # Here you can add your logic to handle the login
        return f"Email: {email}, Password: {password}"
    else:
        # If the form is not valid, render the login page with the form
        return render_template('login.html', form=form)
    return render_template('login.html',  )


if __name__ == '__main__':
    app.run(port=8080, debug=True)
