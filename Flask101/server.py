from flask import Flask
import json

app  = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/about')
def about():
    return "This is the about page."

@app.route('/contact')
def contact():
    return "This is the contact page. carl me at 1234567890"

if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=8080)
    app.run(debug=True, port=8080)