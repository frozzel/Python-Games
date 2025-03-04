from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/about')
def about():
    return "This is the about page."

@app.route('/contact')
def contact():
    # return "Contact us at contact@example.com."
    return json.dumps({'message': 'Contact us at', 'email': 'fro@me.com'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
