from flask import Flask
import json

app  = Flask(__name__)

def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def make_italic(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper
def make_underline(func):
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper
def make_emphasis(func):
    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper

@app.route('/')
def home():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
              "<p style='text-align: center'>This is a simple Flask application.</p>" \
                "<p style='text-align: center'>You can access different pages using the links below:</p>" \
                    "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdm9qaDVtaTl1NXhtaHRvZXllMTFhaWQ5cnF1Y3VvZ3I1OTN3endvbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/njtPBlbYnHAHK/giphy.gif' alt='Kitten' width: 200px style='display: flex, justify-content: center'>" \

@app.route('/about')
def about():
    return "This is the about page."

@app.route('/contact')
def contact():
    return "This is the contact page. carl me at 1234567890"

@app.route('/username/<name>') # <name> is a variable part of the URL
def greater(name):
    return f"Hello {name}!"

@app.route('/bye')
@make_bold
@make_italic
@make_underline
@make_emphasis
def bye():
    return "Bye!"

if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=8080)
    app.run(debug=True, port=8080)