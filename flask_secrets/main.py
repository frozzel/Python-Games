from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap5

import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

class MyForm(FlaskForm):
    email = StringField('Email', [Email(message="Please Enter A Real Email"), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), validators.Length(min=8, max=35)])
    submit = SubmitField('Login')


app = Flask(__name__)
bootstrap = Bootstrap5(app)

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
        
        print(f"Email: {email}")
        print(f"Password: {password}")
        # Check if the email and password match the environment variables
        print(f"Env Email: {os.getenv('EMAIL')}")
        print(f"Env Password: {os.getenv('PASSWORD')}")
        
        if email == os.getenv('EMAIL') and password == os.getenv('PASSWORD'):
            return render_template('success.html')
        else:
            return render_template('denied.html')
        
    else:
        # If the form is not valid, render the login page with the form
        return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
