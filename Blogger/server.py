from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    res = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    return render_template('index.html', posts=res.json())

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# @app.route('/post')
# def post():
#     res = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
#     posts = res.json()
#     return render_template('post.html', posts=posts)

@app.route('/<int:post_id>')
def post_detail(post_id):
    res = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    posts = res.json()
    post = next((post for post in posts if post['id'] == post_id), None)
    if post is None:
        return "Post not found", 404
    return render_template('post.html', title=post['title'], subtitle=post['subtitle'], body=post['body'])

if __name__ == '__main__':
    app.run(debug=True, port=8080)