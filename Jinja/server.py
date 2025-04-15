from flask import Flask, render_template
import random
import datetime
import requests


app = Flask(__name__)
@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = datetime.datetime.now().year
    res = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    
    return render_template('index.html', random_number=random_number, year=year, posts=res.json())

@app.route('/guess/<name>')
def guess(name):
    res = requests.get(f'https://api.genderize.io?name={name}').json()
    gender = res['gender']
    response = requests.get(f'https://api.agify.io?name={name}')
    age = response.json()['age']
    return render_template('guess.html', name=name, gender=gender, age=age)

@app.route('/blog')
def blog():
    res = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    
    return render_template('blog.html', posts=res.json())

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    res = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    posts = res.json()
    post = next((post for post in posts if post['id'] == post_id), None)
    print(post)
    if post is None:
        return "Post not found", 404
    return render_template('post.html', title=post['title'], subtitle=post['subtitle'], body=post['body'])

if __name__ == '__main__':
    app.run(debug=True, port=8080)